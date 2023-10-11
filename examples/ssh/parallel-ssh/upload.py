from pssh.clients import SSHClient

host = 'localhost'
client = SSHClient(host, password='vagrant')
client.copy_remote_file('remote_filename', 'local_filename')
client.scp_recv('remote_filename', 'local_filename')
