
# user table
users = {
    1234:{'name':"Priya", "Email":'priyapittala12@gmail.com', 'balance':5000, 'password':'1234'},
    1235:{'name':"Priya", "Email":'priyapittala054@gmail.com', 'balance':10000, 'password':'1235'}
}



#services
def registers(name:str, email:str,initial_deposite:int, password:str):
    pass

def login(account:int, password:int)->bool:  
    if account in users:
        if password == users[account]['password']:
            return True
        return False
    return False


#balance function defination
def balance(account:int)->int:
    curr_amount = users[account]['balance']
    return curr_amount

#withdraw function defination
def withdraw(account:int, withdraw_amount:int)->str:
    curr_amount = users[account]['balance']
    #check amount
    if curr_amount >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} withdraw successful and current balance is {users[account]['balance']}"
    return "Insufficient Balance"

#Deposite Function Defination
def deposite(account:int, deposite_amount:int):
    users[account]['balance'] += deposite_amount
    return f"{deposite_amount} deposite successful and current balance is{users[account]['balance']}"

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

#Ministatement Function Defination
def ministatement(account:int):
    return "ministatement under development process"

# logout function defination
def logout():
    return "Thank you using small scale bank service, Bye Bye..."


# main
if __name__=="__main__":

    print("welcome to the small scale bank")
    print("1. Register \n 2.Login")
    choice = int(input("select your choice:"))
    
    # calling register function
    if choice == 1:
        print("Register page under development process....")

    # calling Login Function
    elif choice == 2:
        account = int(input("Enter your account number:"))
        password = input("Enter your password:")
        login_val = login(account=account, password=password)

        while True:
            print("The small scale Bank providing services")
            print("1. Balance \n 2. Withdraw \n 3. Deposite \n\
                   4. Transfer \n 5. Ministatement \n 6. Logout")
            choice = int(input("Enter your choice(1-6):"))

            if choice == 1:
                # call Balance function
                current_balance = balance(account=account)
                print(f"Current Balance is:{current_balance}")

            elif choice == 2:
                amount = int(input("Enter your withdraw amount:"))
                # call withdraw function
                res = withdraw(account=account, withdraw_amount=amount)
                print(res)
            elif choice == 3:
                amount = int(input("Enter your deposite amount"))
                # call deposite function
                res = deposite(account=account, deposite_amount=amount)
                print(res)
            elif choice == 4:
                receiver_account = int(input("Enter the Recevier account number"))
                amount = int(input("Enter your Transfer amount:"))
                # call transfer function function
                res = transfer(sender=account, receiver=receiver_account, transfer_amount=amount)
                print(res)
            elif choice == 5:
                # call ministatement
                #amount = int(input("Enter your deposite amount"))
                res = ministatement(account=account)
                print(res)
            elif choice == 6:
                #call logout function
                print(logout())
                exit()
            else:
                print("Invalid choice, select option in between 1 to 6")
        print("Invalid login credentials")
    else:
        print("invalid choice, select option between 1 to 2")