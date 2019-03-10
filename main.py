import pathlib

def loadImg():
    global data
    data = []
    subs = ["image", "text file"]
    exts = [".png", ".txt"]
    x = 0
    for i in range(len(subs)):
        data.insert(x, pathlib.Path(input(f"Enter {subs[x]} name: ")).with_suffix(exts[x]))
        if data[x].is_file():
            if(x < len(subs)):
                x+=1
        else:
            print("Couldn't find the file.")
            pass

def stringToBinary():
    f = open(data[1], "r")
    if f.mode == "r":
        textFile = f.read()
    print(' '.join(format(x, 'b') for x in bytearray(textFile, encoding='ASCII')))

loadImg()
stringToBinary()
