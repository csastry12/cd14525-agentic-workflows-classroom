# TODO: 1 - Import EvaluationAgent and KnowledgeAugmentedPromptAgent classes
from workflow_agents import EvaluationAgent
from workflow_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
base_url =  os.getenv('OPENAI_BASE_URL')
prompt = "What is the capital of France?"

# Parameters for the Knowledge Agent
persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"
# TODO: 2 - Instantiate the KnowledgeAugmentedPromptAgent here
knowledge_agent = knowledge_augmented_prompt_agent = KnowledgeAugmentedPromptAgent(openai_api_key, base_url, persona, knowledge) 

# Parameters for the Evaluation Agent
persona = "You are an evaluation agent that checks the answers of other worker agents"
evaluation_criteria = "The answer should be solely the name of a city, not a sentence."

# TODO: 3 - Instantiate the EvaluationAgent with a maximum of 10 interactions here

evaluation_agent = EvaluationAgent(openai_api_key, base_url, persona, evaluation_criteria, knowledge_agent, 10)

# TODO: 4 - Evaluate the prompt and print the response from the EvaluationAgent

evaluation_agent_response = evaluation_agent.evaluate(prompt)
print(evaluation_agent_response)
