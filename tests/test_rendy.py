import os

def test_render():
	cmd = "python ../ngsqc/reporter/render.py -d report -t data/index_template.md -o index.md"
	print cmd
	#os.system(cmd)


if __name__ == "__main__":
	test_render()
