#!/usr/bin/env python
""" Collection of helper functions for manipulating Project Gutenberg zip files

This is a utility file for finding and extracting specific files from a zip.
After extracting them there is a parser for finding the name of the text using regex.

The structure is broken into several functions:
- fileSearch:
- checkZip:
- findName:
- 

"""

import re
import pandas as pd
import os

def fileSearch (starts = '', ends = '', rootDir = '/media/brian/New Volume/Gutenberg/2006/rawText'):
    sTarget = []
    for dirName, subdirList, fileList in os.walk(rootDir):

        for fname in fileList:
            if fname.lower().startswith((starts)) & fname.lower().endswith((ends)) :
                sTarget.append (os.path.join(dirName,fname))
    return sTarget

def checkZip(target = '', dump = '', fileType = '.txt'):
    """

    """
    output = []
    zf = zipfile.ZipFile(target, 'r')
    contents = zf.namelist()
    for i in contents:
        if i.endswith(fileType):
            zf.extract(i, path = dump)
            output.append(i)

    return output

def findName (bookTarget):
    with open (bookTarget, 'r', errors = "surrogateescape") as f:
        book = f.read()
    book = ''.join([x for x in book if ord(x) < 128])
    reg = re.compile(r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK")
    reg2 = re.compile(r"\s\*\*\*\n")
    if reg.search(book) != None:
        targetStart = reg.search(book).span()[1]
    else:
        targetStart = None
    if reg2.search(book) != None:
        targetEnd = reg2.search(book).span()[0]
    else:
        targetEnd = None
        
    if targetStart != None:
        targetName = book[targetStart: targetEnd]
    else:
        targetName = 'Not Available'
    return targetName

#thing = targetStart.span()[1]
#thing2 = targetEnd.span()[0]
#print (book [targetStart: targetEnd])
#print (book[535:563])


thing = fileSearch ('','-8.txt', rootDir = 'D:\\Gutenberg\\2006\\rawText\\')

names = []

for i in thing:
    names.append(findName(i))