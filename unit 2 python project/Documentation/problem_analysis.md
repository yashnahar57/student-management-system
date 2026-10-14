## 1. Problem Statement
The objective of this project is to develop a Student Record and Academic Management System in Python to store, manage, search, update, and analyze student academic data efficiently.

## 2. Data Structure Selection & Rationale
- Strings: Used to process text-based inputs such as student names, departments, addresses, and email IDs.
- Lists: Used to hold mutable collections, including the master list of all student records, lists of subject names, marks, and attendance values.
- Tuples: Used to store immutable student identifiers like PRN (Permanent Registration Number), registration number, and date of birth.
- Sets: Used to maintain unique, fixed categories like valid department names (`AIML`, `AIDS`, `CSE`, `IT`) and subject names to prevent duplicates.
- Dictionaries: Used as the primary schema for student profiles, mapping keys (e.g., `name`, `department`, `identifiers`, `contact`, `academic_data`) to structured student details.