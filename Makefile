PG_UTILS = read-pg.py read-pg.sh

UTILS = \
	compiled-kernels \
	$(PG_UTILS) \
	rdp-tunnel.sh \
	remove-compiled-kernel \

all:
	echo "Try make install"

install:
	cp $(UTILS) ~/bin/
