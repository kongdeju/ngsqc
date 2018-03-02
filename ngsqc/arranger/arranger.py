
from jbiot.logrun import log

report = "report"



class arranger:
    """
    Here is some other description...
    ===================================
    Args:
        prefix (dict): some description of this dict
                {
                "key1": "...."
                "key2": "..."
                }

    Returns:
        dict : some description of this dict

    """


    def __init__(self,prefix):

        self.prefix = prefix
        self.report = prefix + "." + report
        cmd = "mkdir %s" % self.report        
        log.info(cmd,prefix)
        log.run(cmd,prefix)

    def arrange(self):
        self.arrFastqc()
        self.arrFastp()
        return self.report

    def arrFastqc(self):
        raw = self.prefix + ".fastqc"
        tgt = "%s/fastqc" % self.report
        cmd = "cp -r %s %s" % (raw,tgt)
        log.info(cmd,self.prefix)
        log.run(cmd,self.prefix)

    def arrFastp(self):
        raw = self.prefix + ".fastqInfo.xls"
        tgt = "%s/fastqsInfo.xls" % self.report
        cmd = "cp %s %s" % (raw,tgt)
        log.info(cmd,self.prefix)
        log.run(cmd,self.prefix)
        
