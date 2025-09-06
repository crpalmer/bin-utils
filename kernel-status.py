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

def find_prefix(dir = "/boot/loader/entries"):
    dict = {}
    best = ""
    n_best = 0
    for file in os.listdir(dir):
        if not os.path.isdir(os.path.join(dir, file)):
            prefix = file.partition("-")[0]
            if not prefix in dict:
                dict[prefix] = 0
            dict[prefix] = dict[prefix] + 1
            if dict[prefix] > n_best:
                best = prefix
                n_best = dict[prefix]
    return best + "-"

vmlinuz = load_directory("/boot", "vmlinuz-")
modules = load_directory("/usr/lib/modules")
initrd = load_directory("/boot", "initramfs-", ".img")
config = load_directory("/boot", "config-")
loader = load_directory("/boot/loader/entries", find_prefix(), ".conf")

print("Installed kernels:")
print("==================")

all.sort()
broken = []
for version in all:
    if version in vmlinuz and version in modules and version in initrd and version in loader:
        print(version)
    else:
        broken.append(version)

def report(version, bool):
    if (version in vmlinuz) == bool:
        print(" vmlinuz", end="")
    if (version in modules) == bool:
        print(" modules", end="")
    if (version in initrd) == bool:
        print(" initramfs", end="")
    if (version in loader) == bool:
        print(" boot/loader/entries", end="")

if len(broken) > 0:
    print("\nBroken kernels:")
    print("=================")
    for version in broken:
        print(version, end=" - has:")
        report(version, True)
        print(" | missing:", end="")
        report(version, False)
        print()
