from fabric import Connection

def ssh_command(host, username, pathtokey, command):
  with Connection(
    host,
    user=username,
    port=22,
    connect_kwargs={"key_filename": pathtokey}) as c:
    result = c.run(command)
    return result

host = "192.168.68.60"
username="scott"
pathtokey="/home/scott/.ssh/id_ed25519"
command = "ping boeing.com"

output = ssh_command(host, username, pathtokey, command)
print(output)