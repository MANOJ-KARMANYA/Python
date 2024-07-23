def main():
    special_characters = [
        '"', "'", '\\', '{', '}', '[', ']', '(', ')', '<', '>', '&', '*', '%',
        '$', '!', '@', '#', '^', '~', '`', '|', ':', ';', ',', '.', '?', '/',
        '-', '_', '=', '+'
    ]
    
    string = input("Enter a string: ")
    
    found_special_char = False
    for char in string:
        if char in special_characters:
            found_special_char = True
            break
    
    if found_special_char:
        print("The string contains special characters.")
    else:
        print("The string does not contain any special characters.")

if __name__ == "__main__":
    main()
