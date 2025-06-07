def primary_stress_position(phoneme_list):
    # your code here
    for i in range(len(phoneme_list)):
        if phoneme_list[i][-1] == "1":
            return i
    return None