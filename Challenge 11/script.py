from PIL import Image
#...
import io

img = Image.open('cave.jpg')
pixRGB = img.load()
print(img.size)
listPixels = []

for y in range(0,img.size[1],2):
    for i in range(0,img.size[0],2):
        pixRGB[i+1,y] = (0,0,0,255)
        pixRGB[i,y+1] = (0,0,0,255)
print(type(pixRGB))

img.save('myfiletest3.jpg')


# image = Image.open(io.BytesIO(pixRGB))
# image = Image.frombytes('RGBA', img.size, pixRGB, 'raw')
# image.show()