#!/usr/bin/env python
#coding=utf-8
from jinja2 import Template
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
class Argsor:

    def __init__(self,report):
        self.dir = report
        self.args = {}
        self.per_base_quality() 
   
    def per_base_quality(self):
        for root,dirs,files in os.walk(report):
            for file in files:
                absfile = os.path.join(root,file)
                if file == "per_base_quality.png":
                    self.args["per_base_quality"] = absfile
                    return

    
def render(template,args):
    fp = open(template)
    tem = Template(fp.read())
    md = tem.render(**args)
    return md
def main(report,template,out):
    argsor = Argsor(report)
    args = argsor.args
    md = render(template,args)

    fp = open(out,"w")
    fp.write(md)
    fp.close()

    
if __name__ == "__main__":

    usage='''
Usage:
  render.py -d <reportDir> -t <md> -o <md>
  render.py -h | --help

Options:
    -d <reportDir> --dir=<reportDir>    report directory
    -t <md> --template=<md>             markdown template
    -o <md> --out=<md>                  markdown rendered

    '''
    from docopt import docopt
    args = docopt(usage)
    report = args["--dir"]
    templ = args["--template"]
    out = args["--out"]
    main(report,templ,out)
