import sys
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

# Windows consoles default to cp1252 and fail on characters like bullets
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Resolve the PDF next to this script so it works from any working directory
pdf_path = Path(__file__).parent / 'dl-curriculum.pdf'

loader = PyPDFLoader(str(pdf_path))

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)
