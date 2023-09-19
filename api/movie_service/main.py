from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

from movie_service import __version__
from movie_service.routers import actors, movies

app = FastAPI(
    title="IMDB (not really)",
    description="Example REST API built using Python, FastAPI and PostgreSQL.",
    docs_url=None,
    redoc_url=None,
    version=__version__,
    debug=True,
)

app.include_router(movies.router)
app.include_router(actors.router)


@app.get("/", include_in_schema=False)
async def swagger_docs():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title,
        swagger_css_url="https://cdn.statically.io/gh/Retloldin/swagger_ui_dark/main/main-page-dark-css.css",
        swagger_ui_parameters={"syntaxHighlight.theme": "monokai"},
    )
