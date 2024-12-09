from fastapi import FastAPI
from pydantic import BaseModelnpm 

app=FastAPI()

#http://127.0.0.1:8000/
@app.get("/")
async def test():
    return {"message": "Hello World"}
