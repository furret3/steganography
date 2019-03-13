import pathlib
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
    f = open(data[1], "r")
    if f.mode == "r":
        textFile = f.read()
    binaryTextFile = ' '.join(format(x, 'b') for x in bytearray(textFile, encoding='ASCII'))
    return binaryTextFile

def imageToBinary():
    imgFile = Image.open(data[0], "r")
    grayScale = imgFile.convert("L")
    binaryImgFile = grayScale.point(lambda z: 0 if z<128 else 255, "1")
    binaryImgFile.save("binaryImg.png")

loadFile()
