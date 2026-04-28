from fastmcp import FastMCP
from main import app
mcp = FastMCP.from_fastapi(app=app)


if __name__ == "__main__":
     mcp.run(transport="http",host="127.0.0.1",port=8001)