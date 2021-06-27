from os import listdir, chdir
from os.path import isfile, join
from PIL import Image

# path to folder with images
path = r""
chdir(path)

# fill it first
ids = ["394666",
       "394667",
       "394668",
       "394669",
       "394670"]

# order: id, w, h
lineFormat = r"[url=https://futanaripalace.com/attachment.php?aid={id}][img={w}x{h}]https://futanaripalace.com/attachment.php?aid={id}[/img][/url]"
longSidePreview = 200

# get all files in folder
files = [f for f in listdir(path) if isfile(join(path, f))]
files.sort()

for i in range(len(files)):
    file = files[i]
    im = Image.open(file)
    isImageTall = im.size[0] < im.size[1]

    w = 0.
    h = 0.
    if isImageTall:
        ratio = im.size[0] / im.size[1]
        w = int(longSidePreview * ratio)
        h = int(longSidePreview)
    else:
        ratio = im.size[1] / im.size[2]
        w = int(longSidePreview)
        h = int(longSidePreview * ratio)

    print(f"{file}: {lineFormat.format(id = ids[i], w = w, h = h)}")