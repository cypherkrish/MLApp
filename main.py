from fastapi import FastAPI
from utils.common import PayLoad
from utils.operations import add_numbers

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World", "Status":"The app is running file"}


@app.post("/add")
def add_numbers_api(payload: PayLoad):
    result = add_numbers(payload.number_one, payload.number_two)
    return {"Hello": "World", "Sum":f"{result}"}
    
    
@app.get('/new')
def random():
    pass

