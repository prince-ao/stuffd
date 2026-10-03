from fastapi import FastAPI, HTTPException
from models import CreateAccount, Transfer
import accounts

app = FastAPI()


@app.post("/accounts")
def create_account(account: CreateAccount):
    """
    body:
      initial_amount (optional, int)
    """
    if account.initial_amount:
        account_id = accounts.create(account.initial_amount)
    else:
        account_id = accounts.create()

    return {"account_id": account_id}

@app.get("/accounts/{account_id}")
def get_balance(account_id: str):
    try:
        balance = accounts.get_balance(account_id)

        return {"balance": balance}
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)

@app.post("/transfers")
def transfer_funds(transfer: Transfer):
    ...
