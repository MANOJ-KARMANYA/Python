def add_menu_item(menu_dict):
    item_name = input("Enter new menu item: ")
    item_description = input("Enter item description: ")
    menu_dict[item_name] = item_description
    print("Item added successfully.")
    return menu_dict

def display_menu(menu_dict):
    print("______________ Menu ______________ ")
    for item_name, item_description in menu_dict.items():
        print(f"{item_name}: {item_description}")
    print("________________________________")

def update_menu_item(menu_dict):
    item_to_update = input("Enter menu item to update: ")
    if item_to_update in menu_dict:
        new_description = input("Enter updated description: ")
        menu_dict[item_to_update] = new_description
        print("Menu item updated successfully.")
    else:
        print("Menu item not found.")

def remove_menu_item(menu_dict):
    item_to_remove = input("Enter menu item to remove: ")
    if item_to_remove in menu_dict:
        del menu_dict[item_to_remove]
        print("Menu item removed successfully.")
    else:
        print("Menu item not found in the menu.")

def main():
    menu = {
        'starter1': 'Description of starter1',
        'starter2': 'Description of starter2',
        'starter3': 'Description of starter3'
    }

    while True:
        print("\n1. Display Menu")
        print("2. Add Menu Item")
        print("3. Update Menu Item")
        print("4. Remove Menu Item")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_menu(menu)
        elif choice == '2':
            menu = add_menu_item(menu)
        elif choice == '3':
            update_menu_item(menu)
        elif choice == '4':
            remove_menu_item(menu)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
