newfile.pyfrom openpyxl import Workbook, load_workbook
import os

# Excel file ka naam
file_name = "helpdesk.xlsx"

# Agar Excel file pehle se nahi hai to nayi file banao
if not os.path.exists(file_name):
    wb = Workbook()
    ws = wb.active
    ws.title = "Records"
    ws.append(["Student Name", "Issue"])
    wb.save(file_name)

# Existing Excel file load karo
wb = load_workbook(file_name)
ws = wb.active

print("===== Smart Student Help Desk =====")
name = input("Enter Student Name: ")

print("\nSelect Your Issue:")
print("1. Fees Issue")
print("2. Academic Issue")
print("3. Technical Issue")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    issue = "Fees Issue"
    print("Guidance: Please contact the accounts office.")
elif choice == "2":
    issue = "Academic Issue"
    print("Guidance: Please meet your subject teacher.")
elif choice == "3":
    issue = "Technical Issue"
    print("Guidance: Please visit the IT support desk.")
else:
    issue = "Invalid Choice"
    print("Invalid option selected.")

# Record Excel me save karo
ws.append([name, issue])
wb.save(file_name)

print("\nYour record has been saved successfully.")