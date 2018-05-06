from PIL import Image
import math
import sys

## ===== ENCODE =====================================

def encode(e_img):
    print("encode")

## ===== DECODE =====================================
def decode(d_img):
    imgToDecode = Image.open(d_img)
    # imgToDecode.show();

    # Get width and height of image
    width, height = imgToDecode.size

    # Get length of data stored in the last 11 pixels of image to decode
    pix = imgToDecode.load()
    msg_length = ''
    last_eleventh = 11
    w = width-1
    h = height-1

    for i in range (0, last_eleventh):
        # get the R,G,B pixel values from image to be decoded
        r, g, b = pix[w, h]
        if w == 0:
            w = width
            h -= 1
        msg_length += str(bin(r))[-1]
        msg_length += str(bin(g))[-1]
        msg_length += str(bin(b))[-1]
        w -= 1

    # Keep first 32 bits and cast it to an integer
    msg_length = msg_length[:32]
    msg_length = int(msg_length, 2)

    # Read the hidden text in the image to be decoded starting from 12th-last pixel
    pix_value = math.floor(msg_length/3)
    msg_decoded = ''
    w = width - 12
    for i in range (0, int(pix_value)):
        # get the R,G,B values from image to be decoded
        r, g, b = pix[w, h]
        if w == 0:
            w = width
            h -= 1
        msg_decoded += str(bin(r))[-1]
        msg_decoded += str(bin(g))[-1]
        msg_decoded += str(bin(b))[-1]
        w -= 1

    # Print the hidden text and the length of text
    hidden_text = ''
    for i in range(0, len(msg_decoded), 8):
        hidden_text = hidden_text + ''.join(chr(int(msg_decoded[i:i+8],2)))

    print("size of message is: ", msg_length)
    print("decoded message is: ", hidden_text)

## ===== MENU =======================================
def main():

    print("type 'e' for encode\n");
    print("type 'd' for decode\n");
    print("type 'h' for help\n");

    choice = raw_input("What would you like to do?\n")

    if choice=='e':
        e_img = raw_input("Type in the name of image to be encoded")
        encode(e_img)

    elif choice=='d':
        d_img = raw_input("Type in the name of image to be decoded\n")
        decode(d_img)

    elif choice=='h':
        print("to encode: TBD\n");
        print("to decode: type in the image name. For example, testImage.png\n")

    else:
        print("error");


if __name__ == "__main__":
    main()
