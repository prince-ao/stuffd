from pydantic import BaseModel

class CreateAccount(BaseModel):
    initial_amount: float | None = None

class Transfer(BaseModel):
    idempotency_key: str
    from_account_id: str
    to_account_id: str
    amount: float
