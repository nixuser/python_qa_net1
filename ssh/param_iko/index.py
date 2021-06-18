import paramiko


HOST = "192.168.1.93"
# Add ssh key of client to authorized_keys

ssh = paramiko.SSHClient()
# ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username="ubuntu", port=22)

stin, stout, ster = ssh.exec_command("touch file2.py")
# stin, stout, ster = ssh.exec_command("ls -la")
print(stout.read().decode("utf-8"))

if ssh is not None:
    # Needs to prevent gc error
    # https://github.com/paramiko/paramiko/issues/1078
    ssh.close()
    del ssh, stin
