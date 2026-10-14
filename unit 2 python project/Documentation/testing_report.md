## 1. Duplicate PRN Testing
- Test Case: Input a PRN that already exists in `student_records`.
- Expected Result: System blocks entry and displays a duplicate PRN error message.
- Actual Result: Passed.

## 2. Invalid Input Testing
- Test Case: Enter non-numeric values for subject counts, marks, or attendance.
- Expected Result: Program prompts with appropriate error messages instead of crashing.
- Actual Result: Passed.

## 3. Empty Record Testing
- Test Case: Run search, update, delete, or calculate functions before adding any student.
- Expected Result: System handles empty state gracefully with a "No records found" message.
- Actual Result: Passed.

## 4. Boundary Value Testing
- Test Case: Test edge inputs like 0 and 100 for marks, and 0% and 100% for attendance.
- Expected Result: System accepts boundary values properly.
- Actual Result: Passed.