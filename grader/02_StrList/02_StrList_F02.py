def number_name(n):
    # คืนคำอ่ำนของตัวเลข (หลักเดียว) ตำมตำรำงข้ำงบนนี้
    # n: เป็นสตริงเก็บเลขหลักเดียว '0', '1', ..., '9'
    # หรือ เป็นจำนวนเต็มหรือจำนวนจริงมีค่ำ 0,1,2,...,9
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    return num[int(n)]


exec(input())  # DON'T remove this line
