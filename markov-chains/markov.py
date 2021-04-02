"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path).read()

    return file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    # Appending None to the list to set a stop point for loop in make_text function
    words.append(None)

    length = len(words)
    
    for index in range(length-2): 
        chains_key = (words[index],words[index+1])
        chains_value = words[index+2]
        print(chains_key, chains_value)

        """Checking if the key is in the dictionary. initialize that list and put your word into it. If the key is already in the dictionary, append your word to the list that’s already there."""
        if chains_key not in chains:
            chains[chains_key] = []

        chains[chains_key].append(chains_value)
    
    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    """Create new key out of the second word in the first key 
    and random word you pulled out from the list of words that followed it"""
    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    #Loop throught the list  - stop point is a word "None"(end of our original text)
    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])


    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
