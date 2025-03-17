import cowsay
import sys

def main():
    cowsay.cow("Welcome to Bookmark Analyzer!")

    # Check for usage errors
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            if not sys.argv[1].endswith(".txt"):
                raise ValueError
            input = sys.argv[1]
            output = sys.argv[2]
            sorted_list = abc_sort(input)
            print(f"There are {len(sorted_list)} items in your list.")
            write_to_new_file(sorted_list, output)
            print(f"Check {output} to review your new TXT file.")
        except ValueError:
            sys.exit("Not a TXT file")
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

def abc_sort(input):
    """Sort URLs alphabetically"""
    sorted_list = []
    with open(input, "r") as file:
        for line in sorted(file):
            if line.strip() != "":
                sorted_list.append(line.strip())
        return sorted_list

def remove_duplicates(input):
    """Remove duplicate URLs"""
    ...


def write_to_new_file(input, output):
    """Write TXT to file given in sys.argv[2]"""
    with open(output, "w") as file:
        file.write(f"Updated TXT file\n\n")
        for line in input:
            file.write(line + "\n")


if __name__ == "__main__":
    main()