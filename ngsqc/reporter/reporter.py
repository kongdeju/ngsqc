import config
import os
from jbiot import log

renderScript = (os.path.dirname(os.path.abspath(__file__)),"render.py")
mdtemplate = (os.path.dirname(os.path.abspath(__file__)),"template.md")

def report(reportDir,prefix):

    md = prefix + ".md"    
    cmd = "python %s -d %s -t %s -o %s" % (renderScript,mdtemplate,md)
    log.info("generate report",prefix)
    log.run(cmd,prefix)

    return md


    
