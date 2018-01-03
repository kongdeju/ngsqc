import os
from config import fastqc

def qc2(fq,prefix):

    out = "./" 

    cmd = "%s -t 6 -o %s %s " % (fastqc,out,fq)

    print cmd

    status = os.system(cmd)

    if status :
        return 

    return out


    
