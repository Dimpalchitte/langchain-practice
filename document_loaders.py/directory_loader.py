from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# DirectoryLoader needs a folder, not a file. Use the folder this script is in.
loader = DirectoryLoader(
    path=str(Path(__file__).parent),
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
