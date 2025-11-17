
## What it is:
A basic introduction and instruction guide for the project.

## What it does:

Explains how to run the program

Shows how to set up a virtual environment

Provides commands to run the CLI and tests

### Why we use it:
So anyone opening the project knows exactly how to start and use it.

## requirements.txt

### What it is:
A list of Python packages needed for the project.

### What it does:

Contains dependencies such as pytest (for testing)

### Why we use it:
So others can install the exact packages using:

pip install -r requirements.txt

## data/students.json

### What it is:
A JSON file where all the student data is stored.

### What it does:

Acts as a small local database

Saves the list of students in JSON format

### Why we use it:
To persist student data even after the program exits.

## src/init.py

### What it is:
An empty file marking the src folder as a Python package.

### What it does:
Lets Python import files inside the src directory.

### Why we use it:
This is required for proper module importing (e.g., from src.models.student import Student).

##  src/config/settings.py

### What it is:
A configuration/settings file.

### What it does:

Defines base directory

Defines where student data files are stored

Stores backup file path

### Why we use it:
To avoid hardcoding file paths in multiple places.

## src/models/student.py

### What it is:
The Student model of the system.

### What it does:

Defines the Student structure using dataclass

Creates unique IDs for each student

Provides conversion functions (to_dict, from_dict)

### Why we use it:
To maintain clean, structured student data.

## src/utils/file_utils.py

### What it is:
Utility functions for reading/writing files.

### What it does:

Ensures the file exists

Responsible for loading JSON

Responsible for saving JSON

Handles corrupted files safely

### Why we use it:
To centralize file operations and avoid repeating file-handling code everywhere.

## src/services/analytics.py

### What it is:
A small module for analytics operations.

### What it does:

Calculates average age

Counts number of students by gender

### Why we use it:
To separate analytic logic from CRUD operations.

##  src/services/student_service.py

### What it is:
The core business logic of the project.

### What it does:

Loads all students into memory

Adds new students

Updates student data

Deletes students

Searches by name

Finds by ID

Saves changes to storage file

Exports backups

### Why we use it:
To separate system logic from the UI/CLI code — following clean architecture principles.

## src/main.py

### What it is:
The CLI (Command Line Interface) of the project.

### What it does:

Provides menu options

Takes user input

Connects the menu to StudentService functions

Displays results (student list, analytics, etc.)

### Why we use it:
So users can interact with the system through a simple text-based menu.

## 📄 tests/test_student.py

### What it is:
Unit tests for the Student Management system.

### What it does:

Creates a temporary test database

Tests adding a student

Tests deleting a student

### Why we use it:
To verify the system works correctly and prevent future bugs.

## Notes

Explains that the project is intentionally simple for beginners and can be extended with:

Sorting

Pagination

Flask API

Adding marks, attendance, etc.

