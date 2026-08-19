#a ZIP methode is used to combine two or more iterable item togethe to form tuple format till the shortest itrable item

student_name  = ["X singh","Y Singh","Z Singh","T Singh"]
student_marks = [99.54,98.22,85.88,75.99]
student_grade = ["A","B","C","D"]

my_new_list  = zip(student_name,student_marks,student_grade)

# new_it = my_new_list
# my_it = my_new_list

# for items in my_new_list:
#     print("in First loop ",items)


# for items in my_new_list:
#     print("in second loop ",items)

for name,marks,grade in my_new_list:
    print("in Third loop Candidate name =",name,"Have marks =",marks,"with grade =",grade)