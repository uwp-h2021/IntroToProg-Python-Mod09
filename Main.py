# ------------------------------------------------------------------------- #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# HJong, 6/5/2021,Created new script
# HJong, 6/5/2021, Added import modules
# HJong, 6/6/2021, Added main body of script
# HJong, 6/6/2021, Added exception handling of user choice of option
# ------------------------------------------------------------------------- #

if __name__ == "__main__":
    from DataClasses import Employee as Emp     # Import Employee class
    from ProcessingClasses import FileProcessor as Fp   # Import FileProcessor class
    from IOClasses import EmployeeIO as Eio     # Import EmployeeIO class
else:
    raise Exception('This file was not created to be imported')

# Variables --------------------------------------------------------------- #
strFileName = "EmployeeData.txt"    # Name of Employee Data File
lstTable = []       # List of employee objects
choice = None       # User input of choice of option
employee = None     # Employee object

# Main Body of Script  ---------------------------------------------------- #

lstFileData = Fp.read_data_from_file(strFileName)   # Load data from file into a list of strings
lstTable.clear()
for row in lstFileData:     # Convert the list of strings into list of objects
    lstTable.append(Emp(row[0], row[1], row[2].strip()))

while True:
    try:
        Eio.print_menu_items()      # Print menu of options for user to choose from
        choice = Eio.input_menu_options()   # Receive user choice of option
        if choice == '1':
            Eio.print_current_list_items(lstTable)  # Show current list of employee objects
        elif choice == '2':
            employee = Eio.input_employee_data()
            lstTable.append(employee)   # Add data into the list of employee objects
        elif choice == '3':
            Fp.save_data_to_file(strFileName, lstTable)     # Save data to file
        elif choice == '4':     # Exit program
            print('Good Bye!')
            break
        else:
            raise Exception('Alert!  Please enter between [1-4]!')  # Raise exception for out of range user choice
    except Exception as error:
        print(error)    # Print exception to user and ask for acceptable choice of option
# Main Body of Script  ---------------------------------------------------- #
