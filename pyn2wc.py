import os
import sys
from utils import load_pynum2words_dictionary, is_valid_n2w_file, is_folder
from colorama import init, Fore

init(autoreset=True)

def main():
    if len(sys.argv) != 2:
        print(Fore.BLUE + "Usage: python pyn2wc.py <path to the n2w dictionary file> or the folder containing dictionary files")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        if is_valid_n2w_file(file_path):
            number_to_word, word_to_number, is_valid_dictionary_file = load_pynum2words_dictionary(file_path)
            if is_valid_dictionary_file:
                print(Fore.GREEN + f"{os.path.basename(file_path)} passed the checks.")
                print(Fore.GREEN + f"{os.path.basename(file_path)} Is ready to use.")
        elif is_folder(file_path):
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    full_path = os.path.join(root, file)
                    if is_valid_n2w_file(full_path):
                        number_to_word, word_to_number, is_valid_dictionary_file = load_pynum2words_dictionary(full_path)
                        if is_valid_dictionary_file:
                            print(Fore.GREEN + f"{os.path.basename(full_path)} passed the checks.")
                            print(Fore.GREEN + f"{os.path.basename(full_path)} Is ready to use.")
                    else:
                        print(Fore.RED + f"File '{full_path}' isn't a valid pynum2words dictionary file.")
        else:
            print(Fore.RED + f"File '{file_path}' isn't a valid pynum2words dictionary file.")
            sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"Unable to check dictionary file '{file_path}': due to{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()