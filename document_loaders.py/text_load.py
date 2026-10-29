import sys
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

# Windows consoles default to cp1252 and can fail on some characters
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Resolve the file next to this script so it works from any working directory
text_path = Path(__file__).parent / 'cricket.txt'

loader = TextLoader(str(text_path), encoding='utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))
