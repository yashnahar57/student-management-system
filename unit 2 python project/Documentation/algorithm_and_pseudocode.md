## 1. Add Student Record
- Algorithm:
  1. Input PRN, Registration Number, and Date of Birth into a Tuple.
  2. Check if PRN already exists in the master record list. If duplicate, show error.
  3. Prompt for Name, Address, Email, and Department (validate against predefined department Set).
  4. Prompt for total subjects, then loop to take Subject Name, Marks, and Attendance into Lists.
  5. Combine all fields into a profile Dictionary and append to the master list.

- Pseudocode:
  FUNCTION add_student():
      INPUT prn, reg_no, dob
      IF prn in student_records THEN:
          PRINT "PRN already exists"
          RETURN
      INPUT name, department, address, email
      INPUT num_subjects
      FOR i = 1 TO num_subjects:
          INPUT subject, marks, attendance
          APPEND to respective lists
      CREATE student_dict
      APPEND student_dict TO student_records
      PRINT "Student added successfully"
  END FUNCTION

## 2. Search & Update Record
- Algorithm: 
  Iterate through `student_records`. Compare the requested PRN with the PRN tuple inside each student profile. If found, display details or prompt for field updates; otherwise, return a "Not Found" message.

## 3. Reports & Analytics
- Algorithm:
  Loop through records to calculate average marks, identify the highest average score using comparative logic, filter students by department matching, and return total record counts.