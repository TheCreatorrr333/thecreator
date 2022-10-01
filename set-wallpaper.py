import ctypes
import random

paths = ["C:\\Users\\uczen\\Pictures\\gtapoland.png", "C:\\Users\\uczen\\Pictures\\rickroll.png", "C:\\Users\\uczen\\Pictures\\unknown.png"]

ctypes.windll.user32.SystemParametersInfoW(20, 0, random.choice(paths) , 0)