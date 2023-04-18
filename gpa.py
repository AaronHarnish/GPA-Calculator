import time
g = ''
d = 0
w = 0
gpa = 0.0
count = 0

print("High School GPA Calculator\nBy Aaron Harnish\n----------------")
time.sleep(1)
print("Class Difficulty Inputs:\nCareer/College Prep: 1\nHonors: 2\nAP: 3\nAP+(Dual Enrollment): 4\n----------------")
print("Enter grades as capital letters (A, B, C, etc.)\n----------------\nIf you don't have a class in that period or it isn't weighted, write N/A")

for i in range(1,5):
    print("Enter grade for your block %s class" % (i))
    g = raw_input("> ")
    if g == 'N/A':
        continue

    print("Enter difficulty for your block %d class" % (i))
    d = float(input("> "))

    w = (d / 2) + 3.5
    if g == 'A':
        gpa += (w)
    elif g == 'B':
        gpa += (w-1)
    elif g == 'C':
        gpa += (w-2)
    elif g == 'D':
        gpa +=(w-3)
    elif g == 'F':
        gpa += (0.0)

    count += 1

print("Your final GPA for the semester is:")
print(gpa / count)
