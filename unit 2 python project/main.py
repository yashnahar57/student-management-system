departments_set = {"AIML", "AIDS", "CSE", "IT"}
subjects_set = {
    "Data Structures",
    "Python Programming",
    "Database Systems",
    "Operating Systems",
}
clubs_set = {"Coding Club", "Robotics Club", "Literary Club"}

student_records = []


def add_student():
  print("\n--- Add New Student Record ---")

  prn = input("Enter PRN (e.g., 2126UMLM): ").strip()
  reg_no = input("Enter Registration Number: ").strip()
  dob = input("Enter Date of Birth (DD-MM-YYYY): ").strip()
  identifier_tuple = (prn, reg_no, dob)

  for student in student_records:
    if student["identifier"][0].lower() == prn.lower():
      print("Error: Student with this PRN already exists!")
      return

  name = input("Enter Student Name: ").strip()
  dept = input("Enter Department: ").strip()
  if dept not in departments_set:
    print(
        f"Warning: Department '{dept}' is not in the standard departments set."
    )

  address = input("Enter Address: ").strip()
  email = input("Enter Email ID: ").strip()
  contact_info = {"address": address, "email": email}

  # Input validation to prevent crashes if text is entered instead of a number
  while True:
    try:
      n_subjects = int(input("Enter number of subjects (e.g., 2): "))
      break
    except ValueError:
      print("Invalid input. Please enter a valid number (e.g., 2, 3).")

  subjects_list = []
  marks_list = []
  attendance_list = []

  for i in range(n_subjects):
    subj = input(f"Enter Subject {i+1} name: ").strip()
    subjects_list.append(subj)
    mark = float(input(f"Enter marks for {subj}: "))
    marks_list.append(mark)
    att = float(input(f"Enter attendance percentage for {subj}: "))
    attendance_list.append(att)

  student_profile = {
      "identifier": identifier_tuple,
      "name": name,
      "department": dept,
      "contact": contact_info,
      "subjects": subjects_list,
      "marks": marks_list,
      "attendance": attendance_list,
  }

  student_records.append(student_profile)
  print("Student record added successfully!")


def search_student():
  print("\n--- Search Student by PRN ---")
  prn = input("Enter PRN to search: ").strip()
  found = False
  for student in student_records:
    if student["identifier"][0].lower() == prn.lower():
      print("\nRecord Found:")
      print(f"PRN: {student['identifier'][0]}")
      print(f"Registration Number: {student['identifier'][1]}")
      print(f"Date of Birth: {student['identifier'][2]}")
      print(f"Name: {student['name']}")
      print(f"Department: {student['department']}")
      print(f"Email: {student['contact']['email']}")
      print(f"Address: {student['contact']['address']}")
      print("Academic Performance:")
      for s, m, a in zip(
          student["subjects"], student["marks"], student["attendance"]
      ):
        print(f"  - {s}: Marks = {m}, Attendance = {a}%")
      found = True
      break
  if not found:
    print("Student record not found.")


def update_student():
  print("\n--- Update Student Information ---")
  prn = input("Enter PRN of student to update: ").strip()
  for student in student_records:
    if student["identifier"][0].lower() == prn.lower():
      print(
          "1. Update Name\n2. Update Department\n3. Update Contact Information"
      )
      choice = input("Enter choice (1-3): ").strip()
      if choice == "1":
        student["name"] = input("Enter new name: ").strip()
        print("Name updated successfully.")
      elif choice == "2":
        student["department"] = input("Enter new department: ").strip()
        print("Department updated successfully.")
      elif choice == "3":
        student["contact"]["address"] = input("Enter new address: ").strip()
        student["contact"]["email"] = input("Enter new email: ").strip()
        print("Contact information updated successfully.")
      else:
        print("Invalid choice.")
      return
  print("Student record not found.")


def delete_record():
  print("\n--- Delete Student Record ---")
  prn = input("Enter PRN to delete: ").strip()
  for i, student in enumerate(student_records):
    if student["identifier"][0].lower() == prn.lower():
      del student_records[i]
      print("Student record deleted successfully.")
      return
  print("Student record not found.")


def calculate_average_marks():
  print("\n--- Calculate Average Marks ---")
  prn = input("Enter PRN: ").strip()
  for student in student_records:
    if student["identifier"][0].lower() == prn.lower():
      marks = student["marks"]
      if marks:
        avg = sum(marks) / len(marks)
        print(
            f"Average marks for {student['name']} (PRN:"
            f" {student['identifier'][0]}): {avg:.2f}"
        )
      else:
        print("No marks available for this student.")
      return
  print("Student record not found.")


def find_highest_scorer():
  print("\n--- Find Highest Scorer ---")
  if not student_records:
    print("No student records available.")
    return

  highest_avg = -1
  top_student = None

  for student in student_records:
    marks = student["marks"]
    if marks:
      avg = sum(marks) / len(marks)
      if avg > highest_avg:
        highest_avg = avg
        top_student = student

  if top_student:
    print(
        f"Highest Scorer: {top_student['name']} (PRN:"
        f" {top_student['identifier'][0]}) with Average Marks:"
        f" {highest_avg:.2f}"
    )
  else:
    print("No marks recorded for any student.")


def list_students_by_department():
  print("\n--- List Students by Department ---")
  dept = input("Enter Department name: ").strip()
  found = False
  print(f"\nStudents in Department: {dept}")
  for student in student_records:
    if student["department"].lower() == dept.lower():
      print(
          f"- PRN: {student['identifier'][0]}, Name: {student['name']},"
          f" Email: {student['contact']['email']}"
      )
      found = True
  if not found:
    print("No students found in this department.")


def count_students():
  print(f"\nTotal number of students: {len(student_records)}")


def main():
  while True:
    print("\n=== Student Record and Academic Management System ===")
    print("1. Add New Student Record")
    print("2. Search Student by PRN")
    print("3. Update Student Information")
    print("4. Delete Record")
    print("5. Calculate Average Marks")
    print("6. Find Highest Scorer")
    print("7. List Students by Department")
    print("8. Count Students")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ").strip()
    if choice == "1":
      add_student()
    elif choice == "2":
      search_student()
    elif choice == "3":
      update_student()
    elif choice == "4":
      delete_record()
    elif choice == "5":
      calculate_average_marks()
    elif choice == "6":
      find_highest_scorer()
    elif choice == "7":
      list_students_by_department()
    elif choice == "8":
      count_students()
    elif choice == "9":
      print("Exiting system. Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()