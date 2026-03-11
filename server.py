<<<<<<< HEAD
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from MY MCP"}

@app.get("/example-json")
def read_example():
    return {"message": "Hello from MCP Server!"}
=======
# server.py
from mcp.server.fastmcp import FastMCP

# host="0.0.0.0" pozwala na dostęp spoza kontenera
mcp = FastMCP(name="Tool Example", port=8080, host="0.0.0.0")

@mcp.tool()
def sum(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def get_weather(city: str, unit: str = "celsius") -> str:
    return f"Weather in {city}: 22 degrees {unit[0].upper()}"

def main():
    print("MCP Server w Docker uruchomiony. SSE na porcie 8080")
    mcp.run("sse")

if __name__ == "__main__":
    main()
>>>>>>> b578f07 (Dodanie MCP i plików terminala)
