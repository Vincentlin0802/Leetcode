def threeConsecutiveOdds(arr):
    counter = 0
    for i in range(len(arr)):
        if arr[i]%2 != 0:
            counter += 1
        else:
            counter = 0
        if counter == 3:
            return True
    return False
