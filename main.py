import pathlib

def loadImg():
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
            
loadImg()
