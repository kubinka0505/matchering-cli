<h1 align=center>
	<img src=Documents/Pictures/Matchering_CLI.svg width=500>
</h1>

<p align=center>
	<a href="https://colab.research.google.com/github/kubinka0505/matchering-cli/blob/master/Documents/Matchering-CLI.ipynb"><img src="https://shields.io/badge/Colab-Open-F9AB00?&logoColor=F9AB00&style=for-the-badge&logo=Google-Colab"></a>　<a href="License.txt"><img src="https://custom-icon-badges.demolab.com/github/license/kubinka0505/matchering-cli?logo=law&color=red&style=for-the-badge"></a>
</p>

<p align=center>
	<img src="https://custom-icon-badges.demolab.com/github/languages/code-size/kubinka0505/matchering-cli?logo=database&style=for-the-badge">　<a href="https://codeclimate.com/github/kubinka0505/matchering-cli"><img src="https://shields.io/codeclimate/maintainability/kubinka0505/matchering-cli?logo=Code-Climate&style=for-the-badge"></a>　<a href="https://app.codacy.com/gh/kubinka0505/matchering-cli"><img src="https://shields.io/codacy/grade/b177f6eeb2744d318a0077e47511f561?logo=Codacy&style=for-the-badge"></a>
</p>

## Description 📝
Pack of scripts providing customizable audio matchering.

Features comparison:

|  | [sergree](https://github.com/sergree)'s [`matchering`](https://github.com/sergree/matchering) | [sergree](https://github.com/sergree)'s [`matchering-cli`](https://github.com/sergree/matchering-cli) | [kubinka0505](https://github.com/kubinka0505)'s [`matchering-cli`](https://github.com/kubinka0505/matchering-cli) |
|:-:|:-:|:-:|:-:|
| Cross-platform | ✅ | [❌](https://github.com/sergree/matchering-cli/issues/3) | ✅ |
| URL support | ❌ | ❌ | ✅ |
| Sample rate heritage | ✅<sub>⚙️</sub> | ❌ | ✅ |
| FFT setting | ✅<sub>⚙️</sub> | ❌ | ✅ |
| Normalization disable | ✅<sub>⚙️</sub> | ✅ | ✅ |
| Limiting disable | ✅<sub>⚙️</sub> | ✅ | ✅ |

<sub>⚙️ - *intermediate module knowledge required*</sub>

## Requirements 📥
Programs:
- [`Python >= 3.8`](https://www.python.org/downloads) 🐍

Modules:
- [`matchering >= 2.0.6`](https://github.com/sergree/matchering) - Audio matchering module 🔎
- [`mutagen >= 1.45.1`](https://github.com/quodlibet/mutagen) - Audio info checker 🔊
- [`requests >= 2.12.5`](https://github.com/psf/requests) - URL fetching 🔗
- [`distro >= 1.7`](https://github.com/python-distro/distro)<span>*</span> - Unix directory opening handler 📂

Packages (bold links are **Windows** static executable binaries):
- [**`FFmpeg >= 4.2`**](https://videohelp.com/software/ffmpeg/old-versions) - Audio processing 🎦
	- **64-bit reccomended!** ([*possible memory allocation* failures](https://forum.doom9.org/archive/index.php/t-162236.html#copyright))
- [`Python3-PIP`](https://packages.debian.org/sid/python3-pip)<span>*</span>

<span>*</span> - Required on Linux

## Installation ⚙️
**When on Linux**, install required packages by using this one-liner:
```bash
sudo apt-get install git python3-apt python3-pip ffmpeg
```
1. Clone the repository and move to its directory.
	```bash
	git clone https://github.com/kubinka0505/matchering-cli
	cd matchering-cli
	```
2. Install required modules by inputting `pip install -r requirements.txt`
3. Type **`mg_cli.py -h`** for more info. ℹ️

---

## Usage 📝
Process **target** input file (`-i`) and **reference** audio (`-r`)
```bash
mg_cli.py -i "~/Desktop/Song.wav" -r "~/Downloads/Better_Song.flac"
```

As above, but **set target directory** (`-o`) and **bit depth** to `16`
```bash
mg_cli.py -i "../Sound.flac" -r "%UserProfile%\Downloads\Music.ogg" -o "~/Music/My Songs" -b 16
```

Process with **custom FFT window size** (`-fft`) and **inherit sample rate** (`-sr auto`)
```bash
mg_cli.py -i "https://website.com/Audio.ogg" -r "~/Music/Discography/Artist/Album/Artist - Title.flac" -fft 2048 -sr auto
```

As above, but **do not apply limiting** (`-nl`, **and normalization** (`-nn`) and **process with full logs** (`-v 2`)
```bash
mg_cli.py -i "https://website.com/Artist ft. Guest - Title (Remix).flac" -r "File.wav" -fft 4096 -sr auto -nl -nn -v 2
```

---

## Meta Info ℹ️
All versions of this project have been tested on:
| OS | Distribution | OS Version | Python Version | System Architecture (`bits`) |
|:-:|:-:|:-:|:-:|:-:|
| Windows | ― | 10 | 3.11.0 | 64 |
| Linux | Ubuntu | LTS 22.04 | 3.10.6 | 64 |