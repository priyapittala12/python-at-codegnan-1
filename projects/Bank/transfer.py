#Transfer Function Defination
def transfer(sender:int, receiver:int, transfer_amount:int):
    if receiver in users:
        curr_amount = users[sender]['balance']
        if curr_amount >= transfer_amount:
            users[sender]['balance'] -= transfer_amount
            users[receiver]['balance'] += transfer_amount
            return f"{transfer_amount} transfer sucessgul and current balance is{users[sender]['balance']}"
            return "Insufficient balance"
        return "Receiver account not found"
