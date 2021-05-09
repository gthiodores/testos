# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import paramiko
import time
from scp import SCPClient


# Execute the compressor locally
def execute_java_program():
    command = "java -jar F:/Compressor.jar"
    print("Executing command through OS command prompt")
    returned_value = os.system(command)
    if returned_value == 0:
        print("Program exited successfully")
    else:
        print("Program did not finish successfully")


# Create an ssh client using paramiko
def create_ssh_client(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(server, port, user, password)
    return client


# Retrieve a file from the raspberry pi, record the time it took
# for the transfer to conclude and return it
def record_scp(scp, remote_path, local_path):
    start_time = time.time()
    scp.get(remote_path, local_path)
    end_time = time.time()
    return (end_time - start_time) * 1000


# Entry point of the program
def main_program():
    # Required information to make an SSH Client
    server_address = "192.168.1.8"
    port = 22
    username = "pi"
    password = "Hayate007"

    # File name to be transferred
    file_name = "img21"

    # File location in the remote server
    remote_path = f"/home/pi/skripsi/{file_name}/{file_name}.jpg"
    remote_path_compressed = f"/home/pi/skripsi/{file_name}/{file_name}Compressed.bin"

    # File transfer destination in the local server
    local_path = "C:/puttyTest/"

    # Create an SSH and SCP client
    ssh = create_ssh_client(server_address, port, username, password)
    scp = SCPClient(ssh.get_transport())

    # Record and print the transfer time of the SCP
    original_transfer_time = record_scp(scp, remote_path, local_path)
    print(f"Original file transfer time: {original_transfer_time} ms")

    compressed_transfer_time = record_scp(scp, remote_path_compressed, local_path)
    print(f"Compressed file transfer time: {compressed_transfer_time} ms")

    # Closes the connection to the SSH and SCP client
    scp.close()
    ssh.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_program()
