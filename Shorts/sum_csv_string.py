def sum_csv_string(csv_string):
    # your code here
    output = 0
    for str_num in csv_string.split(","):
        output += int(str_num)
    return output
