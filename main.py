from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

embedding_model=HuggingFaceEmbeddings()

vectorstore=Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model

)

retriever=vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":4,
        "fetch_k":10,
        "lambda_mult":0.5
    }
)

llm=ChatMistralAI(model="mistral-small-2506")

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""),
    (
        "human",
        """Context:
{context}

Question:
{question}
"""
    )
    ]
)

print("Rag System Created")

print("press 0 to exist")

while True:
    quary = input("You : ")
    if quary == "0":
        break

    docs=retriever.invoke(quary)

    context="\n\n".join(
        [doc.page_content for doc in docs]
    )

    final_prompt = prompt.invoke({
        "context":context,
        "question":quary
    })


    respons=llm.invoke(final_prompt)

    print(f"\n AI:{respons.content}")

