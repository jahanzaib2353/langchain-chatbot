from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

def generate_book_desc(Writer_name, book_name):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['Writer_name','book_name'],
        template="hy i have a {Writer_name}, i want to generate all his {book_name} quotes"
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    response = name_chain({'Writer_name': Writer_name, 'book_name':book_name})
    return response


def langchain_agent():

    llm = OpenAI(temperature=0.5)
    tools = load_tools(["wikipedia","llm-math"], llm=llm )

    agent = initialize_agent(
        tools, llm, agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose= True
    )

    result = agent.run(
        "What is the average age of a dog? multiply age of answer by 3"
    )
    print(result)
if __name__ == "__main__":
    # print(generate_book_desc("Jim Kiwik", 'limtless'))  # Example: Pass the animal type as an argument
    langchain_agent()