from lxml import html
import requests

import re
import sys
import urllib.request
import time

def downloadFiles(files):
    destFolder= input("Where do you want to put the files?: ")
    destFolder = "C:/temp"
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    backoff = 5

    #Remove each file upon successfull deletion. Repeat until all files are removed
    while files:
        for file in files:
            try:
                print(file)
                dest = destFolder + '/' + file.replace('/', '_')
                urllib.request.urlretrieve(root + file, dest)
                files.remove(file)
            except Exception as err:
                print(str(err))
                if err.code == 404:
                    print("Page not found!")
                elif err.code == 403:
                    print("Access Denied!")
                else:
                    print("Something went wrong")
                    time.sleep(backoff)
                    backoff += backoff

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

