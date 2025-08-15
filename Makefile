BASHRC = \
	core.rc \
	git.rc \
	pico.rc \

PG_UTILS = _pg-read.py pg-read.sh

UTILS = \
	cmake-debug \
	compiled-kernels \
	$(PG_UTILS) \
	rdp-tunnel.sh \
	remove-compiled-kernel \

all:
	echo "Try make install"

install:
	cp vimrc ~/.vimrc
	mkdir -p ~/.bashrc.d/
	cp $(BASHRC) ~/.bashrc.d/
	if ! grep -q 'bashrc.d' ~/.bashrc; then cat bashrc.d >> ~/.bashrc; fi
	cp $(UTILS) ~/bin/
