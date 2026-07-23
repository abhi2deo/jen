print(''' 1.Withdraw
          2.Deposit
          3.Check balance''')
balance = 10000000000

ch = int(input("Choose operation: "))
if(ch==1):
    amt = int(input("Enter amount: "))
    balance -= amt
    print("Withdrawal successful")
elif(ch==2):
    amt = int(input("Enter amount: "))
    balance += amt
    print("Deposit successful")
elif(ch==3):
    print("Balance: ",balance)
else:
    print("Invalid input")