"""A simple program that appends a note and displays all saved notes."""

NOTES_FILE = "my_notes.txt"


def main():
    note = input("Write a note: ").strip()

    if not note:
        print("No note entered. Nothing was saved.")
        return

    # The append mode ("a") adds the new note without deleting older notes.
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")

    print("\nYour saved notes:")
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.read()
            print(notes, end="")
    except FileNotFoundError:
        print(f"{NOTES_FILE} not found.")


if __name__ == "__main__":
    main()
