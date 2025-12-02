def part1():
    with open("day2.txt", "r") as f:
        f = f.readline()
        ranges = f.split(",")
        invalid_IDs = []
        for rng in ranges:
            start, end = int(rng.split("-")[0]), int(rng.split("-")[1])

            for i in range(start, end + 1):
                if len(str(i)) %2  == 0:
                    first_half = str(i)[:len(str(i))//2]
                    second_half = str(i)[len(str(i))//2:]
                    if first_half == second_half:
                        invalid_IDs.append(i)


        print(sum(invalid_IDs))
                    
                
def part2():
    with open("day2.txt", "r") as f:
        f = f.readline()
        ranges = f.split(",")
        invalid_IDs = []
        for rng in ranges:
            start, end = int(rng.split("-")[0]), int(rng.split("-")[1])    
            for i in range(start, end + 1):
                state= False 
                if len(str(i)) %2  == 0:
                    first_half = str(i)[:len(str(i))//2]
                    second_half = str(i)[len(str(i))//2:]
                    if first_half == second_half:
                        invalid_IDs.append(i)
                        state= True
                        break
                if state == True:
                    break
                k = 0
                for j in range(i):
                    k+=1 if i[k] == i[j+1] else -k
                if k != 0:
                    invalid_IDs.append(i)
                    print(i)
    print(sum(invalid_IDs))                




     
"""
11-22
create a list that starts with 11 and ends with 22
find something that checks number of consequtive identical characters
or filter it all out take evertrihng out you'd get this
111213141516171819202122
at i
after finding a number append it to the list
for i in range(11,23):
    print(i)
"""

part1()