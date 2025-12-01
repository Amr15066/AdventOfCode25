
dial = 50
zeros= 0
with open("day1-1.txt", "r") as f:
    for line in f:
        number = int(line.replace("L","-")) if line[0] == "L" else int(line.replace("R",""))
        dial = (dial + number) % 100
        if dial == 0:
            zeros+=1
print(zeros)
