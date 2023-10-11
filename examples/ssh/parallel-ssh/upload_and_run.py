from pssh.clients import SSHClient

host = 'localhost'
script = 'remote.py'
client = SSHClient(host, password='vagrant')
client.copy_file(script, script)


host_out = client.run_command(f"python ./{script}")

for line in host_out.stdout:
    print(line)
for line in host_out.stderr:
    print(line)