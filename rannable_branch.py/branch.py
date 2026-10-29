from langchain_openai import ChatOpenAI
from langchian_core.prompts import PromptTemplate
from langchain_core.parsers import StructuredOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda

load_dotenv()

prompt1 = promptTemplate(
    input_variables={topic},
    template="Write a detailed report on {topic}"
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StructuredOutputParser()

report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence([report_gen_chain, branch_chain])

print(final_chain.invoke({"topic":"describe the impact of chanting ram naam from ramayan"}))