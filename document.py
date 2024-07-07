from colorama import Fore, Style

VERSION = f'{Fore.RED}1.0.0{Style.RESET_ALL}'

HELP = f'''{Fore.YELLOW}
                     YT Downloader by Code With MaXton
                   ---Video Downloader Tool For Linux ---
                             Version {VERSION}

Note:- This tool is designed to make certain tasks easier. Please do not use 
        it to download YouTube videos for offline viewing. Watch videos on YouTube 
        to support creators by watching Ads. If you use this tool to download 
        videos, we are not responsible for any consequences.{Style.RESET_ALL}
'''

NO_INPUT = '''
No Input!

Here's The Help Menu How You Can Use Post Downloader By Code With MaXton

      -h, --help :          Syntax for help
      -y, --youtube :       To Download video from youtube
      -i, --instagram :     To Download post or Reel from Instagram
      -f, --facebook :      To Download post from Facebook 
      -e, --exit :          To Exit From the tool (You can also press Ctrl+C to exit the program)

Enter syntax from above syntax according to your need
Re-run the program copy and paste this in your terminal

python3 pdmaxton.py 
   '''

ISSUE = f'''
{Fore.YELLOW}Issue :/
\nSometimes the title of downloaded video may not be same as the actual video title 
as some characters are reserved by the OS\n{Style.RESET_ALL}'''

# print(ISSUE)