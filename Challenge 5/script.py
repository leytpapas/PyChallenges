import pickle
import collections

favorite_color = pickle.load(open("banner.p", "rb"))
favorite_color
speciallist = {}
# print(favorite_color)
for f in favorite_color:
    # print(f)
    line = ""
    for el in f:
        for i in range(0, el[1]):
            line += el[0]
    print(line)

