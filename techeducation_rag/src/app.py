import json
from xmlrpc import client
import os
from rag.index_pdf import IndexPDF
from rag.query_rag import QueryRAG


def execute_rag():
    INDEX_FILE = "index.faiss"
    INDEX_FILE1 = "index1.faiss"
    index_pdf=IndexPDF()
    query_rag=QueryRAG()
    if not os.path.exists(INDEX_FILE1):
        pdf_path = os.path.join(os.path.dirname(__file__), "asset", "Python_Functions.pdf")
        index_pdf.create_index(pdf_path)
    else:
        print("⚡ Index already exists. Skipping indexing.")  
    while True:
        user_input=input("You:")   
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break  
        result=query_rag.generate_answer(query=user_input)
        print(f"Final Result: {result}") 
if __name__ == "__main__":   
        execute_rag()

