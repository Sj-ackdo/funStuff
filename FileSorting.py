import argparse
import os
import shutil

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--verbose", "-v", help="increase output verbosity",
                    action="store_true")
parser.add_argument("path", type=str, help="input directory")
parser.add_argument("outputDir", type=str, help="output directory")
parser.add_argument("num", type=str, help="Extension type: 1. jpg - 2. png -  3. jpg & png")
args = parser.parse_args()

def fileExtension(num):
    switch={
      '1':".jpg",
      '2':".png",
      '3':"[\".jpg\", \".png\"]",
      }
    return switch.get(num,"Invalid input")

class checkFile:
    def __init__(self, path):
        self.path = path
         
    def checkFileExtTypeList(self, extList):
        for filename in os.listdir(self.path):
            if os.path.splitext(filename)[1] in extList:
                for filename in os.listdir(self.path):
                    if os.path.splitext(filename)[1] in extList:
                        file_size = os.path.getsize(self.path + "/" + filename)
                        file_size = file_size % 1024^2
                        if args.verbose:
                            print("\n" + filename)
                            print("File Size is :", file_size, "Mib")
                            print("Sorting and Copying Succeeded...\n")
                        if file_size < 512:
                            if not os.path.exists(outputDir + "/VerySmallPictures"):
                                os.mkdir(outputDir + "/VerySmallPictures")
                            shutil.copy(self.path + "/" + filename, outputDir + "/VerySmallPictures")
                        elif file_size > 512 and file_size < 1024:
                            if not os.path.exists(outputDir + "/SmallPictures"):
                                os.mkdir(outputDir + "/SmallPictures")
                            shutil.copy(self.path + "/" + filename, outputDir + "/SmallPictures")
                        elif file_size > 1024 and file_size < 1024^2:
                            if not os.path.exists(outputDir + "/MediumPictures"):
                                os.mkdir(outputDir + "/MediumPictures")
                            shutil.copy(self.path + "/" + filename, outputDir + "/MediumPictures")
                        elif file_size > 1024^2 < 1024^3:
                            if not os.path.exists(outputDir + "/LargePictures"):
                                os.mkdir(outputDir + "/LargePictures")
                            shutil.copy(self.path + "/" + filename, outputDir + "/LargePictures")
                        elif file_size > 1024^3:
                            if not os.path.exists(outputDir + "/VeryLargePictures"):
                                os.mkdir(outputDir + "/VeryLargePictures")
                            shutil.copy(self.path + "/" + filename, outputDir + "/VeryLargePictures")
            else:
                if args.verbose:
                    print(filename)
                    print("Not a valid file extension...")
        else:
            print("\nCompleted...\n")




print(" _____ _ _        ____             _   _             ")
print("|  ___(_) | ___   / ___|  ___  _ __| |_(_)_ __   __ _ ")
print("| |_  | | |/ _ \  \___ \ / _ \| '__| __| | '_ \ / _` |")
print("|  _| | | |  __/   ___) | (_) | |  | |_| | | | | (_| |")
print("|_|   |_|_|\___|  |____/ \___/|_|   \__|_|_| |_|\__, |")
print(" Sorts files!  Sj-ackdo                         |___/ \n")

if args.path and args.outputDir and args.num:
    outputDir = args.outputDir
    checkFile(args.path).checkFileExtTypeList(fileExtension(args.num))
    exit()
else:           
    path = input("Type Path:\n")
    num = input("Available file extensions:\n1. jpg\n2. png\n3. jpg & png\n") 
    outputDir = input("Where do you want to copy the files to?\n")
    checkFile(path).checkFileExtTypeList(fileExtension(num))
