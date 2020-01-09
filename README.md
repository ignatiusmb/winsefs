<h1 align=center>Windows Setup Files Sync (WinSeFS)</h1>
<p align=center>
Your personal settings, config files, and registry manager all in one place, fully synchronized across the cloud.<br>Restore your PC configuration in seconds!
</p>
<blockquote align=center>Unix-like dotfiles for Windows</blockquote>

## Download the executable

- [`Winsefs v1.0.0`](releases/download/v1.0.0/winsefs-v1.0.0.exe) - Initial Release [20.01.09](releases/tag/v1.0.0)

### Usage - with executable

1. Create a folder inside one of your preferred Cloud Storage (e.g. Google Drive, OneDrive, iCloud, etc.)
2. Move the executable inside the created folder
3. Download [`wsfs.json.sample`](wsfs.json.sample) and rename it to `wsfs.json`
4. Add or delete entries in `wsfs.json` with your `config files/directories`
5. Double-click/run the executable

### Usage - with source code

1. Clone this repository inside one of your preferred Cloud Storage
2. Execute `setup.cmd` to copy `wsfs.json.sample`
3. Add or delete entries in `wsfs.json` with your `config files/directories`
4. Run/execute `python link.py` in the folder command prompt

### Distributing

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
