'''Count the number of elements in scores that are 100 or above.

scores = [96, 47, 113, 89, 100, 102]'''

# didn't manage to get the solution: 

scores = [96, 47, 113, 89, 100, 102]

count = 0

for score in scores:
    if score >= 100:
        count +=1

print(count)

'''
launch school solution 2:

high_scores = [score for score in scores if score >= 100]
print(len(high_scores)) # 3

Let's break down the second solution:

[score for score in scores if score >= 100] is the core part of the solution. It's a list comprehension that lets us create a new list based on the existing list (scores in this case). Let's break this expression down:
for score in scores: This iterates over each element in the scores list. Each element is temporarily referred to as score.
if score >= 100: This is a condition applied to each score. Only scores that are greater than or equal to 100 pass this condition.
score (at the beginning of the comprehension): Each score that passes the condition is included in the new list. So, this list comprehension results in a new list that contains only the scores that are 100 or higher.
The len function determines and returns the length of the list created by the list comprehension.
In the end, we print the result stored in the high_scores variable.
'''