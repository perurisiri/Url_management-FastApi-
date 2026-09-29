from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config.db_config import create_db_and_tables
from app.controllers import language_controller, category_controller, url_controller
from sqlalchemy.exc import OperationalError,IntegrityError
from app.handlers.handler import database_unavailable
from app.handlers.handler import integrity_error_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
                                                                                                                                                              

app = FastAPI(title="URL Management",lifespan=lifespan)
app.add_exception_handler(
    IntegrityError,
    integrity_error_handler,
)
app.add_exception_handler(OperationalError, database_unavailable)

app.include_router(language_controller.router)
app.include_router(category_controller.router)
app.include_router(url_controller.router)