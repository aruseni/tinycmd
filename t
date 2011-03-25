#!/usr/bin/env python
from __future__ import print_function


# Config:
tinycmd_host = "tinycmd.org" # The web server host
tinycmd_user = ""            # user on tinycmd_host


import os, sys
import socket
import optparse
from getpass import getpass
if   sys.version_info[0] == 2: import httplib
elif sys.version_info[0] == 3: from http import client as httplib
else: 
	print("Wrong version of Python")
	sys.exit(1)


__prog__        = "tinycmd"
__version__     = "0.1"
__website__     = "http://tinycmd.org"
__description__ = "  tinycmd.org  -  The command string shortening service."
__usage__       = "%prog [options] [command_string_id]" 


if __name__ == "__main__":

	opt = optparse.OptionParser(description=__description__, usage=__usage__,
	                            version = __prog__ + " v" +  __version__,
	                            epilog="")
	opt.add_option("-r", "--run", help="Run without questions", 
	               dest="noquestions", action="store_true", default=False)
	opt.add_option("-s", "--showonly", help="Only show command, don't run", 
	               dest="showonly", action="store_true", default=False)
	opt.add_option("-u", "--user", dest="user", default=tinycmd_user, 
	               type="string", help="Run sript for this user of tinycmd")
	opt.add_option("--host", "--server", dest="host", default=tinycmd_host, 
	               type="string", help="adress of tinycmd-server", 
	               metavar="SERVER")
	opt.add_option("-a", "--addcmd", dest="addcmd", metavar="COMMAND", 
	               help="Add this command to tinycmd-server", type="string")
	opt.add_option("-l", "--listcmd", dest="listcmd", default=False, 
	               action="store_true", help="List commands for current user")
	(options, args) = opt.parse_args()

    	# add command to server
	if options.addcmd:
		if len(args) > 1:
			opt.exit(1, "Wrong count of arguments")
		user = options.user
		pswd = getpass("User: " + user + "\nPassword: ") if user else ""
		# =============================
		# add-command-code will be here
		# =============================
		exit(0)

	# list of command for user
	if options.listcmd:
		if not options.user:
			opt.exit(1, "List of command may be showed only for concrete user")
		# =============================
		# list-command-code will be here
		# =============================
		exit(0)
    
	if len(args) == 0:
		print("Wrong count of arguments\n")
		print(opt.get_usage())
		print(opt.get_description(),"\n")
		print(opt.format_option_help())
		exit(1)

	user = options.user + "/" if options.user else ""
	try: conn = httplib.HTTPConnection(options.host) 
	except (httplib.HTTPResponse, socket.error) as ex:
		opt.exit(1, "Unable to connect to the server:" + str(ex))

	for arg in args:
		
		try: conn.request("GET", "/cs/" + user + arg + "/text/")    
		except (httplib.HTTPResponse, socket.error) as ex:
			opt.exit(1, "Unable to connect to the server:" + str(ex))
	
		r1 = conn.getresponse()
		if r1.status == 404: 
			print("Command string not found.")
		elif r1.status == 500:
			print("The server gives the 500 error. Please try again later.")
		elif r1.status == 200:
			data = r1.read()
			print("Command: ")
			print(data)
			if option.showonly:
				exit(0)    
			else:
				allow_run = True
				if not options.noquestions:
					answer = raw_input("You are really want run this command?")
					allow_run = answer[0].lower() == 'y'
				if allow_run:
					os.system(data)
	
	conn.close()
