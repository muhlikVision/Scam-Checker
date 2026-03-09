from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI(title="Scam Checker API")

# Create a basic "Health Check" route
@app.get("/")
async def root():
    return {"status": "online", "message": "Scam Checker Backend is running!"}