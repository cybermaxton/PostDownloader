import document
import logos
from pytube import YouTube
from moviepy.editor import AudioFileClip, VideoFileClip
import os
from colorama import Fore, Style
import time

version = document.VERSION

PlusLogo = f'{Fore.YELLOW}[+]{Style.RESET_ALL}'

def PostDownloader():
    print(logos.PostDownloaderText)

    print(f'''{Fore.CYAN}
        -h, --help:          Syntax for help
        -y, --youtube:       To Download video from youtube
        -i, --instagram:     To Download post or Reel from Instagram
        -f, --facebook:      To Download post from Facebook 
        -e, --exit:          To Exit From the tool (You can also press Ctrl+C to exit the program){Style.RESET_ALL}
        ''')

def YTDownloader():

    # Prints the YT Downloader logo from logos.py
    print(logos.YTDownloaderText)

    # Ask user for the link
    UserYtLinkInput = input(f'{PlusLogo} Enter Video Link: ')
    
    try:
        # Checks/Verify the link
        videoLink = YouTube(UserYtLinkInput)
        # Prints the title of video
        print(f"{PlusLogo} Title: {videoLink.title}")
        # Retrieve the available streams 
        videoStreams = videoLink.streams
    
        # Filter only MP4 streams
        mp4_streams = videoStreams.filter(file_extension='mp4').filter(type='video')
        # Filter Audio of the video
        video_audio = videoStreams.filter(only_audio=True).first()
        
        # Prints all available streams in descending order with index number
        print(f"\n{PlusLogo} Available MP4 Streams: \n")
        for i, stream in enumerate(mp4_streams, start=1):
            print(f"{i}. Resolution: {stream.resolution}, Format: {stream.mime_type}")
        
        # Ask the user choice for stream to download
        while True:
            try:
                user_choice = int(input(f"\n{PlusLogo} Enter the serial number of the stream you want to download (0 to cancel): "))
                
                # Cancels the download if user want
                if user_choice == 0:
                    print(f"{PlusLogo} Download canceled.")
                    return
                

                elif 1 <= user_choice <= len(mp4_streams):
                    selected_stream = mp4_streams[user_choice - 1]
                    print(f"\n{PlusLogo} Selected Stream: {selected_stream.resolution}, Format: {selected_stream.mime_type}")
                    
                    # This variables were created so that we can delete raw output 
                    video_filepath = 'raw_video.mp4'
                    audio_filepath = 'raw_audio.mp3'
                    
                    # Downloads video and audio
                    selected_stream.download(output_path='.', filename='raw_video.mp4')
                    video_audio.download(output_path='.', filename='raw_audio.mp3')
                    
                    # merges the audio with video as sometime audio may not be downloaded due to API bug
                    audio = AudioFileClip('raw_audio.mp3')
                    video = VideoFileClip('raw_video.mp4')
                    final_output = video.set_audio(audio)

                    # Title of video
                    name = videoLink.title

                    # Remove all charcters which cannot be used in title
                    invalid_characters = ['\\', '/', ':', '*', '?', '"', '<', '>', '|', '.',]

                    for invalid_character in invalid_characters:
                        name = name.replace(invalid_character, '')

                    if invalid_character in videoLink.title:
                        print(document.ISSUE)

                    # Adds .mp4 extension in the output
                    NameWithExtension = name + '.mp4'

                    # Export final video with audio merged
                    final_output.write_videofile('output' + '.mp4')

                    # Renames the output file with original title and also deletes the temporary downloaded files
                    os.rename('output.mp4', NameWithExtension)
                    os.remove(video_filepath)
                    os.remove(audio_filepath)
                    
                    break
                     
                else:
                    print("Invalid serial number. Please enter a valid serial number.")
            
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    except Exception as e:
        print(f":/  Either Invalid Link! or any API issue report us on Github (Code With MaXton)")

def IGDownlaoder():
    print(logos.IGDownloaderText)
    print('Instagram Downloader is in developing stage! Coming soon...')
    return

def FBDownloader():
    print(logos.FBDownloaderText)
    print('Facebook Downloader is in developing stage! Coming soon...')
    return

def ExitProgram():
    print(f'''
                 {Fore.YELLOW}Thanks for using Post Downloder{Style.RESET_ALL}
          {Fore.GREEN}Also Visit our Github Profile:-{Style.RESET_ALL} {Fore.RED}Code With MaXton{Style.RESET_ALL}''')
    exit()

while True:
    time.sleep(2)
    PostDownloader()

    user_input = input(f'\n {Fore.YELLOW}[+]{Style.RESET_ALL} Type Here: ')

    if user_input == "":
        print(document.NO_INPUT)

    elif user_input == "-h" or user_input == "--help":
        print(document.HELP)

    elif user_input == "-y" or user_input == "--youtube":
        YTDownloader()

    elif user_input == '-i' or user_input == '--instagram':
        IGDownlaoder()

    elif user_input == '-f' or user_input == '--facebook':
        FBDownloader()
    
    elif user_input == '-e' or user_input == '--exit':
        ExitProgram()