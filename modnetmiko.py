from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.194.5',  #Your Server IP
    'username': 'syahmi', #your Server Username
    'password': 'syahmirn52', #your server password
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('sudo apt-get update')
print (output)
