def main(path_to_file):
    #allchars = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    #print(type(allchars))
    with open(path_to_file) as f:
        file_contents = f.read()
    #print(file_contents)
    #words_in_book = file_contents.split()
    #whole_string = (" ".join(words_in_book)).lower()
    counted_chars = {}
    #print(words_in_book)
    #print(whole_string)
    for word in file_contents.lower():
        for char in word:
            if char in counted_chars:
                counted_chars[char] += 1
            else:
                counted_chars[char] = 1

    print(counted_chars)

path_to_file = "books/frankenstein.txt"
main(path_to_file)
