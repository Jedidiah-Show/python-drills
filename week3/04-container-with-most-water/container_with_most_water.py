def max_area(height):
    # Write your code here
    if len(height) < 2:
        return 0

    j, max_area, max_height = 0, 0, height[-1]
    for i in range(len(height)-1, -1, -1):
        # area = lambda x, y: y * x
        # if area(i-j, min())

        area = (i-j) * min(height[j], height[i])

        if area > max_area:
            max_area = area
            if height[i] > height[j]:
                max_height = height[j]
                if max_height < height[i]:
                    max_height = height[i]
                j += 1

    return max_area



