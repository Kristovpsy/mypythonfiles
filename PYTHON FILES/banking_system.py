acc_name = {
    "name": "Chris Akigbogun",
    "balance": 0.0,
    "pin": "1303"
}

print('welcome to access bank')

pin = input('enter your pin: ')

if pin != acc_name['pin']:
    print('incorrect pin, access denied')

else:
    print("welcome {acc_name['name']}")

    while True:

        print("\n---Menu---")
        print("1. check balance")
        print("2. Deposit money")
        print("3.Withdraw")
        
        print("4.airtime/data")
        print("5.Loan")
        print("6.exit")
        choice = input("choose an option 1-6")

        if choice == "1":
            print(f"your current balance is {acc_name['balance']:.2f}")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit here"))
                acc_name['balance'] += amount
                print(f"Deposit successful. New balance: {acc_name['balance']:.2f}")
            except ValueError:
                print("Invalid amount entered. Please enter a numeric value.")

        elif choice == "3":
            try:
                amount =  float(input("Enter amount to Withdraw"))

                if amount <= 0:
                    print("invalid amount .")
                elif amount > acc_name["balance"]:
                    print("insuffecient funds")
                else:

                    acc_name["balance"] -= amount
                    print(f"Withdrawal Succesful! New Balance:{acc_name['balance']:.2f}")       
            except ValueError:
                print("invalid input. enter a no")

        

        elif choice == "4":
            print("1. airtime")
        
            print("2. Data")
        elif choice == "5":
            print("1. Personal Loan")
            print("2. Home Loan")
            print("3. Car Loan")
            loan_choice = input("Choose a loan option (1-3): ")
            if loan_choice == "1":
                print("You have selected a Personal Loan.")
            elif loan_choice == "2":
                print("You have selected a Home Loan.")
            elif loan_choice == "3":
                print("You have selected a Car Loan.")
            else:
                print("Invalid loan option.")

        elif choice == "6":
            print("Thank You For Using Our ServIces. Goodbye")
            break
        
        else:
            print("invalid choice")
 