from temp import *
from time import sleep
import json

FILENAME = 'music_collection'
try:
    with open(f"{FILENAME}.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
except json.decoder.JSONDecodeError: #found error that is responsible for json code errors
    data = []


def add_album(filename):
    global data
    data.append({input("Author: "): {"collection": input("Collection: "), "age": int(input("Age: "))}})
    with open(f"{filename}.json", "w", encoding="UTF-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(data)


def get_collection(filename):
    global data
    try:
        with open(f"{filename}.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
            print("Music collection:")
            for album in data:
                for author, info in album.items():
                    print(f"Author: {author}, Collection: {info['collection']}, Year: {info['age']}")
    except FileNotFoundError:
        print(f"File \"{filename}.json\" not found.")


def search_album(filename):
    global data
    author_to_search = input("Enter the author's name: ")
    found = False
    try:
        with open(f"{filename}.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
            for album in data:
                for author, info in album.items():
                    if author.lower() == author_to_search.lower():
                        print(f"Author: {author}, Collection: {info['collection']}, Year: {info['age']}")
                        found = True
            if not found:
                print(f"No songs by {author_to_search} found.")
    except FileNotFoundError:
        print(f"File \"{filename}.json\" not found.")


def delete_album(filename):
    global data
    name_of_delete = input("Enter the album's name: ")
    without_album = []
    found = False
    try:
        with open(f"{filename}.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
            for album in data:
                for author, info in album.items():
                    if info["collection"].lower() == name_of_delete.lower():
                        print(f"Deleted album '{name_of_delete}' by {author}.")
                        found = True
                    else:
                        without_album.append(album)
            if found:
                data = without_album
                with open(f"{filename}.json", "w", encoding="UTF-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            else:
                print(f"Album \"{name_of_delete}\" not found.")
    except FileNotFoundError:
        print(f"File \"{filename}.json\" not found.")


def main():
    while True:
        try:
            user = int(input("Add a new album - 1\n"
                             "See the whole collection - 2\n"
                             "Search album by an artist- 3\n"
                             "Delete an album - 4\n"
                             "Exit - 5\n"))
            if user == 1:
                add_album(FILENAME)
            elif user == 2:
                get_collection(FILENAME)
            elif user == 3:
                search_album(FILENAME)
            elif user == 4:
                delete_album(FILENAME)
            elif user == 5:
                print("Exiting...")
                sleep(1)
                break
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
