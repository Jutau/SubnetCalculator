# SubnetCalculator
A Python Tool for Calculating Subnet Masks


Features
Supported IP Versions: Handles both IPv4 and IPv6 addresses.
Input Format: Accepts IP addresses with subnet masks or prefix lengths (e.g., 192.168.1.10/24 for IPv4 or 2001:db8::1/64 for IPv6).

Calculations:
Network Address: The base address of the subnet.
Broadcast Address (IPv4): The last address in the subnet, used for broadcasts.
Last Address (IPv6): The final address in the subnet (no broadcast in IPv6).
Host Range: The range of usable host addresses.
Number of Hosts: The count of usable host addresses.
IPv4-Specific Features:
Subnet Mask: Displayed in dotted decimal notation (e.g., 255.255.255.0).
Wildcard Mask: The inverse of the subnet mask, useful for configurations like ACLs.
Binary Representation: Optional display of IP, mask, network, and broadcast addresses in binary.

Special Cases:
For IPv4 /31 and /30, correctly handles point-to-point links and small subnets.
For /32 (IPv4) and /128 (IPv6), recognizes single IP addresses with no host range.
User Experience:
Interactive command-line interface with clear prompts.
Error handling for invalid inputs.
Option to perform multiple calculations in one session.

How to Use
Run the Program: Execute the script in a Python environment.
Enter Input: Provide an IP address with its mask or prefix when prompted (e.g., 192.168.1.10/24 or 2001:db8::1/64).
View Results: The program displays the calculated subnet information.
For IPv4: Choose whether to see binary representations.
Repeat or Exit: Decide to perform another calculation or exit.
