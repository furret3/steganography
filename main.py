import pathlib, binascii
from textwrap import wrap
from PIL import Image

def loadFile():
    global data
    x = 0
    data = []
    subs = ["image", "text file"]
    exts = [".jpg", ".txt"]
    while x < 2:
        check = pathlib.Path(input(f"Enter {subs[x]} name: ")).with_suffix(exts[x]) # To be fixed
        if check.is_file():
            data.insert(x, check)
            if(x < len(subs)):
                x+=1
        else:
            print("Couldn't find the file. Try again.")
            x = 0

def stringToBinary():
    global binaryTextFile
    f = open(data[1], "r")
    if f.mode == "r":
        textFile = f.read()
    binaryTextFile = wrap(' '.join(format(x, 'b') for x in bytearray(textFile, encoding='ASCII')), 2)

def imageToBinary():
    global bin_list
    imgFile = open(data[0], "rb")
    imgData = imgFile.read()
    imgFile.close()

    hex_str = str(binascii.hexlify(imgData))
    hex_list = []
    bin_list = []
    for i in range(2, len(hex_str)-1, 2):
        hex = hex_str[i] + hex_str[i+1]
        hex_list.append(hex)
        bin_list.append(bin(int(hex, 16))[2:])
    
    bin_list = wrap(''.join(bin_list), 8)

def enc():
    global result
    x = 0
    result = []
    result = bin_list
    for i in range(len(binaryTextFile)):
        imgByte = str(bin_list[x])
        textBits = str(binaryTextFile[x])
        newImgByte = imgByte[:-2] + textBits
        result.insert(x, newImgByte)
        if(x < len(binaryTextFile)):
            x+=1
        else:
            break
    print(result)

loadFile()
stringToBinary()
imageToBinary()
enc()