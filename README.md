# YuppTV Free-to-Air Channel Scraper and VLC Playlist Generator

This Python script scrapes JSON data of YuppTV free-to-air channels and converts it into a VLC-playable `.m3u8` playlist using a Cloudflare relay.

## Features

- Scrapes free channels from YuppTV.
- Converts the data to an M3U8 playlist format.
- Playlist compatible with VLC player.
- Uses Cloudflare relay to stream channels from:  
  [`https://neptv.guruusr.workers.dev/yupp/`](https://neptv.guruusr.workers.dev/yupp/).

## Channel Categories

The following channel categories are available:

- Spiritual
- News
- Education
- Movies
- Entertainment
- Music
- Sports
- Lifestyle
- Business News
- Other

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sunilprregmi/yupptv-fta.git
   ```

2. **Navigate to the directory:**

   ```bash
   cd yupptv-fta
   ```

3. **Run the Python script:**

   ```bash
   python playlist.py
   ```

   The script will generate an `.m3u8` playlist file that can be opened in VLC or any compatible media player.

## Requirements

- Active brain 🧠
- Python installed on your machine
- Basic knowledge of shell commands
- VLC or any player that supports `.m3u8` files

## Contribution

Feel free to fork, modify, or submit pull requests to improve the project. Contributions are welcome!

## Disclaimer

This tool is intended for educational purposes only. The use of this tool to access YuppTV content should comply with all applicable laws and platform terms of service.
