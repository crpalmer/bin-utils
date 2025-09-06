#!/bin/sh

echo "General compilation:"
sudo dnf install make ccache flex bison openssl-devel elfutils-libelf-devel ncurses-devel pahole dwarves
echo "Rust:"
sudo dnf install rust rust-src bindgen-cli rustfmt clippy
