INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'apps.authentication',
    'apps.users',
    'apps.teams',
    'apps.projects',
    'apps.tasks',
]

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ],

}