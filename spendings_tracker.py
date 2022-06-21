while True:
    print ()
    month = int(input ("Choose a month (1-12): "))

    if month < 1:
        break

    if month > 12:
        break

    while True:
        print ()
        print ("Choose option: ")
        print ("0 - Return to the selection of the month")
        print ("1 - Show all spendings")
        print ("2 - Add a new expense")

    