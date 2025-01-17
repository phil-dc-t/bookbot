# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def count_chars_dict(listofwords):
    counted_chars = {}

    for word in listofwords.lower():
        for char in word:
            if char in counted_chars:
                counted_chars[char] += 1
            else:
                counted_chars[char] = 1

    #print(counted_chars)
    return counted_chars

def make_sorted_dict(temp_dict):
    # first make a list of dictionaries that contains only chars using isalpha()
    # second sort the list using .sort
    list_of_dicts = []

    #first:
    for x in temp_dict:
        if x.isalpha():
            #print(f"adding {x}")
            list_of_dicts.append({"char":x, "num":temp_dict[x]})

    # second
    #print(f"clean list, only aplha: {list_of_dicts}")
    list_of_dicts.sort(reverse=True, key=sort_on)
    #print(list_of_dicts)
    for item in list_of_dicts:
        print(f"The '{item["char"]}' character was found {item["num"]} times")

def main(path_to_file):
    #allchars = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    #print(type(allchars))
    with open(path_to_file) as f:
        file_contents = f.read()
    #print(file_contents)
    #words_in_book = file_contents.split()
    #whole_string = (" ".join(words_in_book)).lower()

    first_dict = count_chars_dict(file_contents)
    #print(first_dict)
    make_sorted_dict(first_dict)

    #print(sorted_dict)
    

path_to_file = "books/frankenstein.txt"
main(path_to_file)
