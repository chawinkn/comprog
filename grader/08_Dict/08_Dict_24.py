d = {
	'2': "abc",
	'3': "def",
	'4': "ghi",
	'5': "jkl",
	'6': "mno",
	'7': "pqrs",
	'8': "tuv",
	'9': "wxyz",
	'0': ' '
}
rd = {}

for k in d:
	v = d[k]
	for i in range(len(v)):
		rd[v[i]] = k * (i+1)

def text2keys(text):
	keys = " ".join([rd[i] for i in text.lower() if i in rd])

	return keys

def keys2text(keys):
	text = "".join([d[i[0]][len(i)-1] for i in keys.split()])
		
	return text

# ต้องมีคำสั่งข้ำงล่ำงนี้ ตอนส่งให้ Grader ตรวจ
exec(input().strip())