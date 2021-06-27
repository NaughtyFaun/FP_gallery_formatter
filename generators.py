import string
from os import listdir
from os.path import isfile, join
from PIL import Image
import requests

# constants
# order: id, w, h
LINE_TEMPLATE         = r"[url=https://futanaripalace.com/attachment.php?aid={id}][img={w}x{h}]https://futanaripalace.com/attachment.php?aid={id}[/img][/url]"
FP_THUMB_URL_TEMPLATE = r"https://futanaripalace.com/attachment.php?thumbnail="
FP_ATCH_URL_TEMPLATE  = r"https://futanaripalace.com/attachment.php?aid="


def generatePostUrlsByFolderFiles(folderPath, ids, longSide):
    # get all files in folder
    files = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
    files.sort()

    posts = []
    for i in range(len(files)):
        file = files[i]
        image = Image.open(file)
        size = getScaledImageSize(image, longSide)
        posts.append(LINE_TEMPLATE.format(id=ids[i], w=size[0], h=size[1]))
        print(f"{file}: {posts[i]}")

    lump = ""
    for i in range(len(files)):
        lump += posts[i] + " "
    print(f"One piece: {lump}")


def generatePostUrlsByFpThumbUrls(urls, longSide):

    ids = [f.replace(FP_THUMB_URL_TEMPLATE, "").strip() for f in urls]
    print(ids)

    # payload
    forum = "https://futanaripalace.com/"

    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'username': 'Naughty Faun', 'password': '2PJqgMNr', 'redirect': 'index.php', 'sid': '', 'login': 'Login'}
    session = requests.Session()

    r = session.post(forum + "index.php", headers=headers, data=payload)
    print(r.text)

    return

    for i in range(len(urls)):
        url = FP_ATCH_URL_TEMPLATE + ids[i]

        print(f"{ids[i]} {url}")
        img = session.get(url, stream=True).raw
        image = Image.open(img)
        print(ids[i])
        size = getScaledImageSize(image, longSide)
        print(f"{ids[i]}: {LINE_TEMPLATE.format(id=ids[i], w=size[0], h=size[1])}")


def getScaledImageSize(image, longSide):
    '''
    Returns tuple (width, height) scaled to fit longSize
    '''

    w = 0.
    h = 0.
    ratio = image.size[0] / image.size[1]
    w = int(longSide * ratio)
    h = int(longSide)

    return w, h
