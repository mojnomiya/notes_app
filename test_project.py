import sqlite3
import pytest
from project import create_note, view_notes, delete_note


@pytest.fixture
def test_database(tmp_path):
    db_file = tmp_path / "test_notes.db"
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT NOT NULL
                    )"""
    )
    yield connection
    connection.close()


def test_create_note(test_database):
    note = create_note()
    assert note is not None


def test_view_notes(test_database, capsys):
    view_notes()
    captured = capsys.readouterr()
    assert "1" in captured.out


def test_delete_note(test_database):
    delete_note()
    cursor = test_database.cursor()
    cursor.execute("SELECT COUNT(*) FROM notes")
    assert cursor.fetchone()[0] == 0
