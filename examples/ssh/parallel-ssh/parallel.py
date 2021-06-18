rom pssh.clients import ParallelSSHClient

hosts = ['localhost', 'localhost']
client = ParallelSSHClient(hosts, password='vagrant')

output = client.run_command('uname')
for host_output in output:
    for line in host_output.stdout:
        print(line)
    exit_code = host_output.exit_code
