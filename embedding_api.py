from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from fastapi.middleware.cors import CORSMiddleware

model = SentenceTransformer('all-mpnet-base-v2')

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/embedding")
def read_root(q: str):

    embedding = model.encode(q)
    return {"embedding": embedding.tolist()}