def index_of(grades, ID):
	for i in range(len(grades)):
		if grades[i][0] == ID:
			return i
	return -1

def upgrade(grades, IDs):
	grade_lst = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
	for i in IDs:
		idx = index_of(grades, i)
		if idx == -1:
			continue
		j = grade_lst.index(grades[idx][1])

		if j > 0:
			grades[idx][1] = grade_lst[j-1]
	
	grades.sort()

# DON'T remove the following three lines
exec(input())
exec(input())
exec(input()) 