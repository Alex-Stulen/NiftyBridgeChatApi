from functools import wraps
from typing import Callable

from fastapi import status
from fastapi.responses import JSONResponse

from conf import settings


def is_auth(func: Callable) -> Callable:
    """ Verify user authorization by query header.
    If the authorization header is valid - returns the controller response,
    otherwise returns 401 error and json body """

    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header_data = kwargs.get(settings.AUTH_HEADER, '')

        if auth_header_data != settings.X_API_KEY_TOKEN:
            msg = {'detail': 'The authentication information provided is incorrect'}
            return JSONResponse(msg, status_code=status.HTTP_401_UNAUTHORIZED)

        return func(*args, **kwargs)

    return wrapper
