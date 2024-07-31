def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_name = f.name
        word_count = len(file_contents.split())
        counts = get_character_counts(file_contents)

        print(f"--- Begin report of {file_name} ---")
        print(f"{word_count} words found in the document")
        for c in counts:
            print(f"The '{c}' character was found {counts[c]} times")
        print("--- End report ---")

def get_character_counts(text):
    char_dict = {}
    all_words = text.split()
    for word in all_words:
        char_range = range(len(word))
        for i in char_range:
            c = word[i].lower()
            if c.isalpha() == False:
                continue
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
    sorted_dict = { k: v for k, v in sorted(char_dict.items(), key=lambda item: item[1], reverse=True) }
    return sorted_dict

main()
