def get_word_count(txt):
    count = len(txt.split())
    print(f"Found {count} total words")

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def get_character_count(txt):
    characters = set()
    character_count = {}

    for word in txt.split():
        for char in word:
            char = char.lower()
            if char in characters:
                character_count[char] += 1
            else:
                characters.add(char)
                character_count[char] = 1

    # print(character_count)
    return character_count

def sort_on(items):
    return items["num"]

def get_report(filepath):
    txt = get_book_text(filepath)
    stuff = get_character_count(txt)
    char_data = []

    for item in stuff:
        char_data.append({"char": item, "num": stuff[item]})

    char_data.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    get_word_count(txt)
    print("--------- Character Count -------")
    for data in char_data:
        print(f"{data['char']}: {data['num']}")
    print("============= END ===============")
    
