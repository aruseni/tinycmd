#!/usr/bin/env python

# The web server host
tinycmd_host = "tinycmd.org"

usage = """
tinycmd.org
The command string shortening service.

Usage: t [command_string_id]
"""

import os, sys
import httplib, socket

if len(sys.argv) != 2:
    print usage
    sys.exit(1)

if sys.argv[1] in ('--usage', '--help', '-h'):
    print usage
    sys.exit(1)
try:
    conn = httplib.HTTPConnection(tinycmd_host)

    # The URL returns the command string as plain/text
    conn.request("GET", "/cs/%s/text/" % sys.argv[1])
except (httplib.HTTPResponse, socket.error) as ex:
    print "Unable to connect to the server:", ex
    sys.exit(1)

r1 = conn.getresponse()

if r1.status == 404:
    print "Command string not found."

elif r1.status == 500:
    print "The server gives the 500 error. Please try again later."

elif r1.status == 200:
    data = r1.read()
    os.system(data)

conn.close()
