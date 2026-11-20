from fastapi import FastAPI

app = FastAPI(
    title="Virtual Pet",
  description="Ein kleines virtuelles Haustier",
    version="0.1.0"
)

@app.get("/")
def home():
    return {"message": "Virtual Pet is running!"}
