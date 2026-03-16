from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
import json
import time
import yfinance as yf
import asyncio
import datetime

app = FastAPI()

# Health check endpoint
@app.get("/")
def root():
    return {"message": "Server is running. Go to /sse for events"}

# SSE endpoint
@app.get("/sse")
def sse():
    def event_stream():
        while True:
            yield f"data: ping - {time.time()}\n\n"
            time.sleep(5)
    return StreamingResponse(event_stream(), media_type="text/event-stream")

# New Weather endpoint (loads data from a JSON file)
@app.get("/weather")
async def get_weather():
    try:
        with open("data/weather_data.json") as f:
            weather_data = json.load(f)  # Loading weather data from JSON file
        return weather_data
    except Exception as e:
        return JSONResponse({"error": f"Error reading weather data: {str(e)}"}, status_code=500)

# Stock endpoint (using Yahoo Finance)
@app.get("/stock/{symbol}")
async def get_stock(symbol: str):
    try:
        stock = yf.Ticker(symbol)  # Create a ticker object using Yahoo Finance
        data = stock.history(period="1d")  # Get stock history for the last day
        return data.to_dict()  # Convert the stock data to a dictionary and return it
    except Exception as e:
        return JSONResponse({"error": f"Error fetching stock data: {str(e)}"}, status_code=500)

# Example tool endpoint for addition
@app.post("/call")
async def call_tool(request: Request):
    try:
        data = await request.json()
        tool = data.get("tool")
        args = data.get("args", {})

        # Tool 'sum' for adding numbers
        if tool == "sum":
            a = args.get("a", 0)
            b = args.get("b", 0)
            return JSONResponse({"result": a + b})
        else:
            return JSONResponse({"error": "Unknown tool"}, status_code=400)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

# Run the server with uvicorn when this script is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
