from fastapi import FastAPI
from routers import user

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Welcome to Fast API"}

# Include user routes
app.include_router(user.router)