# Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:
#  input: "elephant-rides are really fun!"
#           ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
#  words (^):   "elephant" "rides" "are" "really" "fun"
#                 123456     123     1     1234     1
#  ignore short words:               X              X

#  abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
#  all non-word characters (*) remain in place
#                      "-"      " "    " "     " "     "!"
# output: "e6t-r3s are r4y fun!"

import re

regex = re.compile('[a-z]{4,}', re.IGNORECASE)
def replace(match):
    word = match.group(0)
    return word[0] + str(len(word) - 2) + word[-1]

def abbreviate(s: str):
    return regex.sub(replace, s)

