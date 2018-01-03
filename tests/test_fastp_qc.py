import sys
sys.path.append("/lustre/users/lilin/test_ben/qc/ngsqc/ngsqc/fastqc")

from fastp import qc1
from FastQC import FastQC

fq = "/lustre/users/lilin/test_ben/data_test/fastq/ERR091571_1.fastq"
prex = "22"

#def test_qc():
    
#    status = qc(fq,prex)

#    assert status != None

test = FastQC(fq,prex)
test.fastp()
test.fastQc()
#qc1(fq,prex)

