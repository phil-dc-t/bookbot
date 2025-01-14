def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)

path_to_file = "books/frankenstein.txt"
main(path_to_file)
