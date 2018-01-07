from jinja2 import Template


def genArgs(report):
    pass


def render(template,args):
    fp = open(template)
    tem = fp.read()
    md = Template.render(tem,**args)

def main(report,template,out):
    
    args = genArgs(report)
    md = render(template,args)
    
    return md

    


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
