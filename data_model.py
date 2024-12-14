from pydantic import BaseModel


class Phish(BaseModel):
    Email_Text : str
    