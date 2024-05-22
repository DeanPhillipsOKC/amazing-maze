from langchain.prompts.prompt import PromptTemplate
from langchain.tools import Tool
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents.react.agent import create_react_agent
from langchain.agents import AgentExecutor

from tools.maze_controller import MazeController

def play():
    llm = ChatOpenAI(temperature=0, model="gpt-4")

    prompt_template_text = """
        You are going to play a game.  The object of the game is to navigate a maze using the
        tools at your disposal.  The map will be represented by printable ASCII characters.
        Here is the legend.
        
        Legend:
        P: Your current location
        T: A trap.  If your character enters this location it will die and the game will be over
        E: The exit.  If your character enters this location it will win the game.
        #: A wall.  If you try to move into one of these spaces your character location will not
           change.

        Here is an example game board:

        ###############
        # P         T #
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

        You need to move the P through the amaze one space at a time.  You can only move into
        empty spaces.  You cannot pass through walls (#).  If you run into a trap (T) you will die
        and the game will be over.  If you run into the exit (E), you win the game.
    """

    main_prompt = PromptTemplate(template=prompt_template_text, input_variables=[])

    maze_controller = MazeController()

    tool_bag = [
        Tool(
            name = "Display the maze map",
            func=maze_controller.get_maze_map,
            description="""Returns the string representing map including the location of the player, 
            walls, traps, and exit.  It takes no parameters"""
        ),
        Tool(
            name = "Move player up",
            func=maze_controller.move_up,
            description="Move the player up one space"
        ),
        Tool(
            name = "Move player down",
            func=maze_controller.move_down,
            description="Move the player down one space"
        ),
        Tool(
            name = "Move player left",
            func=maze_controller.move_left,
            description="Move the player left one space"
        ),
        Tool(
            name = "Move player right",
            func=maze_controller.move_right,
            description="Move the player right one space"
        ),
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools=tool_bag, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tool_bag, verbose=True, max_iterations=99)

    result = agent_executor.invoke(
        input={"input": main_prompt.format_prompt()}
    )

    linkedin_profile_url = result["output"]

if __name__ == "__main__":
    play()