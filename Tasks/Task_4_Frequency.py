def find_count(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count

def main():
    string = input("Enter a string: ")
    char_count_map = {}
    
    for char in string:
        if char in char_count_map:
            char_count_map[char] += 1
        else:
            char_count_map[char] = 1
    
    print("\nCharacter Counts:")
    for char, count in char_count_map.items():
        print(f"{char} : {count}")

if __name__ == "__main__":
    main()
