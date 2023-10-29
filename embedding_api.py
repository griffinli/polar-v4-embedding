from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from fastapi.middleware.cors import CORSMiddleware

model = None

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

@app.on_event("startup")
async def load_model():
    global model
    model = SentenceTransformer('all-mpnet-base-v2')

@app.get("/embedding")
def read_root(q: str):

    embedding = model.encode(q)
    return {"embedding": embedding.tolist()}

@app.get("/health")
def read_health():

    return {"status": "healthy"}
