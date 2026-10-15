def frequency_sort(items):
    # Write your code here
    if not items:
        return []
    items_dict = {}
    for item in items:
        items_dict[item] = items_dict.get(item, 0) + 1
    items_dict = dict(sorted(items_dict.items(), key=lambda x: (x[0], -x[1])))

    result = []
    for item, freq in items_dict.items():
        result += [item] * freq
    return result


if __name__ == '__main__':
    print(frequency_sort([3, 3, 1, 1, 2,3]))
    print(frequency_sort([5, 4, 3, 2, 1]))
    print(frequency_sort([7, 7, 7, 7]))
    print(frequency_sort([4, 1, 4, 1, 2, 2]))
