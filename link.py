import json
import subprocess
from os.path import isdir, islink
from pathlib import Path
from shutil import rmtree

SOURCE = Path.cwd().joinpath("setup")  # setup folder in winsefs as source
HOMEDIR = Path.home()


class WSFS:
    def process(src: Path, dst: Path) -> bool:
        srctime = src.stat().st_mtime
        dsttime = dst.stat().st_mtime
        if srctime < dsttime:
            print(f"{dst} is newer, replacing {src}")
            WSFS.clone(dst, src)
        elif srctime == dsttime:
            print(f"{src} and {dst} is modified at the exact same time")
            print(f"Using {src} as source file ~> Migrating {dst} to a symbolic link")
        elif srctime > dsttime:
            print(f"{src} is newer, updating {dst}")
        WSFS.symlink(src, dst)

    def validate(src: Path, dst: Path) -> bool:
        return True if src == dst.resolve() else False

    def clone(src: Path, dst: Path):
        print(f"Cloning {src} to {dst}")
        args = ["xcopy", "/g", "/i", "/k"] if isdir(src) else ["copy"]
        args.append(str(src))
        args.append(str(dst))
        subprocess.run(args, shell=True)

    def symlink(src: Path, dst: Path):
        if dst.exists():
            if isdir(dst):
                rmtree(dst)
            else:
                dst.unlink()
        args = ["mklink"]
        if isdir(src):
            args.append("/D")
        args.append(str(dst))
        args.append(str(src))
        subprocess.run(args, shell=True)


def process(name: str, src: Path, dst: Path) -> bool:
    if src.exists():
        if islink(dst):
            if WSFS.validate(src, dst):
                print(f"{name} is already linked!")
                return True
            print(f"Symlink corrupted, renewing {name}")
            WSFS.symlink(src, dst)
        elif dst.exists():
            print(f"{HOMEDIR} already has {name}, comparing with {src}")
            WSFS.process(src, dst)
        return True
    elif dst.exists():
        WSFS.clone(dst, src)
        WSFS.symlink(src, dst)
        return True
    else:
        print(f"There's no {name} in {SOURCE} or {HOMEDIR}.")
        return False


print("Windows Setup Files Sync [Version 1.0.2]")
with open("wsfs.json") as load:
    skipped = []
    count = empty = 0
    data = json.load(load)
    for f in data["files"]:
        print(f"\n--> Processing {f}:")
        if process(f, SOURCE.joinpath(f), HOMEDIR.joinpath(f)):
            count += 1
            continue
        empty += 1
        skipped.append(f)

    for d in data["dirs"]:
        print(f"\n--> Processing {d} folder:")
        if process(d, SOURCE.joinpath(d), HOMEDIR.joinpath(d)):
            count += 1
            continue
        empty += 1
        skipped.append(d)

    total = len(data["files"]) + len(data["dirs"]) - empty
    print(f"\n# Finished processing | {count} of {total} successful links")
    print(f"> Skipped links ({empty}): {skipped if skipped else None}")

input("\nThank you for using WinSeFS! Enter any key to exit...")
