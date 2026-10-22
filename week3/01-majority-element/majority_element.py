def majority_element(numbers):
    # new_dict, majority = {}, None

    # for num in numbers:
    #     new_dict[num] = new_dict.get(num, 0) + 1
    # for key, value in new_dict.items():
    #     if value > len(numbers) / 2:
    #         majority = key

    majority, count = None, 0
    for num in numbers:
        if count == 0:
            majority = num
            count = 1
        elif num == majority:
            count += 1
        else:
            count -= 1

    return majority if numbers.count(majority) > len(numbers)// 2 else None

