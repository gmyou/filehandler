# -*- coding:utf-8 -*-
import os, shutil

path="/Volumes/DATA/Dropbox/Audio/FavorateSong/"  # insert the path to the directory of interest here

def findRename(source):
    destination = source.replace(" ", "")
    destination = destination.replace("`", "")
    destination = destination.replace("'", "")
    destination = destination.replace("(", "_")
    destination = destination.replace(")", "_")
    return destination

def findMusic(dir):
    dirList=os.listdir(dir)
    
    f = file("fileRename.sh", "a")
    for fname in dirList:
        if fname.endswith("mp3"):
            print "\t"+fname
            """
            refname = findRename(fname)
            print("\t"+str(refname))

            if (fname != refname):
                print "\t"+"\t"+dir+fname
                print "\t"+"\t"+dir+refname
                cmd = "mv " + dir+fname + " " + dir+refname
                f.write(cmd+"\n")
            """
    f.close()
            
def findCD():
    dirList=os.listdir(path)
    for fname in dirList:
        if fname.startswith("CD"):
            print fname
            findMusic(path+fname)


f = file("fileRename.sh", "w")
f.write("")
f.close()
findCD()