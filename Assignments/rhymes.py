"""
    File: rhymes.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: From an input file and input word, finds all rhyming words and 
    prints them alphabetically. Expects input of a valid file and word present
    in said file, otherwise throws file not found and key errors respectively.
"""

def read_file():
    """
    reads in the file from input and returns dict with phonemes per word

    Parameters:
        None

    Returns:
        dict{str:list[[str]]}: words mapped to every phoneme combination
    """
    file = open(input())
    output = {}

    for line in file:
        temp = line.split()
        word = temp[0]
        if word not in output:
            output[word] = []

        output[word].append(temp[1:])

    file.close()
    return output

def phoneme_to_match(phonemes):
    """
    takes word as phonemes and returns everything after the primary stress

    Parameters:
        word (list[str]): list of phonemes

    Returns:
        list[str]: list of phonemes after primary stress
    """
    for i in range(len(phonemes)):
        if phonemes[i][-1] == "1":
            return phonemes[i:]
        
def do_continue(phonemes, rhyme_phonemes, matches):
    """
    checks for additional conditions that invalidate rhymes

    Parameters:
        phonemes (list[str]): phonemes of current word from the file
        rhyme_phonemes (list[[str]]): all phonemes of word to rhyme with
        matches (list[[str]]): phonemes of word to rhyme with that come after
        the primary stress

    Returns:
        bool: whether rhyme is invalid
    """
    # skips if phonemes of both words are the same
    if phonemes in rhyme_phonemes:
        return True
    
    # skips if phonemes before primary stress match
    for i in range(len(rhyme_phonemes)):
        if (len(rhyme_phonemes[i]) > len(matches[i])
            and len(phonemes) > len(matches[i])
            and phonemes[-len(matches[i])-1] 
                == rhyme_phonemes[i][-len(matches[i])-1]):
            return True
        
    return False

def find_rhymes(word_dict, word):
    """
    finds and prints all rhymes of word from word_dict

    Parameters:
        word_dict (dict{str:list[[str]]}): words mapped to their phonemes
        word (str): word to match

    Returns:
        None
    """
    output, matches, rhyme_phonemes = [], [], word_dict[word]

    # converts string word to 2D list of phonemes after primary stress
    for phonemes in rhyme_phonemes:
        matches.append(phoneme_to_match(phonemes))
        
    for k, v in word_dict.items():
        for phonemes in v:
            if do_continue(phonemes, rhyme_phonemes, matches):
                continue

            for match in matches:
                # adds to list if end of phonemes are same as match
                if (len(phonemes) >= len(match)
                    and phonemes[-len(match):] == match):
                    output.append(k)

    for word in sorted(output):
        print(word)

def main():
    find_rhymes(read_file(), input().upper())
main()