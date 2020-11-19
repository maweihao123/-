file =open(r'C:\Users\maweihao\Desktop\student.csv','r')
lines = file.readlines()
students = {}
for line in lines:
    tmp_list=line.split(',')
    xuehao =tmp_list[0]
    xingming = tmp_list[1]
    students[xuehao]=xingming
    
print(students)
import random

num=int(input("输入你要抽取的人数："))
xuehao_list=random.sample(students.keys(),num)

for xuehao in xuehao_list:
    print(students[xuehao])