# Lab 4 Problem 1- exercise on using a class

class BookData:
    def __init__(self, author, title, rating):
        self._author = author
        self._title = title
        self._rating = rating

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_rating(self):
        return self._rating

    def __str__(self):
        return self._title + " - " + self._author + " - " + str(self._rating)

def process_data(filename):
    # Step 2: your code goes here
    file = open(filename)
    output = {}
    for line in file:
        temp = line.split(",")
        output[temp[0]] = BookData(temp[1], temp[0], int(temp[2]))
                                   
    file.close()
    return output

def split_with_find(string):
    return string[:string.find(":")], string[string.find(":") + 1:].strip()

def main():
    filename = input("Enter filename: ")
    
    # Step 3: call your process_data function here
    #         and print the resulting dictionary
    book_dict = process_data(filename)
    print(book_dict)
    prompt = ''
    while prompt != 'done':
        title = input("Book title: ")
        # Step 4: print the rating of the book here 
        #         or a message if not there
        if title in book_dict:
            print("Rating is " + str(book_dict[title].get_rating()))
            
        else:
            print("There is no information on that book.")
        prompt = input('Enter "done" if finished: ')
        
    print(split_with_find("F. Scott Fizgerald:  The Great Gatsby"))
    print(split_with_find("Daniel J. Solove:  The Digital Person: Technology\
 and Privacy Today"))
main()
