from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# RESTAPI -> app to app -> how software communicate with each other . 

@app.get("/")
def home_view():
    return {}

@app.post("/")
def home_detail_view():
    return {"hello":"world"}