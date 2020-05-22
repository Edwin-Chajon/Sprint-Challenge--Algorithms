'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if less than 2 letters than it cant be "th", return 0
    if len(word) < 2:
        return 0
    # otherwise start counting the first and second letter from word [0] and [1] to make sure they have 't' & 'h'
    elif word[0] + word[1] == 'th':
        # return with count of one being that the instance is correct. then recurse without the first instance of th until non aplicable.
        return 1 + count_th(word[1:])
    # if no 'th' but word is longer than 2, recurse until it is less than 2 and return 0
    else:
        return count_th(word[1:])