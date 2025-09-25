from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
#from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import summarizer

app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="main.html"
    )

class Mail(BaseModel):
    body: str


@app.post("/summary/")
async def summary(Mail: Mail):
    result = summarizer.summary(Mail.body)
    return {"message": "Mail recieved successfully", "result":result[0], "result0":result[1]}
