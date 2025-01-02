from netmiko import ConnectHandler
from rich import print as rprint
my_device1 = {
    "device_type": "cisco_ios",
    "host": "10.1.10.77",
    #"host": "10.1.10.22",
    "username": "sushil",
    "password": "sushil",
}
#Textfsm converts text data to dictionary data
#Textfsm is open source and genie is built by cisco
#To use genie it requires to install pyats and genie
with ConnectHandler(**my_device1) as conn:
    output = conn.send_command(command_string="show version", use_textfsm=True)
    rprint(output)
    print()
    rprint(output[0]['version'])
    print()
    rprint(output[0]["serial"][0])
    
#Folloing example made with genie
with ConnectHandler(**my_device1) as conn:
    output = conn.send_command(command_string="show version", use_genie=True)
    rprint(output)
    print()
    rprint(output['version']['platform'])
    print()
    rprint(output['version']['uptime'])
