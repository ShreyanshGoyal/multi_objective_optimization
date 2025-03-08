from moma.agents import Student
from moma.objectives import job, gradstudy, health, social, explore
from moma.optimization import run_optimization

student_list = [
    Student(student_id=0, num_obj=1, objs=[job]),
    Student(student_id=1, num_obj=1, objs=[gradstudy]),
    Student(student_id=2, num_obj=1, objs=[health]),
    Student(student_id=3, num_obj=1, objs=[social]),
    Student(student_id=4, num_obj=2, objs=[explore, social])
]

result = run_optimization(student_list)
print("Optimal Decision Variables:", result.X)
print("Objective Values:", result.F)
