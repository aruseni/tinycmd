#!/usr/bin/env python

from __future__ import print_function

# The web server host
tinycmd_host = "tinycmd.org"

usage = """
tinycmd.org
The command string shortening service.

Usage: t [options] [command_string_id]
Options:
    -h, --help, --usage  -  show this help
    -s, --show           -  show real commands for command_string_id
"""

import os, sys
import socket
if sys.version_info[0] == 2:
    import httplib
else:
    from http import client as httplib

if any([i in sys.argv for i in ('--usage', '--help', '-h')]) or \
   len(sys.argv) == 1 or sys.argv[-1].startswith("-"):
    print(usage)
    sys.exit(1)
try:
    conn = httplib.HTTPConnection(tinycmd_host)

    # The URL returns the command string as plain/text
    conn.request("GET", "/cs/" + sys.argv[-1] + "/text/")
except (httplib.HTTPResponse, socket.error) as ex:
    print("Unable to connect to the server:", ex)
    sys.exit(1)

r1 = conn.getresponse()

if r1.status == 404:
    print("Command string not found.")

elif r1.status == 500:
    print("The server gives the 500 error. Please try again later.")

elif r1.status == 200:
    data = r1.read()
    if "-s" in sys.argv or "--show" in sys.argv:
    	print(data)
    else:
        os.system(data)

conn.close()
