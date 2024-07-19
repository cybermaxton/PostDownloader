from colorama import Fore, Style

CrossLogo = f'{Fore.YELLOW}[X]{Style.RESET_ALL}'

VERSION = f'{Fore.RED}1.0.1{Style.RESET_ALL}'

HELP = f'''{Fore.YELLOW}
                       YT Downloader by Cyber MaXton
                   ---Video Downloader Tool For Linux ---
                             Version {VERSION}

Note:- This tool is designed to make certain tasks easier. Please do not use 
        it to download YouTube videos for offline viewing. Watch videos on YouTube
        to support creators by watching Ads. If you use this tool to download 
        videos, we are not responsible for any consequences.{Style.RESET_ALL}
'''

NO_INPUT = f'''
{Fore.YELLOW}No Input!{Style.RESET_ALL}

Here's The Help Menu How You Can Use Post Downloader By Cyber MaXton

      -h, --help :          Syntax for help
      -y, --youtube :       To Download video from youtube
      -i, --instagram :     To Download post or Reel from Instagram
      -f, --facebook :      To Download post from Facebook 
      -e, --exit :          To Exit From the tool (You can also press Ctrl+C to exit the program)

Enter syntax from above syntax according to your need 
   '''

ISSUE = f'''
{Fore.YELLOW}Issue :/
\nSometimes the title of downloaded video may not be same as the actual video title 
as some characters are reserved by the OS\n{Style.RESET_ALL}'''

WRONGINPUT = f'''
{CrossLogo}{Fore.RED} Wrong Input{Style.RESET_ALL} : {Fore.YELLOW} You entered something which was not recognised by this program{Style.RESET_ALL}'''

