from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_book_desc(book_name):
    llm = OpenAI(temperature=0.7, model="gpt-3.5-turbo-0613")

    prompt_template_name = PromptTemplate(
        input_variables=['book_name'],
        template="i will give you the {book_name} give Writer name, and generate summary of that book at the end give link to access the book"
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    response = name_chain({'book_name':book_name})
    return response

if __name__ == "__main__":
    print(generate_book_desc('Rich dad poor dad'))  # Example: Pass the animal type as an argument
    #langchain_agent()
