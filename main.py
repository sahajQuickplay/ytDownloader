import yt_dlp
import inquirer
import os
from typing import List, Dict
from pathlib import Path

def get_available_formats(url: str) -> List[Dict]:
    """Get available resolutions for MP4 video with audio merging."""
    ydl_opts = {
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = []
            
            # Collect resolutions from video formats
            for f in info['formats']:
                if f.get('height') and f.get('ext') == 'mp4':  # MP4 video formats
                    resolution = f"{f['height']}p"
                    formats.append({
                        'resolution': resolution,
                        'format_id': f['format_id'],
                        'vcodec': f.get('vcodec', 'N/A'),
                        'acodec': f.get('acodec', 'N/A')
                    })
            
            # Remove duplicates and sort by resolution
            unique_formats = {f['resolution']: f for f in formats}.values()
            return sorted(unique_formats, key=lambda x: int(x['resolution'][:-1]), reverse=True)
    
    except Exception as e:
        print(f"Error getting video formats: {str(e)}")
        return []

def download_video(url: str, format_choice: Dict, destination: str):
    """Download the video in MP4 with audio."""
    ydl_opts = {
        'format': f"bestvideo[height<={format_choice['resolution'][:-1]}]+bestaudio/best[height<={format_choice['resolution'][:-1]}]",
        'merge_output_format': 'mp4',  # Force MP4 output
        'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nDownloading video in {format_choice['resolution']}...")
            ydl.download([url])
            print("\nDownload completed successfully!")
    
    except Exception as e:
        print(f"\nError downloading video: {str(e)}")

def main():
    try:
        # Get YouTube URL
        url = input("\nEnter YouTube URL: ").strip()
        
        # Get available formats
        print("\nFetching available formats...")
        formats = get_available_formats(url)
        
        if not formats:
            print("No suitable formats found or invalid URL.")
            return
        
        # Create format choices for dropdown
        choices = [f"{f['resolution']} (vcodec: {f['vcodec']}, acodec: {f['acodec']})" for f in formats]
        
        # Resolution selection
        questions = [
            inquirer.List('resolution',
                         message="Select preferred resolution",
                         choices=choices,
                         carousel=True)
        ]
        
        answers = inquirer.prompt(questions)
        if not answers:
            print("\nSelection cancelled.")
            return
            
        selected_res = answers['resolution'].split()[0]
        selected_format = next(f for f in formats if f['resolution'] == selected_res)
        
        # Get destination directory
        print("\nDefault download location is current directory.")
        custom_dest = input("Enter custom download path (or press Enter for default): ").strip()
        destination = custom_dest if custom_dest else os.getcwd()
        
        # Verify destination
        if not os.path.exists(destination):
            create = input(f"\nDirectory {destination} doesn’t exist. Create it? (y/n): ").lower()
            if create == 'y':
                Path(destination).mkdir(parents=True, exist_ok=True)
            else:
                print("Download cancelled.")
                return
        
        # Download the video
        download_video(url, selected_format, destination)
        
    except KeyboardInterrupt:
        print("\n\nDownload cancelled by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()