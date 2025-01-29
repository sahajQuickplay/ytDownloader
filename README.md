# YouTube Video Downloader

## Overview
This Python script allows users to download YouTube videos in their preferred resolution using `yt-dlp`. It provides an interactive prompt for selecting available formats and specifying a download location.

## Features
- Fetches available video formats with resolution, video codec, and audio codec details.
- Allows users to choose their preferred resolution interactively.
- Downloads videos in MP4 format, merging video and audio streams if necessary.
- Supports specifying a custom download directory.

## Requirements
- Python 3.6+
- `yt-dlp` (for downloading YouTube videos)
- `inquirer` (for interactive prompts)
- `ffmpeg` (for merging video and audio streams)

## Installation
First, ensure you have Python installed. Then, install the required dependencies:

```sh
pip install -r requirements.txt
```

You must also have `ffmpeg` installed. You can install it via:

- **Windows:** Download from [FFmpeg official site](https://ffmpeg.org/download.html) and add it to your system PATH.
- **Mac:** Install via Homebrew:
  ```sh
  brew install ffmpeg
  ```
- **Linux:** Install via your package manager:
  ```sh
  sudo apt install ffmpeg  # Debian/Ubuntu
  sudo dnf install ffmpeg  # Fedora
  sudo pacman -S ffmpeg    # Arch
  ```

## Usage
1. **Run the script**
   ```sh
   python main.py
   ```
2. **Enter the YouTube video URL** when prompted.
3. **Select the desired resolution** from the interactive menu.
4. **Specify a download directory** (or press Enter to use the default directory).
5. **Wait for the download to complete.**

## How It Works
1. The script extracts available formats for the given YouTube URL.
2. It filters formats that have either video and audio combined or can be merged.
3. The user selects a preferred resolution from the list.
4. The script downloads the video using `yt-dlp` and saves it to the chosen directory.

## Example Run
```sh
Enter YouTube URL: https://www.youtube.com/watch?v=example
Fetching available formats...

Select preferred resolution:
1) 1080p (codec: avc1.64002A)
2) 720p (codec: avc1.64001F)
3) 480p (codec: avc1.4d4015)

Default download location is current directory.
Enter custom download path (or press Enter for default): 

Downloading video in 1080p...
Download completed successfully!
```

## Error Handling
- If no valid formats are found, the script notifies the user and exits.
- If the specified directory does not exist, the user is prompted to create it.
- If an error occurs during download, it is displayed to the user.
- The script can be safely terminated with `Ctrl + C`.

## License
This script is open-source and can be modified as needed.

