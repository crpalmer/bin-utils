#!/usr/bin/python3

import os

all = []

def load_directory(dir, prefix = "", suffix = ""):
    dict = {}
    for file in os.listdir(dir):
        if prefix == "" or file.startswith(prefix):
            if suffix == "" or file.endswith(suffix):
                full_path = os.path.join(dir, file)
                key = file.removeprefix(prefix).removesuffix(suffix)
                dict[key] = full_path
                if not key in all:
                    all.append(key)
    return dict

vmlinuz = load_directory("/boot", "vmlinuz-")
modules = load_directory("/usr/lib/modules")
initrd = load_directory("/boot", "initramfs-", ".img")
config = load_directory("/boot", "config-")

print(modules)
print("Installed kernels:")
print("==================")

all.sort()
broken = []
for version in all:
    if version in vmlinuz.keys() and version in modules.keys() and version in initrd.keys():
        print(version)
    else:
        broken.append(version)

if len(broken) > 0:
    print("\nBroken kernels:")
    print("=================")
    for version in broken:
        print(version, end=" - missing:")
        if not version in vmlinuz.keys():
            print(" vmlinuz", end="")
        if not version in modules.keys():
            print(" modules", end="")
        if not version in initrd.keys():
            print(" initramfs", end="") 
        print()
