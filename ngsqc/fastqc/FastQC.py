import os
import fast_qc 
import fastp 

class FastQC:
    '''
    init the FastQC class
        
    Args:
        fq (str) : this is the input fastq file
        prefix (str) : the output prefix
        
    '''
    
    def __init__(self,fqs,prefix):
        
        self.fqs = fqs
        self.prex = prefix
        

    def byfastqc(self):
    	fast_qc.qc(self.fqs,self.prex)  

    def byfastp(self):
	    fastp.qc(self.fqs,self.prex)






