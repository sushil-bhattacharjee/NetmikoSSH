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

from netmiko import ConnectHandler
router = {
    'device_type': 'cisco_xr',
    'host': '10.1.10.80',
    'username': 'sushil',
    'password': 'sushil'
}
conn = ConnectHandler(**router)
conn.find_prompt()
output = conn.send_config_from_file('xr_ospf_mpls.cfg')
print(output)
output = conn.send_config_set(['root'])
print(output)
output = conn.send_config_from_file('xr_vrf_bgp.cfg')
print(output)
output = conn.commit()
print(output)

#output = conn.send_command(command_string="show configuration failed")
#print(output)
output = conn.exit_config_mode()
print(output)
conn.disconnect()
