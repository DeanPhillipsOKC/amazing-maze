class MazeController:
    def __init__(self):
        maze_text = """
###############
#P          T #
##### ####### #
#   # #     # #
# # # # ### # #
# #   # # #   #
# ### # # #####
#   # # #     #
# # ### ##### #
# #     #   T #
##### ### #####
#     #   #   #
### ### ### # #
#   #   #   # #
# ########### #
#           E #
###############
"""
        self.maze_array = [list(line) for line in maze_text.strip().split("\n")]
        self.game_over = False

    def get_maze_map(self):
        """Returns a string that represents the game map."""
        return '\n'.join([''.join(row) for row in self.maze_array])

    def _get_player_location(self):
        """Finds the player's location in the maze."""
        for y, row in enumerate(self.maze_array):
            for x, cell in enumerate(row):
                if cell == 'P':
                    return x, y
        return None

    def _is_trap(self, x, y):
        """Checks if the specified location is a trap."""
        if 0 <= x < len(self.maze_array[0]) and 0 <= y < len(self.maze_array):
            return self.maze_array[y][x] == "T"
        return False

    def _is_exit(self, x, y):
        """Checks if the specified location is an exit."""
        if 0 <= x < len(self.maze_array[0]) and 0 <= y < len(self.maze_array):
            return self.maze_array[y][x] == "E"
        return False

    def _is_wall(self, x, y):
        """Checks if the specified location is a wall."""
        if 0 <= x < len(self.maze_array[0]) and 0 <= y < len(self.maze_array):
            return self.maze_array[y][x] == "#"
        return False

    def move_up(self):
        return self._move("up")

    def move_down(self):
        return self._move("down")

    def move_left(self):
        return self._move("left")

    def move_right(self):
        return self._move("right")

    def _move(self, direction):
        """Moves the player in the specified direction if possible."""
        if self.game_over:
            return "Game over. Cannot move."

        direction_map = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0)
        }

        if direction not in direction_map:
            return "Invalid direction. Use 'up', 'down', 'left', or 'right'."

        dx, dy = direction_map[direction]
        player_location = self._get_player_location()

        if player_location is None:
            return "Player not found in the maze."

        x, y = player_location
        new_x, new_y = x + dx, y + dy

        if self._is_trap(new_x, new_y):
            self.game_over = True
            return "The player has died. Game over."

        if self._is_exit(new_x, new_y):
            self.game_over = True
            return "The player has reached the exit.  Game over"

        if self._is_wall(new_x, new_y):
            return "Could not move the player. A wall is in the way."

        self.maze_array[y][x] = " "
        self.maze_array[new_y][new_x] = "P"
        return f"Moved the character {direction}!"
