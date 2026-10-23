def three_sum(numbers):
    # Write your code here
    numbers = sorted(numbers)
#     x, results = 0, []
#
#     while x < len(numbers):
#         y = x+1
#         while y < len(numbers):
#             for z in range(len(numbers)-1, y, -1):
#                 if numbers[x] + numbers[y] + numbers[z] == 0:
#                     result = [numbers[x], numbers[y], numbers[z]]
#                     if result not in results:
#                         results += [result]
#             y += 1
#         x += 1
#
#     return result

    result = []
    for z in range(len(numbers)-2):
        if z > 0 and numbers[z] == numbers[z - 1]:
            continue
        x, y = z + 1, len(numbers) - 1

        while x < y:
            if (triplet := numbers[z] + numbers[x] + numbers[y]) == 0:
                result += [[numbers[z], numbers[x], numbers[y]]]

                while x < y and numbers[x] == numbers[x + 1]:
                    x += 1
                while x < y and numbers[y] == numbers[y - 1]:
                    y -= 1
                x += 1
                y -= 1

            if triplet < 0:
                x += 1
            elif triplet > 0:
                y -= 1

    return result


if __name__ == "__main__":
    print(three_sum([-2, 0, 0, 0, 0, 0, 0, 0, 0, 2]))
