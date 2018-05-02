## /Users/mwirvine/galvanize/self-assessment/challenge1textfile.txt

def letter_counter(path_to_file, letters_to_count):
    counter_dict = {}
    with open(path_to_file) as f:
        text_file_string = f.read()
        for char in letters_to_count:
            counter_dict[char] = text_file_string.count(char)
    return counter_dict

letter_counter('/Users/mwirvine/galvanize/self-assessment/challenge1textfile.txt', 'aeiou')
