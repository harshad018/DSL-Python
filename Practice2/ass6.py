n = int(input("Enter the number of processes: "))

processes = {}


for i in range(1, n + 1):
    processes[i] = int(input(f"is the process {i} active or dead? ( 0=dead, 1=active): "))


initiator = int(input("Enter the process initiating the election: "))


if ( initiator == 0):
    print("Initiator is also down !!")

else:

    #Bully Algorithm 

    coordinator = initiator

    for i in range(initiator + 1, n+1):
        if processes[i] == 1:
            print("Election message has passed to process", i)
            coordinator = i

    print("New Cordinator using bully algorithm: ", coordinator)


    #Ring Algorithm

    active = []
    i = initiator

    while True:

        if processes[i] == 1:
            print("Election is message is passed")
            active.append(i)

        i += 1

        if i > n:
            i = 1

        if i == initiator:
            break


    print("New cordinator using Ring algorithm is ", max(active))