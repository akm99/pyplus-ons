import yaml
from getpass import getpass
from concurrent.futures import ThreadPoolExecutor, wait
from netmiko import ConnectHandler


MAX_WORKERS = 3


def load_devices():
    with open("netmiko.yml") as f:
        devices = yaml.load(f)
    return devices


def ssh_task(device):
    print(f"Thread Started: {device['host']}")
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip arp")
    return {
        "name": device["host"],
        "output": output
    }


def main():
    password = getpass()
    devices_dict = load_devices()
    pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    futures = []
    for device_name, conn_dict in devices_dict.items():
        conn_dict["password"] = password
        print(f"Working on: {device_name}")
        futures.append(pool.submit(ssh_task, conn_dict))

    wait(futures)

    for task in futures:
        result = task.result()
        hostname = result["name"]
        output = result["output"]
        print()
        print("-" * 80)
        print(f"{hostname}:\n\n{output}")
        print("-" * 80)
        print()


if __name__ == "__main__":
    main()
