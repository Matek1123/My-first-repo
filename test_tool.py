# test_tools.py
from mcp.client import MCPClient

# Adres serwera MCP (lokalny lub Cloudflare)
# Lokalny:
url = "http://127.0.0.1:8080/sse"

# Publiczny Cloudflare (jeśli masz Tunnel):
# url = "https://xxxx.trycloudflare.com/sse"

# Tworzymy klienta MCP
client = MCPClient(url=url)

# Test narzędzia sum
result = client.sum(a=5, b=7)
print("Sum result:", result)  # powinno wydrukować: 12

# Test narzędzia get_weather
weather = client.get_weather(city="Warsaw")
print("Weather result:", weather)  # powinno wydrukować: Weather in Warsaw: 22 degrees C
