#Deposite Function Defination
def deposite(account:int, deposite_amount:int):
    users[account]['balance'] += deposite_amount
    return f"{deposite_amount} deposite successful and current balance is{users[account]['balance']}"
