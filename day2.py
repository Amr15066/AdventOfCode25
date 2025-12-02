'''def part1():
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
                    '''
                
def part2():
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
                        print(i)
                        continue
                k = 0
                m = 0
                if i == 1221221:
                    print("here")
                i = str(i)
                for j in range(len(i)-1):
                    if i[k] == i[j+1]: 
                        k+=1
                    else:
                        m+=1
                        k=0

                if k> int(len(i)/2) :
                    if (k % 2 != 0 and len(i) % 2 != 0 ):
                        continue
                    invalid_IDs.append(int(i))
                    print(i)
    print(sum(invalid_IDs))                



def other_method():
    with open("day2.txt", "r") as f:
        f = f.readline()
        ranges = f.split(",")
        invalid_IDs = []
        for rng in ranges:
            start, end = int(rng.split("-")[0]), int(rng.split("-")[1])
            for i in range(start, end + 1):
                i = str(i)
                for j in range(len(i)-1):
                    if len(i) % (j+2) == 0:
                        chunks = divide_into_chunks(i,j+2)
                        if all(chunk == chunks[0] for chunk in chunks):
                            invalid_IDs.append(int(i))
                            print(i)
                            break
    print(sum(invalid_IDs))   

def divide_into_chunks(number, divisions):
    return list(number[i:i + len(number) // divisions] for i in range(0, len(number), len(number) // divisions))

        
#other_method()
part2()


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
                i = str(i)
                m=0
                l=[""]
                for j in range(len(i)-1):
                    l[m] += i[j]
                    if i[k] == i[j+1]:
                        

                    k+=1  else -k
                if k != 0:
                    if k
                    invalid_IDs.append(int(i))
                    print(i)
    print(sum(invalid_IDs))                


    
"""

