#Python Program to get the last commit of one repository to a .txt file and upload it to another directory 

import os
import sys

# New Import
#Here, define the repo from where you want to take the last commit.
#os.chdir(path) 
from subprocess import check_output
content = check_output(["git", "log", "-p", "-1"])  #This will store the output of the command to 'content'
wd = os.getcwd()
#os.chdir("/docs") # location where the txt file needs to be saved
f=open("wd/docs/image-version.md",'w')
f.write(content)
f.close()






