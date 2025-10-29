
# TODO: 1 - Import the KnowledgeAugmentedPromptAgent and RoutingAgent
from workflow_agents import KnowledgeAugmentedPromptAgent
from workflow_agents import RoutingAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
base_url =  os.getenv('OPENAI_BASE_URL')

persona = "You are a college professor"

knowledge = "You know everything about Texas"
# TODO: 2 - Define the Texas Knowledge Augmented Prompt Agent

tx_knowledge_augmented_prompt_agent = KnowledgeAugmentedPromptAgent(openai_api_key, base_url, persona, knowledge)

knowledge = "You know everything about Europe"
# TODO: 3 - Define the Europe Knowledge Augmented Prompt Agent

eu_knowledge_augmented_prompt_agent = KnowledgeAugmentedPromptAgent(openai_api_key, base_url, persona, knowledge)

persona = "You are a college math professor"
knowledge = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
# TODO: 4 - Define the Math Knowledge Augmented Prompt Agent

math_knowledge_augmented_prompt_agent = KnowledgeAugmentedPromptAgent(openai_api_key, base_url, persona, knowledge)

routing_agent = RoutingAgent(openai_api_key, base_url, {})

agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        # TODO: 5 - Call the Texas Agent to respond to prompts
        "func": lambda x: tx_knowledge_augmented_prompt_agent.respond(x)
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        # TODO: 6 - Define a function to call the Europe Agent
        "func": lambda x: eu_knowledge_augmented_prompt_agent.respond(x)
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        # TODO: 7 - Define a function to call the Math Agent
        "func": lambda x: math_knowledge_augmented_prompt_agent.respond(x)
    }
]

routing_agent.agents = agents

# TODO: 8 - Print the RoutingAgent responses to the following prompts:
#           - "Tell me about the history of Rome, Texas"
#           - "Tell me about the history of Rome, Italy"
#           - "One story takes 2 days, and there are 20 stories"


user_inputs = ["Tell me about the history of Rome, Texas", "Tell me about the history of Rome, Italy",
              "One story takes 2 days, and there are 20 stories"]

for user_input in user_inputs:

    print(routing_agent.rout_prompts(user_input))
