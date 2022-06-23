while True:
    print ()
    month = int(input ("Choose a month (1-12): "))

    if month < 1:
        break

    if month > 12:
        break

    expenses = []

    def show_expenses (month):
        for expense_amount, expense_type, expense_month in expenses:
            if expense_month == month:
                print (f'{expense_amount} - {expense_type}')

    def add_expense(month):
        print ()
        expense_amount = int(input("Give an amout [$]: "))
        expense_type = input ("Give a type of expense [food, entertainment, home, other]: ")

        expense = (expense_amount, expense_type, month)
        expenses.append(expense)

    def show_stats(month):
        
        total_amount_this_month = sum(expense_amount for expense_amount, expense_month in expenses if expense_month == month)
        total_amount_all_months = sum(expense_amount for expense_amount in expenses)
        

        print ()
        print("Stats")
        print ("All spendings in this month [$]: ", total_amount_this_month)
        print ("All spendings [$]: ", total_amount_all_months)

    while True:
        print ()
        print ("Available options: ")
        print ("0 - Return to the selection of the month")
        print ("1 - Show all spendings")
        print ("2 - Add a new expense")
        print ("3 - Stats")

        choice = int(input("Choose option: "))

        if choice == 0:
            break
        if choice == 1:
            show_expenses(month)
        if choice == 2:
            add_expense(month)
        if choice == 3:
            show_stats(month)
        else:
            break

    