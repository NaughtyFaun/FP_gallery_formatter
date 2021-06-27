from os import chdir
from os.path import isdir
from generators import generatePostUrls

IMG_LONG_SIDE = 200

# path to folder with images
PATH = r""

# fill it first
remoteIds = ["", "", "", "", ""]


def main(args):

    if len(args) == 0 and len(PATH) == 0:
        print("No input folder provided")
        return

    path = ""
    if len(PATH) == 0 and len(args) > 1:
        path = args[1]
    else:
        path = PATH

    if not isdir(path):
        print(f"Folder provided ({path}) is not a valid directory")
        return

    chdir(path)
    generatePostUrls(path, remoteIds, IMG_LONG_SIDE)
