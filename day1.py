
def part1():        
    dial = 50
    zeros= 0
    with open("day1.txt", "r") as f:
        for line in f:
            number = int(line.replace("L","-")) if line[0] == "L" else int(line.replace("R",""))
            dial = (dial + number) % 100
            if dial == 0:
                zeros+=1
    print(zeros)

def part2():
    dial = 50
    count= 0 
    total_rotations = 0
    with open("day1.txt", "r") as f:
        for line in f:
            rots = 0
            number = int(line.replace("L","-")) if line[0] == "L" else int(line.replace("R",""))
            rots = abs(number) // 100
            if number > 0:
                remainder = number % 100 + dial
                rots+= 1 if  remainder>= 100 else 0
            else:
                remainder= -1*((-1*number)%100) + dial
                rots+= 1 if  remainder<0 else 0
            total_rotations += rots
            old_dial=dial
            dial = (dial + number) % 100
    print(dial)
    print(total_rotations)

part2()
