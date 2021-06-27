from os import listdir
from os.path import isfile, join
from PIL import Image

# constants
# order: id, w, h
LINE_FORMAT = r"[url=https://futanaripalace.com/attachment.php?aid={id}][img={w}x{h}]https://futanaripalace.com/attachment.php?aid={id}[/img][/url]"


def generatePostUrls(folderPath, ids, longSide):
    # get all files in folder
    files = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
    files.sort()

    for i in range(len(files)):
        file = files[i]
        size = getScaledImageSize(file, longSide)
        print(f"{file}: {LINE_FORMAT.format(id=ids[i], w=size[0], h=size[1])}")


def getScaledImageSize(imagePath, longSide):
    '''
    Returns tuple (width, height) scaled to fit longSize
    '''
    im = Image.open(imagePath)
    isImageTall = im.size[0] < im.size[1]

    w = 0.
    h = 0.
    if isImageTall:
        ratio = im.size[0] / im.size[1]
        w = int(longSide * ratio)
        h = int(longSide)
    else:
        ratio = im.size[1] / im.size[2]
        w = int(longSide)
        h = int(longSide * ratio)

    return w, h
