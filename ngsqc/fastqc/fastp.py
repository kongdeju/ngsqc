import os
from config import fastp
from jbiot import log

sdir = os.path.dirname(os.path.abspath(__file__))
fp2tb = os.path.join(sdir,"fastp2table.py")

def qc(fqs,prefix):

    out = "%s.fastp" % prefix
    log.info("fastq file qc by `fastp`",prefix) 
    #cmd = "mkdir %s" % out
    #log.run(cmd,prefix)
    jsons = []    
    for item in fqs:
        fq = item[0]
        prex = item[1]
        html =  prex + ".html"
        json =  prex + ".json"
        jsons.append(json)
        cmd = "%s -Q -L -i %s -h %s -j %s " % (fastp,fq,html,json)
        log.run(cmd,prefix)    
    jstr = " ".join(jsons)

    cmd = "python %s %s" % (fp2tb,jstr)
    log.run(cmd,prefix)

    return out


    
