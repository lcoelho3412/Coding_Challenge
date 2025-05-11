from fastapi import FastAPI

app = FastAPI(title="Marketing AI Assistant")

@app.get("/ping")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}