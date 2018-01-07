import sys
sys.path.append("../")

from ngsqc.fastqc.fast_qc import qc

fqs = [
["data/test_R1.fq.gz","test_R1"],
["data/test_R2.fq.gz","test_R2"],
]

prex = "22"

def test_qc1():
    qc(fqs,prex)




if __name__ == "__main__":
    test_qc1()



