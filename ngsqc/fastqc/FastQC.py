import os
from fast_qc import qc2
from fastp import qc1

class FastQC:
    
    def __init__(self,fq,prefix):
        '''init the FastQC class
        
        Args:
            fq (str) : this is the input fastq file
            prefix (str) : the output prefix
        
        '''
        self.fq1 = fq
        self.prex = prefix
        

    def fastQc(self):
    	qc2(self.fq1,self.prex)  

    def fastp(self):
	    qc1(self.fq1,self.prex)




