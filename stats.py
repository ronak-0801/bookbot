def extract_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content


def count_words(path):
    file_content = extract_text(path)
    words = file_content.split()
    return len(words)

def count_character(path):
    file_content = extract_text(path)
    characters = {}
    for c in file_content:
        char = c.lower()
        if not char.isalpha():
            continue
        characters[char] = characters.get(char, 0) + 1

    return characters


def sort_num(items):
    return items["num"]

def sort_list_of_dict(path):
    char_count = count_character(path)
    ld = []
    for key, value in char_count.items():
        d = {"char": key, "num": value}
        ld.append(d)
    ld.sort(reverse=True, key=sort_num)
    
    return ld