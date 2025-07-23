PG_UTILS = read-pg.py read-pg.sh

UTILS = $(PG_UTILS)

all:
	echo "Try make install"

install:
	cp $(UTILS) ~/bin/
