from pydantic import BaseModel, Field

class MoneyTranferModel(BaseModel):
    sender_id: str
    receiver_id: str
    amount: str

