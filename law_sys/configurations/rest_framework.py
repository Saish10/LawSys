"""
REST Framework Settings
"""

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',

    ],

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/day',
        'user': '1000/day',
    },

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # JSON response format
    ],

    # Parser settings
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',  # JSON parser (default)
        'rest_framework.parsers.FormParser',  # Form data parser
        'rest_framework.parsers.MultiPartParser',  # File upload parser
    ],

    'EXCEPTION_HANDLER': 'base.utils.response.custom_exception_handler',

    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

    'DEFAULT_CACHE_TIMEOUT': 60 * 5,  # Cache timeout in seconds (Optional)

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'SEARCH_PARAM': 'search',
    'ORDERING_PARAM': 'ordering',

    'DATETIME_FORMAT': '%d-%m-%Y %H:%M:%S',  # (e.g., 23-12-24 14:30:00)
    'DATE_FORMAT': '%d-%m-%Y',  # Date format (e.g., 23-12-24)
    'TIME_FORMAT': '%H:%M:%S',  # Time format (e.g., 14:30:00)

    'DATETIME_INPUT_FORMATS': [
        '%d-%m-%Y %H:%M:%S',  # Day-Month-Year format with time
        '%d-%m-%Y',  # Date format (e.g., 23-12-2024)
    ],
    'DATE_INPUT_FORMATS': [
        '%d-%m-%Y',  # Date format with 4-digit year (e.g., 23-12-2024)
    ],
    'TIME_INPUT_FORMATS': [
        '%H:%M:%S',  # Standard time format (e.g., 14:30:00)
        '%I:%M %p',  # 12-hour format (e.g., 02:30 PM)
    ],

    'USE_L10N': True,  # Enable localized formatting
    'USE_TZ': True,  # Enable timezone-aware datetimes (requires pytz)

    'LANGUAGE_CODE': 'en-us',  # Default language code for the application
    'TIME_ZONE': 'UTC',  # Default timezone for the application
    "COERCE_DECIMAL_TO_STRING": False,

}

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,  # Disable session authentication
    "SECURITY_DEFINITIONS": {
        "Token": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
}