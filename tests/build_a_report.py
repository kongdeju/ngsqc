import os
import sys
from shutil import copytree,ignore_patterns,copyfile
mkdocs = "mkdocs"
mkdocs_template = "/home/testData/QCreport/"
destination = "QCreport"
copytree(mkdocs_template, destination, ignore=ignore_patterns('.git/'))
index = "index.md"
copyfile(index,"QCreport/docs/index.md")
os.chdir("QCreport/")
cmd = "%s build" % mkdocs
print cmd
os.system(cmd)
copytree("../report","site/report")
