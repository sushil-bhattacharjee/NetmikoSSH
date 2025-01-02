# Import ConnectionHandler class from Netmiko library
from netmiko import ConnectHandler
# Define PE1 connection information
pe1 = {'device_type': 'cisco_xr', 'host': '10.1.10.80', 'username': 'cisco', 'password': 'cisco'}
# Start a connection to PEl router
conn = ConnectHandler(**pe1)
# Find the EXEC mode prompt
conn.find_prompt ()
# Send EXEC command to router
output = conn.send_command("show ip interface brief")
# Display router response
print('\nshow ip interface brief...\n')
print (output)
# Send EXEC command to router
output = conn.send_command("show cdp neighbors detail")
# Display router response
print('\nshow cdp neighbors detail...\n')
print (output)
# Send EXEC command to router
output = conn.send_command ("show ospf neighbor")
# Display router response
print('\nshow ospf neighbor...\n')
print (output)
# Send EXEC command to router
output = conn.send_command("show mpls ldp neighbor brief")
# Display router response
print('\nshow mpls ldp neighbor brief...\n')
print (output)
# Send EXEC command to router
output = conn.send_command ("show ip route")
# Display router response
print('\nshow ip route...\n')
print (output)