import ipaddress

def main():
    print("Welcome to the Subnet Calculator!")
    while True:
        try:
            # Prompt user for input
            input_str = input("\nEnter IP address with mask or prefix (e.g., 192.168.1.10/24 or 2001:db8::1/64): ")
            # Create an IP interface object from the input
            interface = ipaddress.ip_interface(input_str)
            network = interface.network
            
            # Determine IP version and display results accordingly
            if interface.version == 4:
                display_ipv4_info(interface, network)
            elif interface.version == 6:
                display_ipv6_info(interface, network)
            
            # Ask if the user wants to perform another calculation
            another = input("\nPerform another calculation? (y/n): ").lower()
            if another != 'y':
                print("Thank you for using the Subnet Calculator. Goodbye!")
                break
                
        except ValueError as e:
            print(f"Invalid input: {e}")

def display_ipv4_info(interface, network):
    """Display subnet information for IPv4."""
    ip = interface.ip
    mask = interface.netmask
    prefix_len = network.prefixlen
    network_addr = network.network_address
    broadcast_addr = network.broadcast_address
    wildcard_mask = ~interface.netmask  # Bitwise NOT for wildcard mask
    
    # Calculate host range and number of hosts based on prefix length
    if prefix_len < 30:
        first_host = network_addr + 1
        last_host = broadcast_addr - 1
        num_hosts = network.num_addresses - 2
    elif prefix_len == 30:
        first_host = network_addr + 1
        last_host = network_addr + 2
        num_hosts = 2
    elif prefix_len == 31:
        first_host = network_addr
        last_host = network_addr + 1
        num_hosts = 2
    else:  # /32
        first_host = None
        last_host = None
        num_hosts = 0
    
    # Display the results
    print("\nIPv4 Subnet Information:")
    print(f"IP Address: {ip}")
    print(f"Subnet Mask: {mask} (/{prefix_len})")
    print(f"Wildcard Mask: {wildcard_mask}")
    print(f"Network Address: {network_addr}")
    print(f"Broadcast Address: {broadcast_addr}")
    if num_hosts > 0:
        print(f"Host Range: {first_host} - {last_host}")
        print(f"Number of Hosts: {num_hosts}")
    else:
        print("Host Range: None (single IP address)")
        print("Number of Hosts: 0")
    
    # Offer to display binary representations
    if input("\nDisplay binary representations? (y/n): ").lower() == 'y':
        display_binary(ip, mask, network_addr, broadcast_addr)

def display_ipv6_info(interface, network):
    """Display subnet information for IPv6."""
    ip = interface.ip
    prefix_len = network.prefixlen
    network_addr = network.network_address
    
    # Calculate last address and host range
    last_addr = network_addr + (network.num_addresses - 1)
    if prefix_len < 128:
        first_host = network_addr + 1
        last_host = last_addr
        num_hosts = network.num_addresses - 1
    else:  # /128
        first_host = None
        last_host = None
        num_hosts = 0
    
    # Display the results
    print("\nIPv6 Subnet Information:")
    print(f"IP Address: {ip}")
    print(f"Prefix Length: /{prefix_len}")
    print(f"Network Address: {network_addr}")
    print(f"Last Address: {last_addr}")
    if num_hosts > 0:
        print(f"Host Range: {first_host} - {last_host}")
        print(f"Number of Hosts: {num_hosts}")
    else:
        print("Host Range: None (single IP address)")
        print("Number of Hosts: 0")

def display_binary(ip, mask, network_addr, broadcast_addr):
    """Display binary representations for IPv4 addresses."""
    ip_bin = '.'.join(format(int(octet), '08b') for octet in str(ip).split('.'))
    mask_bin = '.'.join(format(int(octet), '08b') for octet in str(mask).split('.'))
    network_bin = '.'.join(format(int(octet), '08b') for octet in str(network_addr).split('.'))
    broadcast_bin = '.'.join(format(int(octet), '08b') for octet in str(broadcast_addr).split('.'))
    
    print("\nBinary Representations:")
    print(f"IP Address: {ip_bin}")
    print(f"Subnet Mask: {mask_bin}")
    print(f"Network Address: {network_bin}")
    print(f"Broadcast Address: {broadcast_bin}")

if __name__ == "__main__":
    main()
