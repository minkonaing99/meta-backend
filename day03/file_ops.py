def read_file(file_name):
    """ Reads and returns the entire contents of a file as a single string. """
    with open(file_name, "r") as file:
        contents = file.read()
    print(contents)
    return contents


def read_file_into_list(file_name):
    """ Reads a file and returns a list where each element is a line in the file. """
    file_content = []
    with open(file_name, "r") as file:
        for line in file:
            file_content.append(line)
    return file_content


def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a given string to an output file. """
    first_line = file_contents.split("\n")[0]
    with open(output_filename, "w") as file:
        file.write(first_line)


def read_even_numbered_lines(file_name):
    """ Reads even-numbered lines of a file and returns them as a list. """
    even_lines = []
    with open(file_name, "r") as file:
        for index, line in enumerate(file, start=1):
            if index % 2 == 0:
                even_lines.append(line)
    return even_lines


def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of its lines in reverse order. """
    with open(file_name, "r") as file:
        lines = file.readlines()
    reversed_lines = lines[::-1]
    print(reversed_lines)
    return reversed_lines


# Sample commands to run/test your implementations.
def main():
    file_contents = read_file("sampletext.txt")
    print("File Contents:\n", file_contents)
    
    # print(read_file_into_list("sampletext.txt"))
    # write_first_line_to_file(file_contents, "output.txt")
    # print(read_even_numbered_lines("sampletext.txt"))
    # print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
