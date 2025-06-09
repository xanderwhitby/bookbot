def count_words(split_words):
    get_list = split_words.split()
    count = f"Found {len(get_list)} total words"
    return count

def count_char(split_w):
    new_split = split_w.split()
    char_count = {}
    for i in new_split:
        for index, letter in enumerate(i.lower()):
            if letter not in char_count:
                char_count.update({letter: 1})
            elif letter in char_count.keys():
                char_count[letter] += 1
                

    return char_count

def sort_dictionary(original):
    return dict(sorted(original.items(), key=lambda item: item[1], reverse=True))
    




    

        
