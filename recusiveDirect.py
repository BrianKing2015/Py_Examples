# Import the os module, for the os.walk function
import os

fileName = []
directName = []
# Set the directory you want to start from
rootDir = 'C:\\Users\\briank\\Pictures'
fhandle = open ('Output.csv', 'w')



def fileSearch (starts = '', ends = ''):
    for dirName, subdirList, fileList in os.walk(rootDir):
        # Removing the directory from printout
        # print('Found directory: %s' % dirName)

        # Skipping the STAGE folder to only display 1 version
        subdirList[:] = [d for d in subdirList if d not in ['STAGE']]
        for fname in fileList:
            # Set the file types you are looking for use startswith for name of file and endswith for file type
            if fname.lower().startswith((starts)) & fname.lower().endswith((ends)) :
                print('%s' % fname)
                # Sticking the directory name and file name into lists so they are callable later and writing to the Output.csv
                directName.append(dirName)
                fileName.append (fname)
                fhandle.write(fname +'; ' + dirName + '\n')
                 
                
                
# Here an example usage of the function above. 
fileSearch('cat', 'jpg')


# Example
# fileSearch ('ghost','vxmechanism' )
# fileSearch ('p - ', 'vxmechanism')
# fileSearch ('g - ', 'vxmechanism')
# fileSearch ('l - ', 'vxmechanism')
# fileSearch ('h - ', 'vxmechanism')




fhandle.close()
