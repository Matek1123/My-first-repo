from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from MY MCP"}

@app.get("/example-json")
def read_example():
    return {"message": "Hello from MCP Server!"}
