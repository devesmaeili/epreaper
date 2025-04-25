import logging
from typing import Any
from functools import wraps
from fastapi import HTTPException
from pydantic import BaseModel


class APIResponse(BaseModel):
    status: int
    log: str
    detail: str


class HTTPExceptions:
    def __init__(self, *args, **kwargs) -> None:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            try:
                resp: APIResponse = await func(*args, **kwargs)
            except Exception as exc:
                logging.critical(exc.__str__())
                raise HTTPException(status_code=500, detail=exc.__str__())

            if resp.status == 200:
                logging.info(resp.log)
                return resp.detail
            else:
                logging.error(resp.log)
                raise HTTPException(status_code=resp.status, detail=resp.detail)

        return wrapper
