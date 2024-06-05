from pydantic import BaseModel, Field

class User(BaseModel):
    user_id: str = Field(alias="user_id", max_length=2000, min_length=6)
    name: str
    current_balance: str


class UserIdModel(BaseModel):
    user_id: str = Field(alias="user_id", max_length=2000, min_length=6)
