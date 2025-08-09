from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="template")


# Start with an empty list
persons = []

# Pydantic model for incoming data
class Person(BaseModel):
    name: str
    age: int
    isMarried: bool

# GET route to test
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "Marjan"})

# POST route to add a person
@app.post("/person")
def add_data(data: Person):
    persons.append(data.dict())  # convert Pydantic model to dict
    return {"message": "Person added", "data": data}



