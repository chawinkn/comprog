# WORST CODE HERE

s = input()
score, frame = [0]*10, 0
result = [""]*10
i, j, cnt = 0, 0, 0

def cal(c):
	return int(c) if c.isdigit() else 10

while j < len(s):
	cnt += 1

	if (frame != 9 and (s[j] == 'X' or cnt == 2)) or frame == 9:
		if frame == 9:
			j = len(s) - 1
		score[frame] = sum(cal(c) for c in s[i:j+1])
		sz = j-i+1

		if sz == 2 and s[i+1] == '/':
			score[frame] -= cal(s[i])
			if frame != 9:
				score[frame] += cal(s[i+2])
		elif sz == 3:
			if s[i+1] == '/':
				score[frame] -= cal(s[i])
			elif s[i+2] == '/':
				score[frame] -= cal(s[i+1])
		elif s[i] == 'X' and frame != 9:
			if '/' in s[i+1:i+3]:
				score[frame] += 10
			else:
				score[frame] += cal(s[i+1]) + cal(s[i+2])
		# print(frame, s[i:j+1], " -> ", score[frame], j)

		j += 1; i = j
		frame += 1
		cnt = 0
	else:
		j += 1

n = int(input())
if 1 <= n <= 10:
	print(score[n-1])
else:
	print(sum(score))