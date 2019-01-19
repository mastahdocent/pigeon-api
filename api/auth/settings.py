import datetime

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_METHOD': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated'
    )
}

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'api.auth.utils.jwt_response_payload_handler',

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7)
}
