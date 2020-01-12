<h1 align=center>Windows Setup Files Sync (WinSeFS)</h1>
<p align=center>
Your personal settings, config files, and registry manager all in one place, fully synchronized across the cloud.<br>Restore your PC configuration in seconds!
</p>
<blockquote align=center>Unix-like dotfiles for Windows</blockquote>

## Download the executable

- [`v1.0.2`](https://github.com/ignatiusmb/winsefs/releases/download/v1.0.2/winsefs-v1.0.2.exe) - [20.01.12](https://github.com/ignatiusmb/winsefs/releases/tag/v1.0.2) Fix prompt when copying files
- [`v1.0.0`](https://github.com/ignatiusmb/winsefs/releases/download/v1.0.0/winsefs-v1.0.0.exe) - [20.01.09](https://github.com/ignatiusmb/winsefs/releases/tag/v1.0.0) Initial Release

### Usage - with executable

1. Create a folder inside one of your preferred Cloud Storage (e.g. Google Drive, OneDrive, iCloud, etc.)
2. Move the executable inside the created folder
3. Download [`wsfs.json.sample`](wsfs.json.sample) and rename it to `wsfs.json`
4. Add or delete entries in `wsfs.json` with your `config files/directories`
5. Double-click/run the executable
6. A New `setup` folder will be created, this folder consists all of your files from the entries you provided in `wsfs.json`

### Usage - with source code

1. Fork this repository
2. Clone it inside one of your preferred Cloud Storage
3. Execute `setup.cmd` to copy `wsfs.json.sample`
4. Add or delete entries in `wsfs.json` with your `config files/directories`
5. Run/execute `python link.py` in the folder command prompt
6. A New `setup` folder will be created, this folder consists all of your files from the entries you provided in `wsfs.json`
7. Make sure to not remove `setup` from `.gitignore` if you're pushing to a public repository

### Distributing

The executable is created with `pyinstaller` with the command below, you can try compiling from the source code yourself and compare it with the distributed executable

```bash
pyinstaller link.py -F -n winsefs-v<major>.<minor>.<patch>
```

---

<h3 align=center>
    <pre>WinSeFS | <a href=LICENSE>MIT License</a></pre>
</h3>

---

<p align=center>
    <a href=https://ignatiusmb.github.io>Portfolio</a>
    &bull;
    <a href=https://imbagus.com>imbagus.com</a>
</p>
