from netmiko import ConnectHandler
from rich import print as rprint
my_device1 = {
    "device_type": "cisco_ios",
    "host": "10.1.10.77",
    #"host": "10.1.10.22",
    "username": "sushil",
    "password": "sushil",
}
commands = [
    "router ospf 100",
    "router-id 1.1.1.1",
    "network 0.0.0.0 0.0.0.0 area 0"
]

with ConnectHandler(**my_device1) as conn:
    output = conn.send_config_set(config_commands=commands)
    conn.save_config()
print(output)
