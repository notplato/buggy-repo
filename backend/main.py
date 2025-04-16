from fastapi import FastAPI, Request  # add request to use
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.analytics import router as analytics_router
from routes.items import router as items_router
from routes.quiz import router as quiz_router

app = FastAPI()

app.include_router(items_router, prefix="/items")
app.include_router(analytics_router)
app.include_router(quiz_router)

templates = Jinja2Templates(directory="../frontend/")
app.mount(
    "/static", StaticFiles(directory="../frontend/"), name="static"
)  # add this for styles to work


# Asdding th navigation for everythin
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):  # modify to show index.html
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/home", response_class=HTMLResponse)
async def get_home_2(request: Request):  # modify to show index.html
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/items", response_class=HTMLResponse)
async def get_items(request: Request):  # modify to show index.html
    return templates.TemplateResponse("items.html", {"request": request})


@app.get("/analytics", response_class=HTMLResponse)
async def get_analytics(request: Request):  # modify to show index.html
    return templates.TemplateResponse("analytics.html", {"request": request})


@app.get("/news", response_class=HTMLResponse)
async def get_news(request: Request):  # modify to show index.html
    return templates.TemplateResponse("news.html", {"request": request})


@app.get("/quiz", response_class=HTMLResponse)
async def get_quiz(request: Request):  # modify to show index.html
    return templates.TemplateResponse("quiz.html", {"request": request})


@app.get("/profile", response_class=HTMLResponse)
async def get_profile(request: Request):  # modify to show index.html
    return templates.TemplateResponse("profile.html", {"request": request})
