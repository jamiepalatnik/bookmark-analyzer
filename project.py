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
            txtfile = sys.argv[1]
            newtxtfile = sys.argv[2]
            # Sort the list alphabetically
            sorted_list = abc_sort(txtfile)
            print(f"There are {len(sorted_list)} items in your list.")
            # # Ask the user if they want to remove duplicates
            sorted_list = remove_duplicates_on_request(sorted_list)
            write_to_new_file(sorted_list, newtxtfile)
            print(f"Check {newtxtfile} to review your new TXT file.")
        except ValueError:
            sys.exit("Not a TXT file")
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


def abc_sort(txtfile):
    """Sort URLs alphabetically"""
    sorted_list = []
    with open(txtfile, "r") as file:
        for line in sorted(file):
            if line.strip() != "":
                sorted_list.append(line.strip())
        return sorted_list


def remove_duplicates_on_request(txtfile):
    """Remove duplicate URLs if requested"""
    answer = input("Would you like to remove duplicate links? ")
    if answer.lower() == "y" or answer == "yes":
        seen = []
        duplicates = set()
        for i in txtfile:
            if i in seen:
                duplicates.add(i)
            else:
                seen.append(i)
        print(f"{len(txtfile) - len(seen)} duplicate links were removed.")
        print(f"There are {len(seen)} links in your updated list.")
        return seen
    else:
        return txtfile


def write_to_new_file(txtfile, newtxtfile):
    """Write TXT to file given in sys.argv[2]"""
    with open(newtxtfile, "w") as file:
        file.write("Updated TXT file\n\n")
        for line in txtfile:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
