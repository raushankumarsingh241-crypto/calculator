student = {
    101: {"Name": "Raushan", "Course": "MCA", "mark": 80},
    102: {"Name": "Ravi", "Course": "Hindi", "mark": 85},
    103: {"Name": "Sahil", "Course": "Physics", "mark": 82},
    104: {"Name": "Rohan", "Course": "Math", "mark": 78},
    105: {"Name": "Rohit", "Course": "Chemistry", "mark": 75}
}

print("Student details")

for roll_no in student:
    print("Roll-No:", roll_no,end="\t")
    print("Name:", student[roll_no]["Name"],end="\t")
    print("Course:", student[roll_no]["Course"],end="\t")
    print("Mark:", student[roll_no]["mark"])