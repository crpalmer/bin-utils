BASHRC = \
	core.rc \
	git.rc \
	linux.rc \
	pico.rc \

DRACUT = \
	50-slim7x.conf \
	51-usb-storage.conf \

PG_UTILS = _pg-read.py pg-read.sh

ROOT = \
	installkernel \
	kernel-status.py \
	package-compiled-kernel \
	remove-compiled-kernel \
	synology-backup-dirs \

# To start a service you sould do:
# sudo systemctl daemon-reload
# sudo systemctl enable XXXX.service
# sudo systemctl start XXXX.servivce

SERVICES = \
	foundry.service \
	foundry-james.service \
	minecraft.service \

UTILS = \
	build-orca.sh \
	cmake-debug \
	compiled-kernels \
	orca-postprocess.sh \
	$(PG_UTILS) \
	rdp-tunnel.sh \

all:
	echo "Try make install"

install:
	if [ -d /boot/dtbs ]; then \
	    sudo cp $(DRACUT) /etc/dracut.conf.d/ ; \
	fi
	sudo mkdir -p /root/bin/ && sudo cp $(ROOT) /root/bin/
	mkdir -p ~/.bashrc.d/ ~/bin/
	cp vimrc ~/.vimrc
	cp $(BASHRC) ~/.bashrc.d/
	if ! grep -q 'bashrc.d' ~/.bashrc; then cat bashrc.d >> ~/.bashrc; fi
	cp $(UTILS) ~/bin/
	if [ -d /etc/systemd/system ]; then sudo cp $(SERVICES) /etc/systemd/system; fi
