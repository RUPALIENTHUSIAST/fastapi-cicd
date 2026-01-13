from fastapi import FastAPI

app= FastAPI()
@app.get("/")

def root():
    return {"message":"FastAPI deployed via CI/CD 1"}
