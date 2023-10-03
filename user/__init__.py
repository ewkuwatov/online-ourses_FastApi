from pydantic import BaseModel


class LoginUserModel(BaseModel):
    email: str
    password: str


class RegisterUserModel(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    password: str


class EditUserModel(BaseModel):
    name: str
    new_name: str
    new_surname: str
    new_email: str
    new_phone_number: str
    new_password: str

