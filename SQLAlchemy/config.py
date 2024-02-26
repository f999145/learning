from pydantic_settings import BaseSettings, SettingsConfigDict
from pyodbc import drivers

class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_SERVER: str
    DB_DRIVER: str

    @property
    def DATABASE_URL_pyodbc(self):
        return rf"mssql+pyodbc://{self.DB_USER}:{self.DB_PASS}@{self.DB_SERVER}/{self.DB_NAME}?driver={self.DB_DRIVER}"

    # model_config = SettingsConfigDict(env_file='.env')


settings = Settings(DB_USER='parser', DB_PASS='1234!', DB_NAME='3WM_0901', DB_SERVER='id-olap', DB_DRIVER=drivers()[1])
