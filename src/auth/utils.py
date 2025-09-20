from src.settings import settings


def set_token_cookies(response, access_token):
    response.set_cookie(
        key='access_token',
        value=access_token,
        httponly=True,
        secure=True,
        samesite='strict',
        max_age=settings.EXPIRES_AT_ACCESS_TOKEN * 60
    )
