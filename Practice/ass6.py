n = int(input("Enter the number of processes: "))

processes = {}

for i in range( 1, n+1):

    processes[i] = int(input((f'Is process {i} alive or dead? (0=dead, 1=alive): ')))


initiator = int(input("Enter the process starting the election: "))

if initiator == 0:
    print("Initiator process is down")

else:

    #bully algorithm

    coordinator = initiator

    for i in range(initiator + 1, n+1):

        if processes[i] == 1:
            print(f"Election message send to process {i}")

            coordinator = i

    print("New Cordinator: ", coordinator)


    #ring algorithm

    active = []

    i = initiator

    while True:

        if processes[i] == 1:
            active.append(i)

        i += 1

        if i > n:
            i = 1

        if i == initiator:
            break
    print("New Cordinator", max(active))