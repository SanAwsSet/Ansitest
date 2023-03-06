from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command, netmiko_send_config

def change_hostname(task, new_hostname):
    # Use Netmiko to configure the new hostname on the device
    commands = [f"hostname {new_hostname}"]
    task.run(task=netmiko_send_config, config_commands=commands)

def main():
    # Initialize Nornir with the inventory file and any additional options
    nr = InitNornir(config_file="config.yaml")

    # Get the new hostname from user input
    new_hostname = input("Enter the new hostname: ")

    # Filter the devices to only include Cisco routers
    cisco_routers = nr.filter(platform="cisco_ios")

    # Use Nornir to execute the change_hostname function on each device in parallel
    cisco_routers.run(task=change_hostname, new_hostname=new_hostname)

if __name__ == "__main__":
    main()
