#v1.1 STREAM TITLE and you're able to go back if you choose the wrong alternative

#If you have the kbHit file in the same folder as this python script you can remove these 5 lines.
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import jsonTest
import time

#Just to suppress the warnings
import requests
from requests.packages.urllib3.exceptions import SNIMissingWarning, InsecurePlatformWarning

requests.packages.urllib3.disable_warnings(SNIMissingWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

#Clear the shell
def cls():
	print "\n" * 100

#Update these if needed
username = ''
password = ''
#IP Adress
hostname = ''
#Paste your auth key here
authKey = 'q2rcoimmqi7m95tozjqnw9aqk00vkk'

MAC = True

listquality  = {'low': '360p30,low', 'medium': '480p30,medium', 'high': '720p30,720p,high',
            'HD': 'best'}

def chooseMode():
    print "1: To view top streamer currently on twitch.tv"
    print "2: To following WIP"
    try:
        arg = input(": ")
        return arg
    except KeyboardInterrupt:
        print "Bye bye"
        exit()

def openChat():
    # Have to make an iFrame that is small and concise because now it opens a new tab in your
    # current browser
    import webbrowser
    
    webbrowser.open_new(url + "/chat?popout=")

def PCMODE():
    from subprocess import call
    # print url
    string = 'livestreamer ' + url + ' ' + listquality[usrquality] +  \
        ' --twitch-oauth-token ' + authKey + """  -p "/Applications/VLC.app/Contents/MacOS/VLC --meta-title=' """ \
         + str(status) + """ '" """
    
       # startFollowingThread()
    # openChat()
    #print "Here"
    try:
        # Will look into other types of solution. UNSAFE
        call(string, shell=True)
    except KeyboardInterrupt:
        sys.exit(0)

def RPIMODE():
        import kbhit
        import paramiko
        kb = kbhit.KBHit()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
                print "Conntecting to RPi.."
                ssh.connect(hostname, username=username, password=password)
                print "Connection established"
        except paramiko.SSHException:
                print "Connection Failed"
                quit()

        stdin, stdout, stderr = ssh.exec_command("livestreamer " + url + " " + listquality[usrquality] + " -np'omxplayer -o hdmi'")
        print "Opening " + streamer
        print "Give it a few seconds..."
        print "Press any key to close the stream"

        while not kb.kbhit():
                time.sleep(0.5)
        #Kills the mediaplayer
        ssh.exec_command("killall omxplayer.bin")

        kb.set_normal_term()

#------------------#
if __name__ == "__main__":
    while True:
        cls()
        undo = False
        if len(sys.argv) == 1:
            print "Please specify which platform you use, PC or RPI"
            sys.exit()
                
        RPI_OR_PC = str(sys.argv[1])

        if RPI_OR_PC == 'PC':
            print "PC MODE"
        else:
            print "RPI MODE"
                
        if len(sys.argv) > 2:
            usrquality = str(sys.argv[2])
            print "Setting quality to " + usrquality
        else:
            print "No quality specified, defaulting to 'medium'"
            usrquality = 'medium'

        arg = chooseMode()

        if arg == 1:   
            cls()
            print "Fetching current top streamers..."
            jsonTest.fetchTopStreamer()
            print "enter 'b' to go back"
            arg = raw_input(": ")
            if arg == 'b':
                undo = True
            else:
                url, streamer, status = jsonTest.chooseTopStreamer(int(arg))

        elif arg == 2:
            cls()
            print "Fetching streamer you're following"
            jsonTest.fetchFollowing()
            print "enter 'b' to go back"
            arg = raw_input(": ")
            if arg == 'b':
                undo = True
            else:
                url, streamer, status = jsonTest.chooseFollowingStreamer(int(arg))

        else: 
        	print "Error"
        	exit()

        if RPI_OR_PC == 'PC' and not undo:
            PCMODE()
        elif not undo:
            RPIMODE()

