import pytest
from tools.maze_controller import MazeController  # Assuming your class is in maze_controller.py

@pytest.fixture
def maze_controller():
    return MazeController()

def test_initial_player_location(maze_controller):
    assert maze_controller._get_player_location() == (1, 1)

def test_move_up_into_wall(maze_controller):
    result = maze_controller.move_up()
    assert result == "Could not move the player. A wall is in the way."

def test_move_down_into_wall(maze_controller):
    result = maze_controller.move_down()
    assert result == "Could not move the player. A wall is in the way."

def test_move_left_into_wall(maze_controller):
    result = maze_controller.move_left()
    assert result == "Could not move the player. A wall is in the way."

def test_move_right_into_wall(maze_controller):
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_down()
    result = maze_controller.move_right()
    assert result == "Could not move the player. A wall is in the way."

def test_move_right_into_trap(maze_controller):
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    result = maze_controller.move_right()  # This should hit the trap
    assert result == "The player has died. Game over."
    assert maze_controller.game_over

def test_get_maze_map(maze_controller):
    maze_map = maze_controller.get_maze_map()
    expected_map = """
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
""".strip()
    assert maze_map == expected_map

def test_invalid_move_direction(maze_controller):
    result = maze_controller._move("invalid")
    assert result == "Invalid direction. Use 'up', 'down', 'left', or 'right'.", "Invalid move direction should be handled properly."

def test_move_when_game_over(maze_controller):
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()  # This should hit the trap
    result = maze_controller.move_left()
    assert result == "Game over. Cannot move.", "No moves should be allowed after game over."

def test_move_to_exit_and_win(maze_controller):
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()

    maze_controller.move_down()
    maze_controller.move_down()
    maze_controller.move_down()
    maze_controller.move_down()

    maze_controller.move_left()
    maze_controller.move_left()

    maze_controller.move_up()
    maze_controller.move_up()

    maze_controller.move_left()
    maze_controller.move_left()
    
    maze_controller.move_down()
    maze_controller.move_down()
    maze_controller.move_down()
    maze_controller.move_down()
    
    maze_controller.move_right()
    maze_controller.move_right()
    
    maze_controller.move_down()
    maze_controller.move_down()
    
    maze_controller.move_right()
    maze_controller.move_right()
    
    maze_controller.move_down()
    maze_controller.move_down()

    maze_controller.move_left()
    maze_controller.move_left()
    
    maze_controller.move_down()
    maze_controller.move_down()

    maze_controller.move_left()
    maze_controller.move_left()

    maze_controller.move_down()
    maze_controller.move_down()

    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    maze_controller.move_right()
    result = maze_controller.move_right()
    
    assert result == "The player has reached the exit.  Game over"
    assert maze_controller.game_over

if __name__ == "__main__":
    pytest.main()
