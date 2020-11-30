import os
import ctypes
import sys


def isUserAdmin():
    if os.name == 'nt':  
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False


def main():
    if(isUserAdmin()):
        os.popen('netsh interface ipv4 set address name="Wi-Fi" static 192.168.1.169 255.255.255.0 192.168.1.1')
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

main()