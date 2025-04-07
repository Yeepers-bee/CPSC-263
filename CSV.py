import csv


def main():
    menu()
    FILENAME = "monthly_sales.csv"
    while True:
        command_occured = False
        print('')
        user_input = input("Command: ")
        if user_input == 'monthly':
            month(FILENAME)
            command_occured = True
        elif user_input == 'yearly':
            year(FILENAME)
            command_occured = True
        elif user_input == 'edit':
            edit(FILENAME)
            command_occured = True
        elif user_input == 'exit':
            print("Bye!")
            return
        elif not command_occured:
            print("ERROR! Invalid command.")

            

def month(FILENAME):
    with open(FILENAME, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0] + ' - ' + row[1])
        return


def year(FILENAME):
    with open(FILENAME, 'r', newline='') as file:
        reader = csv.reader(file)
        total = 0
        for row in reader:
            total = total + int(row[1])
        average: float = total / 12
        print("Yearly total: " + str(total))
        print("Monthly average: " + str(round(average, 2)))

def edit(FILENAME):
    month_array = get_month_array(FILENAME)
    report = read(FILENAME)
    user_input = input("Three-letter Month: ")
    found_month = user_input in month_array
    month_index = month_array.index(user_input)
    if found_month:

        user_sales_input = input("Sales Amount: ")
        report[month_index][0] = user_input
        report[month_index][1] = user_sales_input
        write(report,FILENAME)
        print("Sales amount for " + str(user_input) + " was modified.")
        return
    else:
        print("ERROR! No month found with name " + str(user_input))
        return

def read(FILENAME):
    report = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            report.append(row)
        return report

def write(report,FILENAME):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(report)
        

def get_month_array(FILENAME):
    month_array = []
    with open(FILENAME, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            month_array.append(row[0])
        return month_array

def menu():
    print("monthly - View monthly sales")
    print("yearly  - View yearly summary")
    print("edit	- Edit sales for a month")
    print("exit	- Exit program")



if __name__ == "__main__":
    main()
