import subprocess
from fabric import Connection

command = "ping boeing.com"

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

while True:
  output = process.stdout.readline()
  if output == '' and process.poll() is not None:
    break
  if output:
    print(output.strip())

# c = Connection(
#   host='192.168.68.60',
#   user='scott',
#   port=22,
#   connect_kwargs={"key_filename": "/home/scott/.ssh/id_ed25519"}
# )
# print(c.run('hostname'))
# print(c.run('uname -s'))

