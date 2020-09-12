'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) <= 1:
        return 0
    # check if word has 'th' in it
    if word.find("th") == -1:
        return 0
    else:
        # if the word does have 'th' in it then get the index where it is found
        index = word.find("th")
        # set count to 1 + what the function returns
        # start word at index + 2 / to start at the letter after 'h'
        th_count = 1 + count_th(word[index + 2:])

        return th_count
