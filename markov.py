"""Generate markov text from text files."""


from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open("GoT.txt").read()
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

    # get first key by choosing from keys in dict
    our_key = choice(chains.keys())

    while our_key != ('horrors', 'beyond.'):
        # randomly select from value list using choice()
        value = choice(chains[our_key])
        #unpack key tuple into 2 values
        key1, key2 = our_key
        # make new key from key2 and the value
        our_key = (key2, value)
        # append key and value to words
        words.append(key1)
        words.append(key2)
        words.append(value)

    return " ".join(words)


input_path = "GoT.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
