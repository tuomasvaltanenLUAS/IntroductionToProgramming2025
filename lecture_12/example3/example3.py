# CODE REQUIREMENTS:
#
# This file has an application, that contains a list of lists of string data.
# The idea is to analyze how many good and bad texts there are in each list.
#
# After defining the testing data the code processes each
# list one at a time, and within each list, one text at a time
# => if text doesn't have the character '*' => give 5 points
# => if text has the character '*'          => reduce 5 points
#
# Finally, code outputs a verbal grade of each list's total points:
# => if points within 0-19, print "Low"
# => if points within 20-29, print "Middle"
# => if points within 30-39, print "High"

# text submission grading code
# * is a bad char -> penalty, otherwise add points
addition = 5
penalty = addition * -1

# test values, should come from data API later
submissions = [["AB", "CE*", "FF", "EE*", "EE", "EE", "EE", "EE", "EE"],
               ["A*B", "CE*", "*FF", "EE", "EE", "EE", "EE"],
               ["AB", "CE*", "FF", "HJ", "AY", "UU", "FF", "FF", "FF", "FF*"]]

areas = {"0-19": "Low", "20-29": "Middle", "30-39": "High"}
results = []

selection = int(input("Amount of cycles: \n"))
print()

max_range = (selection, len(submissions))[selection > (len(submissions) - 1)]

# loop submissions
for sub in range(max_range):
    score = 0
    for state in submissions[sub]: score += penalty if "*" in state else addition
    results.append(score)

# loop results
for r in results:
    for i in areas.keys(): print(areas[i], f"\t({r} pts)", "\t-> ", ", ".join(submissions[results.index(r)])) \
        if int(i.split("-")[0]) <= r <= int(i.split("-")[1]) else print("", end="")