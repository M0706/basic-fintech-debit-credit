from src.exceptions.exceptions import (
    InvalidPayloadException,
    UpstreamConnectError,
    AuthenticationException,
    ConnectionError,
    InternalServerError
)
import json
from functools import wraps
from fastapi import HTTPException, status
from requests import ConnectionError as ConnError, ConnectTimeout
from pydantic import ValidationError
from src.logger import logger


def handle_exceptions_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        except (UpstreamConnectError, ConnError, ConnectTimeout) as e:
            logger.error(f"Error connecting upstream: {e}")
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, detail="Upstream service unavailable")

        except InvalidPayloadException as e:
            logger.error(f"Invalid payload error: {e}")
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Invalid payload")

        except (ConnectionError, AuthenticationException) as e:
            logger.error(f"Connection or Authentication error: {e}")
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")

        except InternalServerError as e:
            logger.error(f"Internal server error: {e}")
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unexpected error")

    return wrapper
