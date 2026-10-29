from pathlib import Path

from langchain_community.document_loaders import CSVLoader

# Resolve the CSV next to this script so it works from any working directory
csv_path = Path(__file__).parent / "Social_Network_Ads.csv"

loader = CSVLoader(file_path=str(csv_path), encoding="utf-8")
docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)
