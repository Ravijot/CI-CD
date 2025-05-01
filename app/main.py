from fastapi import FastAPI

myapp = FastAPI()

@myapp.get("/check")
def read_root():
    return {"message": "Welcome to FastAPI"}

