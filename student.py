STUDENTS = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    student = {"roll": roll, "name": name, "marks": marks}
    STUDENTS.append(student)
    print("✅ Student record added successfully!\n")

def view_students():
    if not STUDENTS:
        print("❌ No student records found.\n")
        return
    print("\nRoll\tName\tMarks")
    print("-" * 25)
    for s in STUDENTS:
        print(f"{s['roll']}\t{s['name']}\t{s['marks']}")
    print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    for s in STUDENTS:
        if s["roll"] == roll:
            print("\n🎯 Student Found")
            print(f"Roll  : {s['roll']}")
            print(f"Name  : {s['name']}")
            print(f"Marks : {s['marks']}\n")
            return
    print("❌ student not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    for s in STUDENTS:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            s["marks"] = float(input("Enter new marks: "))
            print("✅ Student record updated successfully!\n")
            return
    print("❌ Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    for s in STUDENTS:
        if s["roll"] == roll:
            STUDENTS.remove(s)
            print("🗑️ Student record deleted successfully!\n")
            return
    print("❌ Student not found.\n")

def sort_students():
    STUDENTS.sort(key=lambda x: x["marks"], reverse=True)
    print("📊 Students sorted by marks (descending order).\n")

def menu():
    while True:
        print("===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort Students by Marks")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            sort_students()
        elif choice == "7":
            print("👋 Exiting program. Thank you!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

menu()
