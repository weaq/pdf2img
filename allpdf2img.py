#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install pdf2image
# sudo apt-get purge build
# sudo apt-get update
# sudo apt-get install libpoppler-dev

# use
# convert pdf file in pdfs directory to png or jpg extension
# $ python allpdf2img.py -i pdfs -t png


import argparse
# arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--in directory", required=True,
    help="path of input file - pdf")
ap.add_argument("-t", "--to extension", required=True,
    help="output extension - png or jpg")
ap.add_argument("-d", "--dpi", nargs='?', type=int, default=1,
    help="dpi between dpi between 72-800 dpi")

args = vars(ap.parse_args())

pathInput = args["in directory"]
pathOutput = args["to extension"]
dpi = args["dpi"]

###########################

from pdf2image import convert_from_path
import os, glob
pathInput = pathInput + "/"
inputFile = "*.pdf"

if pathOutput == "png" or "jpg":
    fileExtension = pathOutput
else:
    quit()

pathOutput = pathOutput + "/"

# between 72 - 800 dpi
if dpi < 72:
    dpi = 72
elif dpi > 800:
    dpi = 800

# input dir not exist
if not os.path.isdir(pathInput):
    print("Not found DIR: " + pathInput)
    quit()

# output dir not exist
if not os.path.isdir(pathOutput):
    print("Make DIR: " + pathOutput)
    os.mkdir(pathOutput)

# full path for glob
paths = pathInput + inputFile

for pathFile in glob.glob(paths):
    print("input: " + pathFile)
    # only filename
    fileName = os.path.basename(pathFile)

    # convert
    print("convert: " + fileName)
    pages = convert_from_path(pathFile, dpi) # 350, 270

    i = 1

    # create output file
    for page in pages:

        if fileExtension == 'png':
            outputFile = pathOutput + fileName + "-p" + str(i) + ".png"
            page.save(outputFile, "PNG")
        elif fileExtension == 'jpg':
            outputFile = pathOutput + fileName + "-p" + str(i) + ".jpg"
            page.save(outputFile, "JPEG")

        print("save: " + outputFile)
        i = i+1
