print("===== STUDENT INFORMATION AND GRADING SYSTEM =====")

name=str(input("enter name : "))
age=int(input("enter age : "))
course=str(input("enter your course : "))
employement_status=str(input("enter your current employemnt status : "))
monthly_stipend=float(input("enter your stipend : "))

student=(name,age,course,employement_status,monthly_stipend)
new_name=name[:3]
uppercase=new_name.upper()

subjects={}
mark_list=[]
sub_list=int(input("\n enter the number of subjects : "))

for i in range(sub_list):
    subject=str(input("enter the subject : "))
    marks=float(input("enter the corresponding marks : "))

    subjects[subject]=marks
    mark_list.append(marks)

print("== STUDENT PROFILE == ")

print("NAME                 :", name)
print("AGE                  :", age)
print("COURSE               :", course)
print("EMPLOYMENT STATUS    :",employement_status)
print("MONTHLY STIPEND      :",monthly_stipend)
print("first 3 letters of the name : ",new_name)
print("First 3 letters in caps : ",uppercase)
print(student)

for subject,marks in subjects.items():
    print(subject, " : " , marks)


new_mark=float(input("\n enter the new mark : "))
mark_list.append(new_mark)
print(f"Marks after adding new mark : {mark_list}")

remove=float(input("enter the marks that need to be removed : "))

if remove in mark_list:
    mark_list.remove(remove)
    print(f"Marks after removing : {mark_list}")
else:
    print("Mark not found")

mark_list.sort()
print(f"\n SORTED MARKLIST : {mark_list}")

unique=list(set(mark_list))
unique.sort()
print(f"marks without duplicates : {unique}")

update_subjects=str(input("enter the subject whose mark you want to update : "))

if update_subjects in subjects:
    updated_mark=float(input("enter new mark : "))
    subjects[update_subjects]=updated_mark
    print(f"updated {update_subjects} mark : {updated_mark}")
else:
    print("subject not found")

new_subject=str(input("\nenter new subject : "))
sub_mark=float(input("enter the new mark : "))
subjects[new_subject]=sub_mark
print("\nupdated subject wise mark : ")

for subject,marks in subjects.items():
    print(f"{subjects} : {marks}")

subject_set=frozenset(subjects.keys())
print("\nsubjects using frozenset : ",subject_set)
print(f"data type of frozenset : {type(subject_set)}")

print("---- ONLINE AND OFFLINE STUDENTS ----")

online_std=set(input("enter the students in online : ").split(","))
offline_std=set(input("enter the students in offline : ").split(","))

print(f"ONLINE STUDENTS ARE : {online_std}")
print(f"OFFLINE STUDENTS ARE : {offline_std}")

common_std=online_std.intersection(offline_std)
print(f"COMMON STUDENTS ARE : {common_std}")

registerd=online_std.union(offline_std)
print(f"all registered students are : {registerd}")

exclu_online=online_std.difference(offline_std)
print(f"exclusivly online students are : {exclu_online}")

print("==== AVERAGE MARKS ==== ")

total_marks=sum(mark_list)
average_marks=total_marks/len(mark_list)
print(average_marks)

print("==== GRADING ====")

if average_marks>=90:
    grade="A"
elif average_marks>=75:
    grade="B"
elif average_marks>=50:
    grade="C"
else:
    grade="Fail"

print("\n===== FINAL RESULT =====")

print(f"Total Marks   : {total_marks}")

print(f"Average Marks : {average_marks:.2f}")

print(f"Grade         : {grade}")

print("\n===== DATA TYPES =====")

print(f"Name             : {type(name)}")

print(f"Age              : {type(age)}")

print(f"Course           : {type(course)}")

print(f"Employment       : {type(employement_status)}")

print(f"Monthly Stipend  : {type(monthly_stipend)}")

print(f"Student Tuple    : {type(student)}")

print(f"Marks List       : {type(marks)}")

print(f"Subject Dictionary : {type(subjects)}")

print(f"Frozenset        : {type(subject_set)}")

print(f"Online Students  : {type(online_std)}")

print(f"Offline Students : {type(offline_std)}")

print(f"Average Marks    : {type(average_marks)}")





