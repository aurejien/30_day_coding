"""
Next update creat new db.json if doen't existe yet.

{}

"""

import json

def reader():
    path = "./db.json"
    with open(path, "r") as f:
        dict_db = json.load(f)
    return dict_db


def writer(dict_db):
    path = "./db.json"
    with open(path, "w") as f:
        json.dump(dict_db, f)


def new():
    dict_db = reader()

    try:
        id = int(list(dict_db.keys())[-1]) + 1
    except IndexError:
        id = 1

    dict_db[id] = {"Name" : 0,
                "Mail" : 0,
                "Tel": 0,
                "Bday": 0
                }

    for i in dict_db[id]:
        choice = input(f"{i}: -> ").lower()
        dict_db[id][i] = choice

    writer(dict_db)
    

def show():
    """
    Show the list of contact form db.json
    """
    dict_db = reader()

    for key, value in dict_db.items():
        print(f"id: {key}")
        for i, j in value.items():
            print(f"\t{i}: {j}")


def delete():
    """
    delete conctat inside db.json and give it to modif() as f_values
    """
    dict_db = reader()

    vvar = False
    text = "Choose's contact by name, tel, mail, id...."
    choice = input(f"{text}\n-> ")

    for f_keys, f_values in dict_db.items():
        if choice in f_values.values():
            vvar = True
            a = f_keys

    if vvar:
        del dict_db[a]
        writer(dict_db)
        print(f"User {choice} was deleted successfully....")
    else:
        print(f"{choice} not found....")


def menu():
    print("-"*15, "\nM E N U")
    liste_menu = {
        "1": ["New", new],
        "2": ["Show", show],
        "3": ["Delete", delete],
        "q": ["Exit", 0]
    }

    for i, j in liste_menu.items():
        if i.isdigit():
            print(f"  [{i}] {j[0]} Contact")
        else:
            print(f"  [{i}] {j[0]}")

    choice = input("-> ").lower()

    if choice == "q":
        print("Goodbye.")
    elif choice in liste_menu:
        liste_menu[choice][1]()
        menu()
    else:
        print(f"{choice} not able: Value Error")
        menu()
        
    


print("-"*15, "\nW E L C O M E" )
menu()