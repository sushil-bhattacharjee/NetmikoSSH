# send_command: Sends EXEC mode commands to the device and returns output. This function accepts a string that contains the EXEC command as argument.

# send_config_set: Sends configuration commands to the device. This function accepts a list of strings that contain configuration commands to send to the device.

# send_config_from_file: Sends configuration commands that you load from a file. This function accepts a string of the path to the file.

# save_config: Saves the running-config to the startup-config.

# find_prompt: Returns the current router prompt.

# commit: Executes a commit action on Cisco IOS XR devices.

# disconnect: Closes the connection to the device.

from netmiko import ConnectHandler
from rich import print as rprint

device = {
    "device_type": "cisco_xe",
    "host": "10.1.10.77",
    "username": "sushil",
    "password": "sushil",
}


configuration_commands = [
    "router ospf 1",
    "router-id 10.10.1.1",
    "network 0.0.0.0 255.255.255.255 area 0"
]

with ConnectHandler(**device) as conn:
        output1 = conn.send_config_set(config_commands=configuration_commands)
        print(output1)

show_commands = ["sh run | s router ospf", "sh run | s router bgp", "sh ip int bri", "sh run | s router isis"]

with ConnectHandler(**device) as conn:
    for command in show_commands:
        output = conn.send_command(command_string=command)
        print(output)