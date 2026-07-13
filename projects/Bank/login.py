def login(account:int, password:int)->bool:  
    if account in users:
        if password == users[account]['password']:
            return True
        return False
    return False