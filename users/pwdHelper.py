from passlib.context import CryptContext


class PwdHelper:
    def __init__(self):
        self.pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")

    def hash_password(self, pwd: str) -> str:
        return self.pwd_context.hash(pwd)

    def verify_password(self, plain_pwd: str, hashed_pwd: str) -> bool:
        return self.pwd_context.verify(plain_pwd, hashed_pwd)


pwd_helper = PwdHelper()
