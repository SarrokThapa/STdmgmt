import tempfile
from pathlib import Path

from src.config import settings
from src.services.student_service import StudentService


def test_add_and_delete(tmp_path: Path):
    # point the settings to a temporary file for testing
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    students_file = data_dir / "students.json"

    # create an empty students file
    students_file.write_text("[]")

    # monkeypatch the settings to use this path
    settings.STUDENTS_FILE = students_file

    svc = StudentService()

    s = svc.add_student("Alice", 20, "F", "A")
    assert s.name == "Alice"

    all_students = svc.list_students()
    assert any(st.id == s.id for st in all_students)

    deleted = svc.delete_student(s.id)
    assert deleted is True

    assert svc.list_students() == []
