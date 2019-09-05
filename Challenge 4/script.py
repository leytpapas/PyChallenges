import http.client
import re
import time
regex="and the next nothing is (\d+)$"

def trace(test_str):

    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):

        # print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            # print(match.group(groupNum))
            return match.group(groupNum)



connection = http.client.HTTPConnection('www.pythonchallenge.com', 80, timeout=10)
#extra = "12345" # starting from 12345 we find out that in 16044 it says 'divide by 2 and keep going'.In the next time our program stops it says 'peak.html' which is the solution
extra = str(16044/2)
for i in range(0, 401):
    connection.request("GET", "/pc/def/linkedlist.php?nothing=" + extra)
    response = connection.getresponse()
    # print(response.getheaders())
    for line in response.readlines():
        line = line.decode("utf-8")
        extra = trace(line)
        print(i, ":", extra)
        # print(str(response.readlines()))
    # time.sleep(1)



connection.close()