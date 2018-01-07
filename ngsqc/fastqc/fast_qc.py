import os
from config import fastqc

from jbiot import log

def qc(fqs,prefix):

    out = "%s.fastqc" % prefix
    log.info("fastq file qc by `fastqc`",prefix) 
    cmd = "mkdir %s" % out
    log.run(cmd,prefix)
    for item in fqs:
        fq = item[0]
        prex = item[1]
        cmd = "%s -o %s %s " % (fastqc,out,fq)
        log.run(cmd,prefix)    

    return out
    
