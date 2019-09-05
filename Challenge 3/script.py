import re


def trace(test_str, regex):

    matches = re.finditer(regex, test_str, re.MULTILINE)
    returnString = ""
    for matchNum, match in enumerate(matches, start=1):

        # print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            # print(match.group(groupNum))
            if match.group(groupNum) is None:
                returnString += " "
            returnString += match.group(groupNum)
    return returnString


regex = r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"

sentence = ""
with open("input.txt") as f:

    for line in f.readlines():
        sentence += trace(line, regex)

print(sentence)
print(len(sentence))