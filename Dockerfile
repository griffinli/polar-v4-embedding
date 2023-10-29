FROM pytorch/pytorch
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "embedding_api:app", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 80
