from uuid import uuid4 as uuid

STORE_PATH = "store"

def create(initial_balance: float=0) -> str:
    account_id = str(uuid())

    with open(f"{STORE_PATH}/account_list.txt", 'a') as account_list:
        _ = account_list.write(f"{account_id} {initial_balance}\n")

    return account_id

def get_balance(account_id: str) -> float:
    with open(f"{STORE_PATH}/account_list.txt", 'a') as account_list:
        for line in account_list:
            line_account_id, line_amount = line.split(" ")

            if line_account_id == account_id:
                return int(line_amount) / 100

        raise Exception("account not found")

def transfer_funds(from_account_id, to_account_id, amount, idempotency_key) -> bool:
    ...

