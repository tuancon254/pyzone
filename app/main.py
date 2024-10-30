from fastapi import FastAPI
# Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/hello")
async def hello():
    return {"mesage": "hello"}