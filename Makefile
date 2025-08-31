BASHRC = \
	core.rc \
	git.rc \
	linux.rc \
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
	if [ -d /boot/dtbs ]; then sudo mkdir -p /root/bin/ && sudo cp installkernel /root/bin/; fi
	mkdir -p ~/.bashrc.d/ ~/bin/
	cp vimrc ~/.vimrc
	cp $(BASHRC) ~/.bashrc.d/
	if ! grep -q 'bashrc.d' ~/.bashrc; then cat bashrc.d >> ~/.bashrc; fi
	cp $(UTILS) ~/bin/
