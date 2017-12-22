import os
from config import fastp

def qc(fq,prefix):

    html = prefix + ".html"

    cmd = "%s -Q -L -i %s -h %s " % (fastp,fq,html)

    print cmd

    status = os.system(cmd)

    if status :
        return 

    return html


    
