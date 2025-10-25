def hanoi(n, source, destination, spare):
    if n == 1:
        #best case, move the disk! call this when you oly need to use one disk idiot!
        print(f"move disk from {source} to {destination}")
    else:
        #step1 move n-1 disks from source to spare
        hanoi(n-1, source, spare, destination)
        #step2 move the bottom disk from source to dest
        print(f"move disk from {source} to {destination}")
        #step3 move n-1 disks from spare tp dest
        hanoi(n-1, spare, destination, source)

hanoi(4, 'A','C','B')