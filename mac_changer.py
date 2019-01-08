import subprocess
import argparse
import re


def change_mac(interface, mac_addr):
    print('[+] Changing mac address of interface {0} with {1}'.format(interface, mac_addr))
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac_addr])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])
    ifconfig_out = subprocess.check_output(['ifconfig', interface])
    changed_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_out)
    print('[+] Mac successfully changed to {0}'.format(changed_mac.group(0)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', dest='interface', help='Interface')
    parser.add_argument('-m', '--mac address', dest='mac', help='Mac address')
    args = parser.parse_args()
    if args.interface is not None and args.mac is not None:
        change_mac(args.interface, args.mac)
    else:
        print('[-] Enter the arguments\n')
        print(parser.print_help())
