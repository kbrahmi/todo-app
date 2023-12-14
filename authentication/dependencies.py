from fastapi.security import OAuth2PasswordBearer


def get_oauth2_scheme():
    return OAuth2PasswordBearer(tokenUrl="/token")
