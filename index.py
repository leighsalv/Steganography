from PIL import Image

img = Image.open("pup.jpeg")
imgPixel = img.load()
rgb_img = img.convert('RGB')
width, height = img.size

hidden_text = "I am the secret message"
hidden_text_size = len(hidden_text)
hidden_text_binary = (bin(hidden_text_size))
print(hidden_text_binary)

length_start_pixel = 0
text_start_pixel = 11

# Write length of hidden text in the first 11 pixels
s = ('{0:011b}'.format(hidden_text_size))
#print(hidden_text_binary) #23    00000010111
counter = 0
x = 10111
s = 1 # shift hidden_text_binary to 1 right
red_channel = img.split()[0]
green_channel = img.split()[1]
blue_channel = img.split()[2]
val_channel = 1

r=''.join(map(str, hidden_text_binary))

for row in range ((width-11),width):
    color = tuple(imgPixel[row,height-1])
    r,g,b = color

    print(r,g,b)
    print(bin(r))
    print(bin(g))
    print(bin(b))

    if(counter == 0)
        b |= hm
        print("--")
        print(bin(r))
        print("\n")
        print(b_color)


# print(img.show())
# (x >> 1) % 2
# (x >> 2) % 2
# (x >> 3) % 2
# (x >> 4) % 2
# (x >> 5) % 2
# (x >> 6) % 2
# (x >> 7) % 2
# (x >> 8) % 2
# (x >> 9) % 2
# (x >> 10) % 2
# (x >> 11) % 2


# print(img.show())

    # if start < len(hidden_text_binary)
    #     color = tuple(imgPixel[row,col-1])
    #     r,g,b = color
    #     b >> 1
    #     b << 1





#Write text from right-bottom after last 11 bits
# for row in range(height):
#     for col in range(width-11):
#         imgPix = img.getpixel(col,row)
#         pixR = imgPix.getRed()
#         # print(row,col)

# print "Size: "
# print(img.format, img.size)
# print(img.show())
