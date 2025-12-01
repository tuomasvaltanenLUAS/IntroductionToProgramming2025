# text submission grading
# * is a bad char -> penalty, otherwise add points
addition = 5

# this is usually better, if logic is not always: (points * -1)
penalty = -5

# use some test data
submissions = [["AB", "CE*", "FF", "EE*", "EE", "EE", "EE", "EE", "EE"],
               ["A*B", "CE*", "*FF", "EE", "EE", "EE", "EE"],
               ["AB", "CE*", "FF", "HJ", "AY", "UU", "FF", "FF", "FF", "FF*"]]

# point limits -> text description
areas = {"0-19": "Low", "20-29": "Middle", "30-39": "High"}

# collect the results of data processing into this list
results = []

# ask user how much data will be processed
selection = int(input("Amount of cycles: \n"))
print()

# by default, we process all data rows
max_range = len(submissions)

# if user gives a different limit, use that instead
if 0 <= selection < len(submissions):
    max_range = selection

# STEP 1: process each text within the original data
for index in range(max_range):
    score = 0
    submission = submissions[index]

    # add or reduce points based on text content
    for text in submission:
        if "*" in text:
            score += penalty
        else:
            score += addition

    # save points regarding this list
    results.append(score)

# get the keys of the limits into a separate collection
range_keys = areas.keys()

# ------------------------------
# STEP 2: go through the results
for result in results:

    # find the needed limit boundary for current list score
    for range_index in range_keys:
        parts = range_index.split("-")
        min_range = int(parts[0])
        max_range = int(parts[1])

        # if we found a suitable text description with given limits
        # => print a summary of points
        if min_range <= result <= max_range:

            # get the needed texts for this summary and combine
            grade_text = areas[range_index]
            submission_index = results.index(result)
            submission_values = ", ".join(submissions[submission_index])

            # print the summary
            print(f"{grade_text} \t({result} pts) \t-> {submission_values}")
