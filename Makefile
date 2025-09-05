BASHRC = \
	core.rc \
	git.rc \
	linux.rc \
	pico.rc \

DRACUT = \
	50-slim7x.conf \
	51-usb-storage.conf \

PG_UTILS = _pg-read.py pg-read.sh

UTILS = \
	cmake-debug \
	compiled-kernels \
	kernel-status.py \
	$(PG_UTILS) \
	rdp-tunnel.sh \
	remove-compiled-kernel \

all:
	echo "Try make install"

install:
	if [ -d /boot/dtbs ]; then \
	    sudo cp $(DRACUT) /etc/dracut.conf.d/ ; \
	fi
	sudo mkdir -p /root/bin/ && sudo cp installkernel /root/bin/
	mkdir -p ~/.bashrc.d/ ~/bin/
	cp vimrc ~/.vimrc
	cp $(BASHRC) ~/.bashrc.d/
	if ! grep -q 'bashrc.d' ~/.bashrc; then cat bashrc.d >> ~/.bashrc; fi
	cp $(UTILS) ~/bin/
