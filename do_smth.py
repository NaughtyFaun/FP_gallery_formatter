from os import chdir
from os.path import isdir, isfile
from generators import generatePostUrlsByFolderFiles, generatePostUrlsByFpThumbUrls

IMG_LONG_SIDE = 200

# path to folder with images
PATH = r""

# fill it first
remoteIds = ["392476", "392477", "392478"]


def main(args):

    if len(args) == 0 and len(PATH) == 0:
        print("No input folder provided")
        return

    path = ""
    if len(PATH) == 0 and len(args) > 1:
        path = args[1]
    else:
        path = PATH

    if isdir(path):
        print(f"Generating urls by FOLDER FILES at path {path}\n")
        chdir(path)
        generatePostUrlsByFolderFiles(path, remoteIds, IMG_LONG_SIDE)
        return

    if isfile(path):
        print(f"Generating urls by FP thumbnail list at path {path}\n")
        file1 = open(path, 'r')
        urls = file1.readlines()
        generatePostUrlsByFpThumbUrls(urls, IMG_LONG_SIDE)
        return

    print(f"Something is wrong with the path \"{path}\". Doing nothing.")



