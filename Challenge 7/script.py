from PIL import Image
#...


img = Image.open('oxygen.png')
pixRGB = img.load()
print(img.size)
listPixels = []

for y in range(43,44):  #(img.size[1]):
    line = []
    for x in range(0,img.size[0],7):
        if pixRGB[x,y][0] == pixRGB[x,y][1] and pixRGB[x,y][1] == pixRGB[x,y][2]:
            line.append(pixRGB[x,y])
    if line != []:
        listPixels.append(line)
        
output = ""
for l in listPixels:
    for kapa in l:
        output+= ((chr(kapa[0])))
print(output)

newstr = [105, 110, 116, 101, 103, 114, 105, 116, 121]
newstr = [chr(x) for x in newstr]
print(newstr)