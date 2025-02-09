<p align="center">
  <img src="logo01.png" alt="WaveShrink Logo" style="border: 2px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</p>


# WaveShrink 🎵

WaveShrink is a simple yet powerful CLI tool to **compress WAV files** into smaller audio formats like **MP3** and **OGG** while maintaining quality. It supports **batch processing** of all WAV files in a directory.

## Features ✨
✅ Convert WAV to MP3 or OGG
✅ Support for **batch conversion** in a directory
✅ Customizable **bitrate**
✅ Lightweight and easy to use
✅ Option to keep or delete original WAV files

## Installation 🛠️
WaveShrink requires **Python 3.7+** and `pydub`. Install dependencies with:

```sh
pip install pydub rich
```

### **FFmpeg Requirement**
Pydub requires FFmpeg to process audio files. Install it using:

- **Mac (Homebrew)**:
  ```sh
  brew install ffmpeg
  ```
- **Linux (Debian-based)**:
  ```sh
  sudo apt install ffmpeg
  ```
- **Windows**: [Download FFmpeg](https://ffmpeg.org/download.html) and add it to PATH.

## Usage 🚀

### Convert a single WAV file:
```sh
python main.py example.wav                    # Converts to MP3 and deletes original
python main.py example.wav --keep            # Converts to MP3 and keeps original
python main.py example.wav -f ogg            # Converts to OGG and deletes original
python main.py example.wav -b 128k           # Converts with 128k bitrate
```
This converts `example.wav` into `example.mp3` with **128 kbps** bitrate.

### Convert all WAV files in a directory:
```sh
python main.py -d /path/to/directory             # Converts all WAVs to MP3 and deletes originals
python main.py -d /path/to/directory --keep      # Converts all WAVs to MP3 and keeps originals
```
This finds **all `.wav` files** in `/path/to/directory` and converts them into **OGG (96 kbps)**.

## Command-Line Options 📝

```sh
usage: main.py [-h] [-d DIRECTORY] [-f {mp3,ogg}] [-b BITRATE] [-k] [input]

Convert a WAV file or all WAV files in a directory to a smaller compressed format (MP3, OGG).

positional arguments:
  input                 Path to a WAV file (if converting a single file).

optional arguments:
  -d DIRECTORY, --directory DIRECTORY
                        Path to a directory containing WAV files (batch conversion).
  -f {mp3,ogg}, --format {mp3,ogg}
                        Output format (default: mp3).
  -b BITRATE, --bitrate BITRATE
                        Bitrate for the output file (default: 64k).
  -k, --keep            Keep original WAV files (default: delete after conversion).
```

## Example Output 📊
```sh
🎵 Converting example.wav → example.mp3 at 64k bitrate

Processing... ████████████░░░░░░░░░░░░  67%
✅ Conversion complete! Saved as: example.mp3
```

## License 📜
MIT License. Feel free to use, modify, and contribute!

---
Made with ❤️ to help you save storage! 🚀

