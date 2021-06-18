# https://github.com/ParallelSSH/parallel-ssh
from pssh.clients import SSHClient

host = 'localhost'
cmd = 'uname'
client = SSHClient(host, password='vagrant')

host_out = client.run_command(cmd)
for line in host_out.stdout:
    print(line)
exit_code = host_out.exit_code
