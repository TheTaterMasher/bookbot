def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print_report(book_text)

def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

# returns the book text as str
def get_book_text(path):
    with open(path) as f:
        return f.read()

# returns a dict for the amount of times each character appears
def get_char_dict(file_contents):
    char_count = {}
    for char in file_contents:
        lowered = char.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1          
    return char_count

def print_char_dict(file_contents):
    char_count = get_char_dict(file_contents)
    sorted_char_count = sort_dict(char_count)
    for mini_dict in sorted_char_count:
        for key in mini_dict:
            print(f"The {key} charactert was found {mini_dict[key]} times")

#takes in dict and return a sorted list of dict
def sort_dict(unsorted_dict):
    sorted_list = []
    unsorted_list = []
    for key in unsorted_dict:
        temp_dict = {key: unsorted_dict[key]}
        unsorted_list.append(temp_dict)

    for item in unsorted_list:
        for key in item:
            if not key.isalpha():
                unsorted_list.remove(item)


    for i in range(0, len(unsorted_list)):
        #find largest
        max_value = float("-inf")
        max_key = ""
        temp_mini_dict = {}

        for mini_dict in unsorted_list:
            for key in mini_dict:
                if mini_dict[key] > max_value:
                    max_value = mini_dict[key]
                    max_key = key
                    temp_mini_dict = mini_dict
        
        unsorted_list.remove(temp_mini_dict)
          
        #append largets to sorted list
        temp_dict = {max_key: max_value}
        sorted_list.append(temp_dict)

        #repeat
    return sorted_list

def sort_on():
    pass

def print_report(file_contents):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_num_words(file_contents)} words found in the document")
    print("")
    print_char_dict(file_contents)
    print("--- End report ---")

main()