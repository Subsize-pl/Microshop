from passlib.context import CryptContext


class PwdHelper:
    pwd_context: CryptContext

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, pwd: str) -> str:
        return self.pwd_context.hash(pwd)

    def verify_password(self, plain_pwd: str, hashed_pwd: str) -> bool:
        return self.pwd_context.verify(plain_pwd, hashed_pwd)


pwd_helper = PwdHelper()
