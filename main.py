def sort_on(dict):
    return dict["count"]

def character_count(book_text):
    dict_char = {}
    for letter in book_text:
        lowered = letter.lower()
        if lowered.isalpha():
            if lowered in dict_char:
                dict_char[lowered] = dict_char[lowered] + 1
            else:
                dict_char[lowered] = 1
    dict_to_arr = []
    for k, v in dict_char.items():
        new = {"char": k, "count": v}
        dict_to_arr.append(new)
    dict_to_arr.sort(reverse=True, key=sort_on)
    return dict_to_arr

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    print("--- Begin report of " + book_path + " ---")
    word_count = len(file_contents.split())
    print(str(word_count) + " words found in the document")
    char_count = character_count(file_contents)
    for entry in char_count:
        print("The " + entry["char"] + " character was found " + str(entry["count"]) + " times")

main()