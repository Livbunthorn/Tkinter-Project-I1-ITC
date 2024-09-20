# YouTube Video Downloader

This is a simple Python project using Tkinter that allows users to download videos from YouTube by providing a URL. The application uses the `yt-dlp` library to handle downloading and saves the video to a location chosen by the user.

## Features

- Download YouTube videos by providing a URL.
- Allows users to choose the download location.
- interface built using Tkinter.

## Requirements

- Python 3.6 or higher
- `yt-dlp` library

## Installation

### Step 1: Install Python 3

Ensure you have Python 3 installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Step 2: Install `yt-dlp`

The `yt-dlp` library is required to download YouTube videos. You can install it using `pip` as follows:

#### If you have only one version of Python installed:
    pip install yt-dlp

####  If you have Python 3 (and, possibly, other versions) installed:
    pip3 install yt-dlp

#### If you don't have PIP or it doesn't work
    python -m pip install yt-dlp
                
    python3 -m pip install yt-dlp

#### If you have Linux and you need to fix permissions (any one):
    sudo pip3 install yt-dlp
    pip3 install yt-dlp --user


####  If you have Windows and you have set up the py alias
    py -m pip install yt-dlp


## Usage
1. Run the code.
2. Enter the URL of the YouTube video you want to download.
3. Choose the directory where you'd like to save the downloaded video.
4. Click "Download Video."
5. The video will be downloaded, and you'll receive a success message.

## Troubleshooting
If the download fails, check the following:
- Ensure the YouTube URL is correct.
- Check if "yt-dlp" is installed properly using "yt-dlp --version".
- Ensure you have an active internet connection.