# Import the os module, for the os.walk function
import os

fileName = []
directName = []
# Set the directory you want to start from
rootDir = 'C:\\Users\\Example_user'
fhandle = open ('Output.csv', 'w')



def fileSearch (starts = '', ends = ''):
    for dirName, subdirList, fileList in os.walk(rootDir):
        # Removing the directory from printout
        # print('Found directory: %s' % dirName)

        for fname in fileList:
            # Set the file names you are looking for use startswith for name of file and endswith for file type
            if fname.lower().startswith((starts)) & fname.lower().endswith((ends)) :
                print('%s' % fname)
                # Sticking the directory name and file name into lists so they are callable later and writing to the Output.csv
                directName.append(dirName)
                fileName.append (fname)
                fhandle.write(fname +'; ' + dirName + '\n')
                 
                
                
# Here an simple example usage that finds files that start with cat and are in the format jpeg  
fileSearch('cat', 'jpg')


## Examples:
# Finds all jpegs
# fileSearch ('','jpg' )

## Finds every file named joe, regardless of file type 
# fileSearch ('joe', '')



fhandle.close()
