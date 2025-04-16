from fastapi import FastAPI, Request  # add request to use
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routes.analytics import router as analytics_router
from routes.items import router as items_router
from routes.quiz import router as quiz_router

app = FastAPI()

app.include_router(items_router, prefix="/items")
app.include_router(analytics_router)
app.include_router(quiz_router)

templates = Jinja2Templates(directory="../frontend/")


@app.get("/home", response_class=HTMLResponse)
async def get_home(request: Request):  # modify to show index.html
    return templates.TemplateResponse("index.html", {"request": request})
