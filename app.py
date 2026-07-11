from qna import ask_question
from learning_path import get_learning_path
from quiz_module import generate_quiz
from explanation_module import explain_concept
from summary_module import summarize_text
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )

from fastapi import Form

@app.post("/ask", response_class=HTMLResponse)
async def ask(request: Request, question: str = Form(...)):
    answer = ask_question(question)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "answer": answer
        }
    )

from fastapi import Form

@app.post("/summary", response_class=HTMLResponse)
async def summary(request: Request, notes: str = Form(...)):

    summary = summarize_text(notes)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "summary": summary
        }
    )

@app.post("/explain", response_class=HTMLResponse)
async def explain(request: Request, topic: str = Form(...)):

    explanation = explain_concept(topic)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "explanation": explanation
        }
    )

@app.post("/quiz", response_class=HTMLResponse)
async def quiz(request: Request, topic: str = Form(...)):

    quiz = generate_quiz(topic)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "quiz": quiz
        }
    )

@app.post("/learning", response_class=HTMLResponse)
async def learning(request: Request, topic: str = Form(...)):

    path = get_learning_path(topic)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "learning": path
        }
    )