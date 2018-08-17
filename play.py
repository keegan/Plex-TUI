import subprocess
import auth
import secret
from time import sleep

token=auth.auth()

def play(loc):
    subprocess.Popen("pkill -f ffplay", shell=True)
    sleep(3)
    cmd = "ffplay <(curl -s " + secret.root_url + loc + "?X-Plex-Token=" + token + ") -autoexit -showmode 1 &> /dev/null &"
    #print(cmd)
    subprocess.Popen(cmd, shell=True, executable="/bin/bash")
    sleep(3)
