import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)

key = os.getenv("GOOGLE_API_KEY")

emb = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=key)
print("embeddings ok:", emb.embed_query("hello")[:3])

m = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=key)
print("chat ok:", m.invoke("say hi in 3 words").content)