from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()
class person(BaseModel):
    name:str = Field(description = 'name of the person')
    age:int = Field( gt=18,description ='age of the person')
    city : str = Field(description = 'city of the person')

parser = PydanticOutputParser(pydantic_object=person)
template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser
final_result =chain.invoke({'place':'dhule'})
print(final_result)

