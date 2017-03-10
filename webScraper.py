from lxml import html
import requests

import re
import sys
import urllib.request

def downloadFiles(files):
    downloadDest = input("Where do you want to put the files?: ")
    downloadDest = "C:/temp"

    try:
        testfile = urllib.request.urlopen(root + files[0])
        print(files[0])
        print(testfile.read())

        files[0] = files[0].replace('/', '_')
        saveFile = open(downloadDest + "/" + files[0], 'w')
        saveFile.write(str(testfile.read()))
        hm = testfile.read()
        saveFile.close()
    except Exception as e:
        print(str(e))

def getLinks(root, ext):
    # Get html tree
    page = requests.get(root)
    tree = html.fromstring(page.content)

    print(tree)

    # Get links of the appropriate extension
    files = tree.xpath("//a/@href")
    extLen = 0 - len(ext)
    extFiles = []
    for file in files:
        if (file[extLen:] == ext):
            extFiles.append(file)
    return extFiles

#Get site and extension type to download
#link = input("WebSite Link: ")
#ext = input("Extension to Download: ")

root = "https://www.cs.toronto.edu/~gfb/csc324/2017W/"
ext = ".rkt"

files = getLinks(root, ext)
downloadFiles(files)

