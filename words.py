def print_upper_words(word_list, words_must_start):
    '''Enter in words and letters,uppercases and prints word if starts with letters'''
    for word in word_list:
        if word[0] in words_must_start:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   {"h", "y"})
            