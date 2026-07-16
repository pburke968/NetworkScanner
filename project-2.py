from icmplib import ping
online_hosts = []

def main():
    uip = int(input('''
            ================================
                    NETWORK SCANNER
            ================================

1) Scan Network
2) View Previous Scan
3) Export Results
4) Exit

                    Your Choice: '''))
    if uip == 1:
        scan()
        
    elif uip == 2:
        view()
    
    elif uip == 3:
        export()

    elif uip == 4:
        quitP()

    else:
        print(f"Please select a valid option")
        main()

def scan():
        netwrk = input("Please enter the network you would like to scan (example: 192.168.1): ")
        for i in range(1,256):
            host = (f"{netwrk}.{i}")
            result = ping(host, count=1)
            if result.is_alive:
                print(f"Online {host} {result.avg_rtt} ms")
                online_hosts.append(host)
            else:
                print(f"No response from {host}")
        print("\nSCAN COMPLETE!")
        print("To view results, select 'View Previous Scans' from the main menu.")
        main()

def view():
    print("Previous Scan:")
    if not online_hosts:
        print("You need to run the scan first")
        main()
    else:
        for hosts in online_hosts:
            print(hosts)
    uip = input("Please enter to return to the main menu")
    if uip == "": 
        main()


def export():
    pass

def quitP():
    exit()

main()