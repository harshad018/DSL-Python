n = int(input("Enter number of processes: "))

process = []

for i in range(n):
    process.append(i+1)

token = int(input("Enter process holding token initially: "))

while True:
    request = int(input("Enter process requesting critical section(0 to exist) : "))

    if request == 0:
        print("Program Ended.")
        break

    print("Token Passing : ")

    while token != request:
        print("Process",token,"passes token.")
        token = token + 1

        if token > n:
            token = 1

    print("process",request,"enters critical section .")
    print("process",request," exists critical section .")