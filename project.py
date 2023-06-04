from pyfiglet import Figlet
from tabulate import tabulate
import sqlite3

conn = sqlite3.connect("notes.db")
cur = conn.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL
            )"""
)

cur.execute(
    """CREATE TRIGGER IF NOT EXISTS reset_id
                AFTER DELETE ON notes
                FOR EACH ROW
                BEGIN
                    UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'notes';
                END
            """
)


class Message:
    def __init__(self) -> None:
        print("\nTake Notes And Organize Yourself")
        print("1. Create a note")
        print("2. View all notes")
        print("3. View a single note")
        print("4. Edit a note")
        print("5. Delete a note")
        print("6. Exit")


def header():
    f = Figlet(font="slant")
    print(f.renderText("Notes"))
    print(f.renderText("A CS50 Projects"))
    print("=" * 80)


def create_note():
    title = input("Enter the note title: ")
    body = input("Enter the note body: ")
    cur.execute("INSERT INTO notes (title, description) VALUES (?, ?)", (title, body))
    conn.commit()
    note_id = cur.lastrowid
    cur.execute("SELECT * FROM notes WHERE id=?", (note_id,))
    note = cur.fetchone()
    print("Note added successfully!")
    return note


def view_notes():
    cur.execute("SELECT * FROM notes")
    notes = cur.fetchall()

    headers = ["ID", "Title", "Body"]
    print(tabulate(notes, headers=headers, tablefmt="heavy_grid"))


def view_single_note():
    note_id = input("Enter the ID of the note you want to view: ")

    cur.execute("SELECT * FROM notes WHERE id=?", (note_id,))
    note = cur.fetchone()
    if not note:
        print("Note not found.")
        return

    headers = ["ID", "Title", "Body"]
    print(tabulate([note], headers=headers, tablefmt="grid"))


def edit_note():
    note_id = input("Enter the ID of the note you want to edit: ")

    cur.execute("SELECT * FROM notes WHERE id=?", (note_id,))
    note = cur.fetchone()
    if not note:
        print("Note not found.")
        return

    new_title = input("Enter the new title (leave blank to keep the current title): ")
    new_body = input("Enter the new body (leave blank to keep the current body): ")
    if new_title or new_body:
        if not new_title:
            new_title = note[1]
        if not new_body:
            new_body = note[2]
        cur.execute(
            "UPDATE notes SET title=?, description=? WHERE id=?",
            (new_title, new_body, note_id),
        )
        conn.commit()
        print("Note updated successfully!")
    else:
        print("Nothing to update.")


def delete_note():
    note_id = input("Enter the ID of the note you want to delete: ")

    cur.execute("SELECT * FROM notes WHERE id=?", (note_id,))
    note = cur.fetchone()
    if not note:
        print("Note not found.")
        return

    confirm = input("Are you sure you want to delete this note? (Y/N): ")
    if confirm.upper() == "Y":
        cur.execute("DELETE FROM notes WHERE id=?", (note_id,))
        conn.commit()
        print("Note deleted successfully!")
    else:
        print("Deletion canceled.")


def main():
    header()
    while True:
        msg = Message()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            view_single_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
