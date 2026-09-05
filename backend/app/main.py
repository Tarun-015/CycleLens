from fastapi import FastAPI

app = FastAPI(
    title="CycleLens API",
    description="Women's Health and PCOS Pattern Assessment API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to CycleLens API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }