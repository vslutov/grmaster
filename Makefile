SRC_DIR = grmaster

test :
	py.test $(SRC_DIR)

lint :
	pylint $(SRC_DIR)

pep257 :
	pep257 $(SRC_DIR)

all : test lint pep257
