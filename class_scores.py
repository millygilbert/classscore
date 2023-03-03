##
# class_scores.py
# Milly
# 02/03/23

# Lists of class scores 
class_a = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
class_b = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

# Combine list
both_classes = class_a + class_b
print(both_classes)
for score in both_classes:
    count += 1
    total_score += both_classes
    


# Print lowest score
lowest_score = min(both_classes)
print("The lowest score is {}".format(lowest_score))

# Print median score
median_score = total_score / count
print("The median score is {}".format(median_score))

# Print highest score
print("HI")
