# Notes 

#### Video Demo:  <URL HERE>
#### Description:

This program is a simple command-line application for taking notes and organizing them. It allows users to perform various operations on their notes, such as creating a note, viewing all notes, viewing a single note, editing a note, and deleting a note. The application utilizes a SQLite database to store and manage the notes.

## Project Files

This project consists of several files that serve different purposes. Here's a description of each file:

### project.py

The `project.py` file is the main program file of the project. It contains the implementation of the notes application. When executed, it presents a command-line interface to the user and allows them to create, view, edit, and delete notes. The program utilizes a SQLite database to store and manage the notes. It also includes the necessary functions and classes to handle user input, display messages, and interact with the database.

### test_project.py

The `test_project.py` file is a test file for the `project.py` program. It contains unit tests that verify the correctness of the functions and methods implemented in the main program file. These tests help ensure that the program behaves as expected and that any changes or updates to the code do not introduce errors or regressions. Running the `test_project.py` file executes the test cases and provides feedback on whether the program functions as intended.

### requirements.txt

The `requirements.txt` file is a text file that lists the required libraries and their versions for running the project. It is commonly used in Python projects to document the dependencies needed to run the program. Each library is listed on a separate line, and the version, if specified, is included after the library name and separated by the `==` symbol. This file helps ensure that the necessary libraries are installed in the correct versions for the project to work correctly.

### README.md

The `README.md` file is a Markdown file that provides documentation and information about the project. It serves as a guide for users and developers, explaining the purpose of the project, how to install and use it, and any other relevant details. The README file includes an overview of the project, instructions for installation, usage examples, descriptions of files and directories, acknowledgments, and any other information deemed necessary to understand and use the project effectively. It is a standard practice to include a README file in software projects to provide essential information and improve project discoverability and collaboration.

These files collectively form the project and facilitate its development, testing, and usage.


## Requirements
- Python 3.x
- pyfiglet library
- tabulate library
- sqlite3 library

## Installation
1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries by running the following command:
   ```
   pip install pyfiglet tabulate
   ```
3. Clone or download the source code from the repository.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory where the program files are located.
3. Run the following command to start the application:
   ```
   python notes.py
   ```
4. The program will display a menu with the available options.
5. Enter the corresponding number for the operation you want to perform.
6. Follow the prompts to enter the required information for each operation.

## Functionality
1. **Create a note**: This option allows you to create a new note by entering a title and a description for the note.

2. **View all notes**: This option displays a table showing all the existing notes, including their IDs, titles, and descriptions.

3. **View a single note**: With this option, you can view the details of a specific note by entering its ID.

4. **Edit a note**: This option enables you to edit the title and/or description of an existing note. You need to provide the ID of the note you want to edit and then enter the new title and/or description. Leaving a field blank will keep the current value.

5. **Delete a note**: This option allows you to delete a note by providing its ID. You will be prompted for confirmation before the deletion is performed.

6. **Exit**: Choosing this option terminates the program.

## Acknowledgements
This program uses the following libraries:

- [pyfiglet](https://github.com/pwaller/pyfiglet): A Python library for creating ASCII art text from plain text.

- [tabulate](https://github.com/astanin/python-tabulate): A Python library for creating tables from tabular data.

## Database
The program utilizes a SQLite database named `notes.db` to store the notes. The database has a single table called `notes` with the following structure:

```
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL
)
```

The table has three columns:
- `id`: An auto-incrementing integer that serves as the unique identifier for each note.
- `title`: The title of the note.
- `description`: The description or body of the note.

Additionally, the program creates a trigger named `reset_id` to reset the auto-incrementing ID counter to 0 after a note is deleted:

```
CREATE TRIGGER IF NOT EXISTS reset_id
    AFTER DELETE ON notes
    FOR EACH ROW
    BEGIN
        UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'notes';
    END
```

## Note
This program was developed as part of the CS50 Projects. It provides a basic functionality for taking and managing notes. Feel free to modify and enhance it to suit your needs.

And say: "This is CS50"
```
