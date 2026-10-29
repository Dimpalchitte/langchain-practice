# LangChain Practice Projects

Hands-on examples for learning LangChain: prompts, chains, output parsers, structured output, document loaders, text splitters and vector stores.

## Contents

| Folder / file | What it covers |
|---|---|
| `simple_chain.py`, `parallel_chain.py` | Building basic and parallel chains |
| `stroutput_parser.py`, `pydanticOutputParser.py`, `structuredOutputParser.py` | Output parsers |
| `with_structured_output_*.py`, `Typeddict_demo.py`, `pydantic_demo.py` | Structured output with TypedDict, Pydantic and JSON |
| `rannable_branch.py/` | Runnables: branch, lambda, parallel, passthrough, sequence |
| `document_loaders.py/` | Text, CSV, PDF, directory and web loaders (with sample data) |
| `splitter.py/` | Text splitters: length, structure, markdown, code and semantic |
| `VECTOR_STORE.PY` | Chroma vector store: add, search, update, delete |

Note: some folders are named with a `.py` ending (for example `document_loaders.py/`). They are folders, not scripts.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

Create a `.env` file in the project root with your key (never commit this file):

```
OPENAI_API_KEY=your-key-here
```

## Run an example

```bash
python VECTOR_STORE.PY
python document_loaders.py/csv_loader.py
python splitter.py/markdown_splitting.py
```

PDF files are not included in this repo (copyright). To run `pdf_loader.py` or `directory_loader.py`, put your own PDF in `document_loaders.py/` (the scripts expect `dl-curriculum.pdf`).

Scripts that call OpenAI (chains, embeddings, semantic splitter, vector store) need an API key with available credits.
