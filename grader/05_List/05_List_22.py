ids, grades = [], []

while (s := input()) != 'q':
	id, grade = s.split()
	ids.append(id)
	grades.append(grade)

uids = input().split()
grade_lst = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]

for id in uids:
	i = ids.index(id)
	grade = grades[i]
	j = grade_lst.index(grade)
	if j > 0:
		grades[i] = grade_lst[j-1]

again = sorted([[ids[i], grades[i]] for i in range(len(ids))])

for id, grade in again:
	print(id, grade)