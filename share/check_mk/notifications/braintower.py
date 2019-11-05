#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# Braintower SMS Gateway

import sys, os, urllib
import htmllib
import requests

# user with permission to use Web-API of gateway
username    = os.environ.get("NOTIFY_PARAMETER_USERNAME")
password    = os.environ.get("NOTIFY_PARAMETER_PASSWORD")
hostnames   = os.environ.get("NOTIFY_PARAMETER_HOSTS")
to          = os.environ.get("NOTIFY_CONTACTPAGER")
contact     = os.environ.get("NOTIFY_CONTACTNAME")
message   = "[HOST] " + os.environ['NOTIFY_HOSTNAME'] + " "

print os.environ

if hostnames == None:
    sys.stdout.write("No braintower hostname given. Please configure the hostname in the notification settings.\n")
    sys.exit(1)

if to == "":
    sys.stdout.write("The user %s has no phone number configured.\n" % contact)
    sys.exit(1)

hostnames = hostnames.split()

if os.environ['NOTIFY_WHAT'] == 'SERVICE':
    # Service notification
    message += "[SERVICE] " + os.environ['NOTIFY_SERVICESTATE'] + ": "
    message += os.environ['NOTIFY_SERVICEDESC'] + " - "
    message += os.environ['NOTIFY_SERVICEOUTPUT']
else:
    # Host notification
    message += "is " + os.environ['NOTIFY_HOSTSTATE']

for hostname in hostnames:
    url = "http://%s/api.php?" % hostname + urllib.urlencode([
        ("username", username),
        ("password", password),
        ("to",       to      ),
        ("text",     message )
    ])

    try:
        handle = urllib.urlopen(url)
        response = handle.read().strip()

        if handle.getcode() == 200:
            status = requests.get("http://"+hostname+"/check.php?option=state").text
            if ("Blocked" in status) or ("Trouble" in status) or ("Unknown" in status):
                sys.stdout.write("The braintower gateway %s seems to have an error: %s\n" % (hostname, status))
            else:
                sys.stdout.write("Successfully sent SMS to %s\n" % to)
                sys.exit(0)
        else:
            sys.stdout.write("HTTP Error sending SMS to %s: HTTP error code %s\n" % (to, handle.getcode()))
            sys.stdout.write("URL was %s\n" % url)
    except Exception, e:
        sys.stdout.write("Error sending SMS to %s via %s: %s\n" % (to, hostname, e))

sys.stdout.write("CRITICAL ERROR - No gateway for sending SMS has responded with an OK state!\n")
sys.exit(1)
