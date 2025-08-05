PG_UTILS = read-pg.py read-pg.sh

UTILS = $(PG_UTILS) \
	rdp-tunnel.sh

all:
	echo "Try make install"

install:
	cp $(UTILS) ~/bin/
