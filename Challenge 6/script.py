import re


def trace(test_str, regex):
    matches = re.finditer(regex, test_str, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):

        print("Match {matchNum} was found : {match}".format(matchNum=matchNum, match=match.group()))
        if match.group(1) !="":
            print(match.group(1))
        return match.group(2)


regex = r"(.*)Next nothing is (\d+)$"
nextFile = "90052"
i=1
while True:
    with open(nextFile+".txt") as f:
        line = f.readline()
    nextFile = str(trace(line, regex))
    i+=1
    if nextFile == "None":
        break
print(i)