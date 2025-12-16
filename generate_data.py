import csv
import random

def generate_students():
    students = []
    # Generate 62 student
    for i in range(1, 63):
        # Format: BSDSF24M001, BSDSF24M002, ...
        roll_no = f"BSDSF24M{i:03d}"
        
        # Mock names
        first_names = ["Ali", "Ahmed", "Bilal", "Zara", "Sara", "Fatima", "Omar", "Usman", "Hassan", "Ayesha"]
        last_names = ["Khan", "Malik", "Raza", "Shah", "Ahmed", "Butt", "Sheikh", "Jutt", "Iqbal", "Bibi"]
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        
        students.append([roll_no, name])

    # Write to CSV
    with open(r"d:\DS'F24 LMS\students.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Roll Number", "Name"]) # Header
        writer.writerows(students)
    
    print(f"Generated {len(students)} students in students.csv")

if __name__ == "__main__":
    generate_students()
