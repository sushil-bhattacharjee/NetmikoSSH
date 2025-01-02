# Import ConnectionHandler class from Netmiko library
from netmiko import ConnectHandler
# Define PE3 connection information
pe3 ={'device_type': 'cisco_ios', 'host': '10.1.10.77', 'username': 'cisco', 'password': 'cisco' }
# Start a connection to PE3 router
conn = ConnectHandler(**pe3)
# Find the EXEC mode prompt
conn.find_prompt ()
# Send EXEC command to router
output = conn.send_command("show ip interface brief")
# Display router response
print('\nshow ip interface brief.....\n')
print(output)
# Send EXEC command to router
output = conn.send_command("show cdp neighbors detail")
# Display router response
print('\nshow cdp neighbors detail.....\n')
print(output)
# Send EXEC command to router
output = conn.send_command("show ip ospf neighbor")
# Display router response
print('\nshow ip ospf neighbor.....\n')
print(output)
# Send EXEC command to router
output = conn. send_command("show vrf")
# Display router response
print('\nshow vrf.....\n')
print(output)
# Send EXEC command to router
output = conn.send_command("show ip route")
# Display router response
print('\nshow ip route.....\n')
print(output)