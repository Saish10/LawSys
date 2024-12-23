"""
Response utils
"""

from rest_framework.views import exception_handler
from rest_framework.status import HTTP_413_REQUEST_ENTITY_TOO_LARGE
from rest_framework.response import Response
from django.core.exceptions import RequestDataTooBig


class APIResponse:
    """
    API Response
    """

    @staticmethod
    def success(message="", data=None):
        """
        Success
        """
        return {"message": message, "data": data}

    @staticmethod
    def error(message="", errors=None, data=None):
        """
        Error
        """
        return {
            "message": serialize_error_message(errors) if errors else message,
            "data": data,
        }


def serialize_error_message(errors):
    """
    Serialize error message
    """
    error = list(errors)[0]
    str_msg = errors[error][0]
    msg = (
        ""
        if error == "non_field_errors"
        else error.capitalize().replace("_", " ") + ", "
    )
    msg = msg + str_msg
    return msg


def custom_exception_handler(exc, context):
    """
    Custom exception handler
    """
    if isinstance(exc, RequestDataTooBig):
        response = APIResponse.error(
            message="Uploaded file is too large.",
        )
        return Response(response, status=HTTP_413_REQUEST_ENTITY_TOO_LARGE)

    response = exception_handler(exc, context)
    if response is not None:
        detail = response.data.get("detail", "")
        response.data = APIResponse.error(message=detail)

    return response
