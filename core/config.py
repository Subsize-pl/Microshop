from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    name: str
    echo: bool = False

    @property
    def DB_URL_asyncpg(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class AuthJWT(BaseSettings):
    # делаем ключи необязательными, потому что читаем их из файлов
    private_key: str | None = None
    public_key: str | None = None

    algorithm: str
    access_token_expire_minutes: int

    private_key_path: str
    public_key_path: str

    def model_post_init(self, __context):
        # читаем файлы только если ключи ещё не заданы
        if not self.private_key:
            self.private_key = Path(self.private_key_path).read_text()
        if not self.public_key:
            self.public_key = Path(self.public_key_path).read_text()


class Settings(BaseSettings):
    db: DbSettings
    auth_jwt: AuthJWT

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
    )


settings = Settings()
