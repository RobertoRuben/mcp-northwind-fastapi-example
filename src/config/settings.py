from pydantic_settings import BaseSettings
from urllib.parse import quote_plus


class Settings(BaseSettings):
    DB_ECHO_LOG: bool = True
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    @property
    def database_url(self) -> str:
        user = quote_plus(self.DB_USER)
        password = quote_plus(self.DB_PASSWORD)
        driver = quote_plus("ODBC Driver 18 for SQL Server")
        params = f"driver={driver}" "&TrustServerCertificate=yes"
        return (
            f"mssql+aioodbc://{user}:{password}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            f"?{params}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
