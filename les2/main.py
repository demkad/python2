import ctypes
from winsound import MB_ICONEXCLAMATION
import win32api
import win32com.client
 
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.volume = 99
speaker.Speak("ananin ami!")
 
hDllUser32 = ctypes.WinDLL('user32.dll')

# 
#ret = hDllUser32.SetCursorPos(40,35)
#ret = hDllUser32.mouse_event(0x02,100,100,0,0)
#ret = hDllUser32.mouse_event(0x04,100,100,0,0)
# 

#MB_ICONEXCLAMATION = ctypes.c_uint(int("0x30",0))
# 
#NULL = None
#ret = hDllUser32.MessageBoxA(NULL,
#                             b'This is a MessageBox wrapping MessageBoxA()',
#                             b'Message Box Test',
#                             MB_ICONEXCLAMATION)
#                             
#
#del hDllUser32         