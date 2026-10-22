def max_area(height):
    # Write your code here
    if len(height) < 2:
        return 0

#     j, max_area, max_height = 0, 0, height[-1]
#     for i in range(len(height)-1, -1, -1):
#         area = (i-j) * min(height[j], height[i])
#
#         if area > max_area:
#             max_area = area
#             if height[i] > height[j]:
#                 max_height = height[j]
#                 if max_height < height[i]:
#                     max_height = height[i]
#                 j += 1

    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        tallest = height[left] if height[left] < height[right] else height[right]
        area = (right -left) * tallest
        # area = (right - left) * min(height[left], height[right])

        max_area = area if max_area < area else max_area
        # max_area = max(max_area, area)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area



