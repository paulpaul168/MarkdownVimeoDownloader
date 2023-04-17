# Markdown Vimeo Downloader


This is a Python script that downloads videos from Vimeo based on their URLs in a Markdown file. It uses Vimeo's API to extract the video URL and then saves the video to a local directory.
Prerequisites

- Python 3
- requests library

## Usage

- Create a new Markdown file named videos.md.
- Add the Vimeo video URLs to the Markdown file in the following format: [Title](URL).
- Run the script in the terminal or command prompt: python vimeo_downloader.py
- The script will create a videos directory if it doesn't exist, download the videos, and save them with their corresponding titles in the format Title.mp4.
- If a video with the same title already exists in the videos directory, it will skip downloading that video.

## Limitations

- The script is only able to download videos from Vimeo.
- The video URLs must be in a Markdown file named videos.md.
- The script assumes that the video URL is in the format https://vimeo.com/VIDEO_ID. If the URL is different, the script may not work as expected.

## Disclaimer

This script is intended for educational purposes only. Downloading copyrighted material may be illegal in your country. Use at your own risk.