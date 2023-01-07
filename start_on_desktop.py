from win32gui import GetWindowText, GetForegroundWindow
import time
import os, sys
import subprocess

apps = []

while True:
    if GetWindowText(GetForegroundWindow()) == '':
        with open('start_on_desktop.txt', 'r') as f:
            exec(f.read())
    time.sleep(5)