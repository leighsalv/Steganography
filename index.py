from PIL import Image

def encode():
    print("encode")

def decode(path):
    imgDecode = Image.open(path)
    imgDecode.show()

## === MENU ================================
def main():

    print("type 'e' for encode\n");
    print("type 'd' for decode\n");

    choice = raw_input("What would you like to do?\n")

    if choice=='e':
        encode()

    elif choice=='d':
        path = raw_input("Type in the filepath of image\n")
        decode(path)

    else:
        print("error");


if __name__ == "__main__":
    main()
