
import config
from jbiot import log

report = "report"

class arranger:

    def __init__(self,prefix):
        self.prefix = prefix
        self.report = report
        cmd = "mkdir %s" % report        
        log.info(cmd,prefix)
        log.run(cmd,prefix)

    def arrange(self):
        self.arrFastqc()
        self.arrFastp()
        return report

    def arrFastqc(self):
        raw = self.prefix + ".fastqc"
        tgt = "%s/fastqc" % report
        cmd = "cp -r %s %s" % (raw,tgt)
        log.info(cmd,self.prefix)
        log.run(cmd,self.prefix)

    def arrFastp(self):
        raw = self.prefix + ".fastqInfo.tsv"
        tgt = "%s/fastqsInfo.tsv" % report
        cmd = "cp %s %s" % (raw,tgt)
        log.info(cmd,self.prefix)
        log.run(cmd,self.prefix)
        
