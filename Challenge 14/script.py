from PIL import Image
#...
import io

img = Image.open('wire.png')
pixRGB = img.load()
print(img.size)
listPixels = []
newImage = [[() for i in range(100)] for j in range(100)]
print(len(newImage), "x", len(newImage[0]))
# print(newImage)
index = 0


# im2 = Image.new(img.mode, (100,100))
# for y in range(100):
#     for i in range(100):
#     #     newImage[i][y] = pixRGB[i*y, 0]
#         im2.putpixel((i, y), pixRGB[(y*100)+i, 0])
#     # im2.paste(pixRGB[i*y, 0] for i in range(100))
# # im2.putdata(newImage)
# im2.save("bit.png")
#

im2 = Image.new(img.mode, (100, 100))
for y in range(100):
    for i in range(100):
    #     newImage[i][y] = pixRGB[i*y, 0]
        im2.putpixel((i, y), pixRGB[(y*100)+i, 0])
    # im2.paste(pixRGB[i*y, 0] for i in range(100))
# im2.putdata(newImage)
im2.save("bit.png")


# summ = 0
# for i,y in zip(range(100, 0, -2), range(0, 50)):  # 50 iterations -> 100*100
#     # im2.putpixel()
#     currsum = (i+i-1+i-1+i-2)
#     print(currsum)
#     summ += currsum
#     im2.putpixel((y, 0), pixRGB[i, 0])
#     # print(summ)
# im2.save("next.png")

# print("\n", summ) # =100*100
# remember: 100*100 = (100+99+99+98) + (...
