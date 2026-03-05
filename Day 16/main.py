
from prettytable import PrettyTable


def print_table():
    table = PrettyTable()


    table.field_names = ["Pokemon name", "Type"]
    table.add_row(["Pikachu", "Electric"])
    table.add_row(["Squirtle","Water"])
    table.add_row(["Charmander", "Fire"])

    print(table)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_table()






