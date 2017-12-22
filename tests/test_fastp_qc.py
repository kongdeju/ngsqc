import sys
sys.path.append("../")

from ngsqc.fastqc.fastp import qc


fq = "data/test_R1.fq.gz"
prex = "22"

def test_qc():
    
    status = qc(fq,prex)

    assert status != None



