import json
import os
import msvcrt

data = json.load(open('./locations.json'))

def clear():
    os.system('cls')

def await_key():
    print("\n\n\npress any key to continue...")
    msvcrt.getch()

def menu():
    clear()
    print("Options (ensure all paths are in the same disc):")
    print("\t1.\tAdd source folder")
    print("\t2.\tUpdate destination for image files")
    print("\t3.\tUpdate destination for document files")
    print("\t4.\tUpdate destination for executable files")
    print("\t5.\tUpdate destination for attachment files")
    print("\t6.\tUpdate destination for audio files")
    print("\t0.\tExit setup")

    option = int(input())
    types = ['photos', 'documents', 'executables', 'attachments', 'audio']

    if option == 1:
        add_source()
        menu()
    elif 2 <= option and option <= 6:
        update_destination(types[option-2])
        menu()
    
def add_source():
    clear()
    print("Enter new source folder to pull files from: ")
    loc = input()
    data['source'].append(loc)
    print("Successfully added path: {}".format(loc))
    await_key()
    clear()

def update_destination (type: str):
    clear()
    print("Enter new destination for {} files".format(type))
    loc = input()
    data["destination"][type] = loc
    print("Successfully updated {} path to: {}".format(type, loc))
    await_key()
    clear()


def main():
    clear()
    print("Welcome to Download Manager setup Wizard")
    await_key()
    clear()

    menu()

    with open('locations.json', 'w') as f:
        json.dump(data, f)

    clear()
    print("Setup Complete")
    await_key()
    clear()

if __name__ == '__main__':
    main()