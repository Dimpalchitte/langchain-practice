from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

response_schemas = [
    ResponseSchema(name=f"fact_{i}", description=f"Interesting fact #{i} about the topic")
    for i in range(1, 6)
]
parser = StructuredOutputParser.from_response_schemas(response_schemas)

prompt = PromptTemplate(
    template="generate 5 intrsesting facts about {topic}\n\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

model = ChatOpenAI()
chain = prompt | model | parser
result = chain.invoke({"topic": "Cricket"})
print(result)
chain.get_graph().print_ascii()