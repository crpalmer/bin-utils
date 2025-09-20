#!/bin/sh

echo "General compilation:"
sudo dnf install make ccache flex bison openssl-devel elfutils-libelf-devel ncurses-devel pahole dwarves cmake
echo "Rust:"
sudo dnf install rust rust-src bindgen-cli rustfmt clippy
echo "VIM:"
sudo dnf install vim
echo "Fedora Kernel spec"
sudo dnf install fedpkg
mkdir -p ~/fedora && cd ~/fedora && fedpkg clone -a kernel && cd kernel && sudo dnf builddep kernel.spec
