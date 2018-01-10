import sys
sys.path.append("../")
from ngsqc.reporter.reporter import report

reportDir = "report"
pref = "22"

def test_report():
    report(reportDir,pref)

if __name__ == "__main__":
	test_report()
