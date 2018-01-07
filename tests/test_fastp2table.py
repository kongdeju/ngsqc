import sys
sys.path.append("../")

from ngsqc.fastqc.fastp2table import fastp2table

jsons = [
"data/test_R1.json",
"data/test_R2.json",
]


def test_fastp2table():
    fastp2table(jsons)




if __name__ == "__main__":
    test_fastp2table()



