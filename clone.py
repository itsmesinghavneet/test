#Python Program to get the last commit.

import os
import sys
from subprocess import check_output

content = check_output(['git', 'rev-parse', '--short', 'HEAD'])  #This will store the output of the command to 'content'
wd = os.getcwd()
f=open("docs/image-version.md",'w')
f.write("image version: " + content)
f.close()






