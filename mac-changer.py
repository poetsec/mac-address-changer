#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # code to handle error
        parser.error("[-] Please specify an interface. Use --help for more info.")
    elif not options.new_mac:
        # code to handle error
        parser.error("[-] Please specify a new MAC. Use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    # bring interface down
    subprocess.call(["ifconfig", interface, " down"])
    # change mac address to the address you would like to use
    subprocess.call(["ifconfig", interface, " hw", " ether", new_mac])
    # enable mac address
    subprocess.call(["ifconfig", interface, " up"])

options = get_arguments()
# change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
if mac_address_search_result:
    print(mac_address_search_result.group(0))
else:
    print("[-] Could not read MAC address.")