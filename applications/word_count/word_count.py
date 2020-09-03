def word_count(s):
    # store the words here
    counts = {}

    # remove any special characters
    ignored_chars = {'"': None, ':': None, ';': None, ',': None, '.': None, '-': None, '+': None, '=': None, '/': None, '\\': None, '|': None, '[': None, ']': None, '{': None, '}': None, '(': None, ')': None, '*': None, '^': None, '&': None, }

    # for each letter in the string
    for char in s:
        # if it's an ignored character
        if char in ignored_chars:
            # remove it
            s = s.replace(char, '')
    
    # make all letters lowercase and separate into a list at spaces
    wordList = s.lower().split()

    # for each word...
    for word in wordList:
        # check if we already have it in counts, if so add one
        if word in counts:
            counts[word] += 1
        # if not, set it equal to one
        else:
            counts[word] = 1
    # return the final counts dictionary
    return counts

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))