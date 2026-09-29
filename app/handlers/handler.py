from fastapi.responses import JSONResponse
import logging
from fastapi import Request
from sqlalchemy.exc import OperationalError
from psycopg2.errors import ForeignKeyViolation,UniqueViolation
from sqlalchemy.exc import IntegrityError


def success_response(data, message="Success", status=200):
    response = {
        "status": "success",
        "success": True,
        "message": message,
        "data": data
    }
    return JSONResponse(status_code=status, content=response)


def error_response(message="Something went wrong", status=500):
    response = {
        "status": "failed",
        "success": False,
        "message": message,
    }
    return JSONResponse(status_code=status, content=response)


logger = logging.getLogger(__name__)
async def database_unavailable(request: Request, exc: OperationalError):
    logger.error(
        "Database operation failed",
        exc_info=(type(exc), exc, exc.__traceback__),
    )
    return error_response(
        message="Database is temporarily unavailable. Please try again later.",
        status=503,
    )

async def integrity_error_handler(
    request: Request,
    exc: IntegrityError,
):
    if isinstance(exc.orig, UniqueViolation):
        return error_response(
            message="This record already exists.",
            status=409,
        )

    if isinstance(exc.orig, ForeignKeyViolation):
        return error_response(
            message="Cannot perform this operation because related records are linked.",
            status=409,
        )

    return error_response(
        message="Database constraint violation.",
        status=409,
    )