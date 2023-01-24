#Harrison Wendt
#30353351
#Created: 11/28/2022
#Last modified: 11/28/2022
#driver.py
from executive import Executive
def main():
    file_name = input("Enter file name: ")
    print()
    my_executive = Executive(file_name)
    my_executive.file_input()
    my_executive.run()

main()