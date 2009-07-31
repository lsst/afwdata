# -*- python -*-
#
# Setup our environment
#
import glob, os
import lsst.SConsUtils as scons

env = scons.makeEnv("afwdata",
                    r"$HeadURL$",
                    [])

# files with the following suffixes are considered data files
DataFileSuffixSet = set((".fits", ".dat", ".txt"))

def getInstallList(basePath):
    """Make an install list for all data files in or below the specified base path, plus ups table files.
    
    Data files have suffixes in DataFileSuffixSet
    
    Excludes invisible files and files in invisible directories.
    """
    installList = [env.InstallEups(env['prefix'] + "/ups", glob.glob("ups/*.table"))]
    isBaseDir = True
    for dirPath, dirNameList, fileNameList in os.walk(basePath):
        dataFileList = (os.path.join(dirPath, fn) for fn in fileNameList if \
            ((fn[0] != ".") and (os.path.splitext(fn)[1] in DataFileSuffixSet)))
        installList.append(env.Install(env['prefix'] + dirPath[1:], list(dataFileList)))

        newDirNameList = (dn for dn in dirNameList if dn[0] != ".")
        if isBaseDir:
            newDirNameList = (dn for dn in newDirNameList if dn != "ups")
        if newDirNameList != dirNameList:
            dirNameList[:] = newDirNameList
        isBaseDir = True
    return installList

Alias("install", getInstallList("."))

scons.CleanTree(r"*~ core *.so *.os *.o")

env.Declare()

env.Help("""
Test data for lsst/afw
""")
