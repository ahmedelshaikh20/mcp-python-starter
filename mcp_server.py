from mcp.server import FastMCP
from mcp import types
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


@mcp.tool(
    name = "read_doc" , 
    description = "Read the contents of a document. Input is the document name, output is the document contents.")
def read_doc(doc_id:str)-> str: 
    if doc_id not in docs:
        return "Document not found."
    return docs[doc_id]

@mcp.tool(
        name = "edit_document",
        description = "Edit the contents of a document. Input is the document name and new contents, output is a confirmation message.")
def edit_doc(doc_id: str, old_str: str, new_str: str):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)


@mcp.resource(
    name="documents", 
    uri="docs://documents",
    description="List all available documents",
    mime_type="application/json")
def list_docs()-> list[str]:
    return list(docs.keys())

@mcp.resource(
    name="read_doc",
    uri="docs://documents/{doc_id}",
    description="Read the contents of a document. Input is the document name, output is the document contents",
    mime_type="text/plain")
def read_doc(doc_id:str)-> str: 
    if doc_id not in docs:
        return "Document not found."
    return docs[doc_id]

@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format.")
def format_document(doc_id: str = Field(description="Id of the document to format")) -> str:
    prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:
<document_id>
{doc_id}
</document_id>

First, use the 'read_doc' tool to read the current content of the document.
Then, reformat it with proper markdown syntax including:
- Headers (# ## ###)
- Bullet points and lists  
- Bold/italic text formatting
- Code blocks if needed
- Tables if appropriate

Finally, use the 'edit_document' tool to replace the old content with the new markdown formatted version.

Show the user the reformatted content when complete.
"""
    
    return prompt

# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
