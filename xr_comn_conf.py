# send_command: Sends EXEC mode commands to the device and returns output. 
# This function accepts a string that contains the EXEC command as argument.

# send_config_set: Sends configuration commands to the device. 
# This function accepts a list of strings that contain configuration commands to send to the device.

# send_config_from_file: Sends configuration commands that you load from a file. 
# This function accepts a string of the path to the file.

# save_config: Saves the running-config to the startup-config.

# find_prompt: Returns the current router prompt.

# commit: Executes a commit action on Cisco IOS XR devices.

# disconnect: Closes the connection to the device.
# exit_config_mode: exit from the config

#Import ConnectionHandler class from Netmiko Library
from netmiko import ConnectHandler
#Define configuration commands as a list
common_config = [
    'clock timezone AEST Australia/Sydney',
    'logging console warning',
    'cdp',
    'ntp server 10.1.10.101',
    'tftp client source-interface MgmtEth0/RP0/CPU0/0',
]
# Define Device connection information
my_device = {
    'device_type': 'cisco_xr',
    'host': '10.1.10.80',
    'username': 'sushil',
    'password': 'sushil'
}

# Start a connection to the router
conn = ConnectHandler(**my_device)
# Find the EXEC mode prompt
conn.find_prompt()
# Send the configurations config to the router
output = conn.send_config_set(common_config)
# Display router response to each command
print(output)
# Commit configuration changees in XR router
output = conn.commit()
# Return to EXEC mode
output = conn.exit_config_mode()
# Display router response
print(output)
# Close connection
conn.disconnect()