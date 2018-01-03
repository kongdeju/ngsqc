import os
#from config import fastp

def qc1(fq,prefix):

    html = prefix + ".html"

    cmd = "fastp -Q -L -w 6 -i %s -h %s " % (fq,html)

    print cmd

    status = os.system(cmd)

    if status :
        return 

    return html


    
