from lxml import html
import requests

import re
import sys
import urllib.request

def downloadFiles(files):
    destFolder= input("Where do you want to put the files?: ")
    destFolder = "C:/temp"

    try:
        dest = destFolder + '/' + files[0].replace('/', '_')
        urllib.request.urlretrieve(root + files[0], dest)
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

