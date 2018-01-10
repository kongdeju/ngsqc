from config import mkdocs,mkdocs_template
import os
from jbiot import log
import sys

renderScript = os.path.join(os.path.dirname(os.path.abspath(__file__)),"render.py")
mdtemplate = os.path.join(os.path.dirname(os.path.abspath(__file__)),"template.md")

def report(reportDir,prefix):
    
    curdir = os.getcwd()
    
    # render template
    md = prefix + ".md"    
    cmd = "python %s -d %s -t %s -o %s" % (renderScript,reportDir,mdtemplate,md)
    log.info("generate report",prefix)
    log.run(cmd,prefix)

    # mkdocs build html
    log.info("cp mkdocs template and index template",prefix)
    target = "QC_REPORT"
    cmd = "cp -r %s %s" % (mkdocs_template,target)
    log.run(cmd,prefix)
    idx = os.path.join(target,"docs/index.md")
    cmd = "cp %s %s" % (md,idx)
    log.run(cmd,prefix)

    cmd = "cd %s" % target
    log.info(cmd,prefix)
    log.run(cmd,prefix)
    
    cmd = "%s build" % mkdocs
    log.info(cmd,prefix)
    log.run(cmd,prefix)
    
    
    cmd = "cd %s" % curdir
    log.info(cmd,prefix)
    log.run(cmd,prefix)

    site = os.path.join(target,"site")
    cmd = "cp -r %s %s" % (reportDir,site)
    log.info(cmd,prefix)
    log.run(cmd,prefix)

    rawsite = os.path.join(target,"site")
    newsite = "HTML_Report"
    
    cmd = "cp -r %s %s" % (rawsite,newsite)
    log.info(cmd,prefix)
    log.run(cmd,prefix)

    out = prefix + ".out.tgz"
    cmd = "tar cvzf %s %s "  % (out,newsite)  
    log.info("oh yeah!!!",prefix)
    log.run(cmd,prefix)

    return 


    
