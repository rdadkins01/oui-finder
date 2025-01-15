# oui-finder

Created for the purposes of finding a vendor OUI straight from the CLI or within another script without needing to use a web browser.

This script pulls from Wireshark's public OUI data at "https://www.wireshark.org/download/automated/data/manuf.gz". 

This script could instead have used a public API to retrieve OUI data each time it is run. I opted to download it instead to avoid having to send a query to the Internet if the data has already been downloaded. This means you only initially need an Internet connection.

Some notes on the format the MAC address is provided in. This script expects a 12 character MAC at the moment. It also only accepts colons (:) and periods (.) as delimiters. However, you can provide a mix of colons and periods in any position and they will be stripped. For example, ".FC:F.E:C:2.000.000:" is accepted.

### Usage
'''Python
usage: main.py [-h] [-s] macaddress

positional arguments:
  macaddress   Enter the mac address to be queried.

options:
  -h, --help   show this help message and exit
  -s, --short  Returns short vendor name
'''

### Example
'''Python
python3 main.py FC:FE:C2:00:00:00 -s
InvensysCont
'''

'''Python
python3 main.py FC:FE:C2:00:00:00
Invensys Controls UK Limited
'''
