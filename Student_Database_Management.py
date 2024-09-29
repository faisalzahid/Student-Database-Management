def manage_student_database():
    # Step 1: Initialize an empty list to store student tuples and a counter for IDs
    students = []
    student_id = 1

    # Step 2: Handle user input
    while True:
        name = input("Please enter the student's name (or type 'stop' to finish): ").strip()
        
        # Check if user wants to stop the input process
        if name.lower() == 'stop':
            break

        # Step 3: Check for duplicate names
        if any(student[1] == name for student in students):
            print("This name is already in the list.")
        else:
            # Add student tuple (ID, name) to the list
            students.append((student_id, name))
            student_id += 1

    # Step 4: Display the complete list of students
    print("\nComplete List of Students (Tuples):")
    print(students)

    # Step 5: Display each student's ID and name individually
    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

    # Step 6: Calculate and display statistics
    total_students = len(students)
    total_length_of_names = sum(len(student[1]) for student in students)
    if students:
        longest_name_student = max(students, key=lambda student: len(student[1]))
        shortest_name_student = min(students, key=lambda student: len(student[1]))

        # Display statistics
        print(f"\nTotal number of students: {total_students}")
        print(f"Total length of all student names combined: {total_length_of_names}")
        print(f"The student with the longest name is: {longest_name_student[1]}")
        print(f"The student with the shortest name is: {shortest_name_student[1]}")
    else:
        print("\nNo students were added to the list.")

# Step 7: Call the manage_student_database() function
manage_student_database()
