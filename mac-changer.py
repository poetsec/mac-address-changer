#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    # bring interface down
    subprocess.call(["ifconfig", interface, " down"])
    # change mac address to the address you would like to use
    subprocess.call(["ifconfig", interface, " hw", " ether", new_mac])
    # enable mac address
    subprocess.call(["ifconfig", interface, " up"])

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")

(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)