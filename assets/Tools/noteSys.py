import pickle


def placeholder():
    return "Sorry, this tool is currently indev"


def load_notes():
    try:
        with open("notes.pkl", "rb") as file:
            notes = pickle.load(file)
    except (FileNotFoundError, EOFError):
        notes = {}
    return notes


def save_notes(notes):
    with open("assets/notes.pkl", "wb") as file:
        pickle.dump(notes, file)


def display_notes(notes):
    if not notes:
        print("No notes available.")
    else:
        print("Your Notes:")
        for index, (title, content) in enumerate(notes.items(), start=1):
            print(index, ".", title)


def add_note(notes):
    title = input("Enter the title of the note: ")
    content = input("Enter the content of the note: ")
    notes[title] = content
    save_notes(notes)
    print("Note added successfully.")


def view_note(notes):
    display_notes(notes)
    if notes:
        note_index = int(input("Enter the number of the note you want to view: "))
        note_title = list(notes.keys())[note_index - 1]
        note_content = notes[note_title]
        print("\n", note_title, ":", "\n", note_content)
    else:
        print("No notes available.")


def delete_note(notes):
    display_notes(notes)
    if notes:
        note_index = int(input("Enter the number of the note you want to delete: "))
        note_title = list(notes.keys())[note_index - 1]
        del notes[note_title]
        save_notes(notes)
        print("Note deleted successfully.")
    else:
        print("No notes available.")


def main():
    notes = load_notes()
    while True:
        print("\nOptions:")
        print("1. View Notes")
        print("2. Add Note")
        print("3. View a Note")
        print("4. Delete a Note")
        print("q. Exit")

        choice = input("Enter your choice 1/2/3/4/q: ")

        if choice == '1':
            display_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            view_note(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == 'q':
            save_notes(notes)
            break
        else:
            print("Invalid choice. Please retry")
