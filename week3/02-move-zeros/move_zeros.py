def move_zeros(numbers):
    # for i in range(len(numbers)-1, -1, -1):
    #     if numbers[i] == 0:
    #         numbers.pop(i)
    #         numbers.append(0)

    j = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[j] = numbers[i]
            if i != j:
                numbers[i] = 0
            j += 1


if __name__ == "__main__":
    print(move_zeros([0,1,0,3,4,0,1,0]))
