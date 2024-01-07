import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Application Info
    app_name: str = "Library API"
    app_description: str = """
FASTAPI application to make the CURD operations in Library Management. 🚀

## Titles

Books <br/>
Users <br/>
Notes <br/>
Ratings <br/>

### Books

You will be able to:

* **Create books** accessed only by admins
* **Read books** accessed by admins/users
* **Update books** accessed only by admins
* **Delete books** accessed only by admins
* **Filter books** accessed by admins/users

### Users

You will be able to:

* **Create users** accessed only by admins
* **Read users** accessed only by admins
* **Update users** accessed by admins/user
* **Login users** accessed by admins/user
* **Delete users** accessed only by admins


    """
    api_summary: str = "CURD operations on Library API "
    api_contact: dict = {
        "name": "Naveen Ravi Chandran",
        "url": "https://naveenravi.onrender.com",
        "email": "naveen.cravi@gmail.com",
    }
    api_prefix: str = "/api/v1"
    api_version: str = "0.0.1"
    # Database
    database_uri: str = os.environ.get("postgre_uri")
    # JWT_config
    JWT_SECRET_KEY: str = os.environ.get(
        "jwt_secret_key", "e177df33-ceef-4e97-9657-eddaf6c92d17"
    )
    JWT_ACCESS_TOKEN_EXPIRE_TIME: int = int(
        os.environ.get("jwt_access_token_expire_time", 3600)
    )
    JWT_REFRESH_TOKEN_EXPIRE_TIME: int = int(
        os.environ.get("jwt_refresh_token_expire_time", 108000)
    )


settings: Settings = Settings()
