"""Generate markov text from text files."""


from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open("green-eggs.txt").read()
    return contents


def make_chains(text_list):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    chains = {}
    index = 0
    text_list = text_list.split()

    while index < (len(text_list) - 2):

        for word in range(len(text_list) - 2):

            bigram = text_list[index], text_list[index + 1]

            if bigram not in chains:
                chains[bigram] = [text_list[index + 2]]
            else:
                chains[bigram].append(text_list[index + 2])

            index += 1

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    our_key = choice(chains.keys())
    our_values = chains[our_key]
    value = choice(chains[our_key])

    # pull the items out of the tuple add them as strings to words
    key1, key2 = our_key

    words.append(key1)
    words.append(key2)
    words.append(value)

    # new_key = words[1], value
    # print new_key
    # words = [our_key + value]

    print our_key
    print our_values
    print value
    print words
    print key1
    print key2
    # put the key in the container words
    # use the key to get the value from the dict
    # randomly select from value list using random.choice()
    # append that value to words
    # make new key from words[1] and the value
    # repeat


    # return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
