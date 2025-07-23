PG_UTILS = read-pg.py read-pg.sh

UTILS = $(PG_UTILS)

install:
	cp $(UTILS) ~/bin/
