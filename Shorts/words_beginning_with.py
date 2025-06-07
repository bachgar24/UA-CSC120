def words_beginning_with(wordlist, head):
    # your code here
    output = []
    for word in wordlist:
        if word[:len(head)] == head:
            output.append(word)
    return output