from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

model = ChatOpenAI()

schema = [
     ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
     ResponseSchema(name='fact_2',description='fact 2 about the topic'),
     ResponseSchema(name='senario_3',description='senario about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model|parser
result = chain.invoke({'topic':'sitaram from ramayan'})
print(result)