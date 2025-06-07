"""
    File: lab_2
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: contains three lab problems reviewing various topics
"""

def compare(file1name, file2name):
    file1, file2 = open(file1name), open(file2name)
    for line in file1:
        line2 = file2.readline()
        # breaks if no lines left
        if line2 == "":
            break
        
        if line != line2:
            print("Lines are different")
    file1.close()
    file2.close()
    
def pair_frequencies(word_list):
    output = {}
    for word in word_list:
        for i in range(len(word)-1):
            temp = word[i:i+2]
            if temp not in output:
                output[temp] = 0
            output[temp] += 1
            
    for key in output:
        print(key, ":", output[key])
    return output

def merge_dicts(d1, d2):
    output = dict(d2)
    for key in set(d1.keys()):
        if key not in output:
            output[key] = 0
        output[key] += d1[key]
    return output
        
        
if __name__ == "__main__":
    # compare()
    pair_frequencies(["banana", "bends", "i", "mend", "sandy"])
    print(merge_dicts({"t":4, "x":2, "z":5}, {"b":3, "x":1, "t":2, "c":9}))