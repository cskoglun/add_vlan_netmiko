print("\n\n *** Netmiko Configuration Script *** \n\n")

from netmiko import ConnectHandler

device = {
    'device_type':'cisco_xe',
    'ip':'IP ADDRESS', # add host information
    'username':'USERNAME', # add username
    'password':'PASSWORD', # add password
}

print("Configure vlan 20 for interface g1/0/1 - 3 and vlan 30 for interface g1/0/4 - 10 \n\n")
vlan20 = ["vlan 20", "int range g1/0/1 - 3", "description THIS PORT IS VLAN 20", "switchport mode access", "switchport access vlan 20"]
vlan30 = ["vlan 30", "int range g1/0/4 - 10", "description THIS PORT IS VLAN 30", "switchport mode access", "switchport access vlan 30"]
vlans = vlan20 + vlan30

connect = ConnectHandler(**device)
output = connect.send_config_set(vlans)

print("\n\n *** Netmiko Python Script Execution complete *** \n\n")