import time
import nmap
from rich.console import Console

con = Console()

def show(host,result):
    con.print(host,result)
nm = nmap.PortScannerAsync()
nm.scan(hosts="5.9.157.157",arguments='-sV -A -p 1-1024',timeout=10,callback=show)
while nm.still_scanning():
    con.print("waiting..")
    time.sleep(2)
# con.print(res)