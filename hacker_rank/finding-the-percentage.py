

student_marks = {}

for _ in range(int(input())):
    global line
    name, *line = input().split()
    scores = list(map(float, line))

    student_marks[name]=scores

query_name = input()

#x=[k for k,v in student_marks.items() if k==query_name ]


y=list()

for m in student_marks[query_name]:
    y.append(m)

z=sum(y)/len(y)

print("{:.2f}".format(z))


#link https://www.hackerrank.com/challenges/finding-the-percentage/problem
