import argparse
import requests
import multiprocessing

# Creating the argument parser
parser = argparse.ArgumentParser(description="Discovers directories on a URL using a provided wordlist.")
parser.add_argument('-w', '--wordlist', type=str, required=True, help="Path to the wordlist file")
parser.add_argument('-u', '--url', type=str, required=True, help="URL to discover directories")

# Parse the arguments provided by the user
args = parser.parse_args()

# Variables from the arguments
wordlist = args.wordlist
url = args.url

# Manager to handle shared memory for 'direc'
manager = multiprocessing.Manager()
direc = manager.list()  # This is a shared list across processes

# Read the wordlist file
try:
    with open(wordlist, "r") as file:
        text = file.read()
        print(f"Wordlist file '{wordlist}' read successfully.")
except FileNotFoundError:
    print(f"Error: The file '{wordlist}' was not found.")
    exit(1)  

# Function to print in blue
def print_blue(text):
    print(f"\033[94m{text}\033[0m")

# Function to print in red
def print_red(text):
    print(f"\033[91m{text}\033[0m")

# Function to check directories
def check_directory(line):
    target_url = f"{url}/{line}"
    try:
        response = requests.get(target_url)  
        if response.status_code == 200:
            print_blue(f"/{line} - Found!")
            direc.append(line)  # Appending the found directory to the shared list
        else:
            print_red(f"/{line} - Not found.")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Create a pool of workers (processes) to speed up the directory checking
if __name__ == '__main__':
    # Use multiprocessing to process the directories in parallel
    with multiprocessing.Pool(processes=100) as pool:
        pool.map(check_directory, text.splitlines())

    # Print the found directories
    print("\nFound directories:")
    for lines in direc:
        print_blue(lines)
