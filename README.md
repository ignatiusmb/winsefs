<h1 align=center>Windows Setup Files Sync (WinSeFS)</h1>

Your personal settings, config files, and registry manager all in one place, fully synchronized across the cloud.

> Unix-like dotfiles for Windows

**DISCLAIMER!** Make sure you commit to a **private repository** if you're going to save your private keys and/or credentials. In no event shall the authors be held responsible for any disclosure.

e.g. *ssh* and *gpg keys*, *.gitconfig*, any *password*, etc.

## Prerequisites

- *This guide assumes you have python3 installed*

## Usage

1. Execute `setup.cmd` to copy `wsfs.json.sample`
2. Add or delete entries in `<name>.wsfs` with your `config files/directories`
3. Run `python link.py` to connect files/directories using symbolic links
