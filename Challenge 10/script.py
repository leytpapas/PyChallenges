import re

def lookNsaySequence(test_str):
    regex = r"(\d)\1*"
    matches = re.finditer(regex, test_str, re.MULTILINE)
    newSequence = ""
    for matchNum, match in enumerate(matches, start=1):
        
        # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        newSequence+= str(match.end()-match.start())+str(match.group()[0])
        # for groupNum in range(0, len(match.groups())):
        #     groupNum = groupNum + 1
        #     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    return newSequence

newS="1"
for i in range(0,30):
    newS = lookNsaySequence(newS)
print(len(newS))
