import subprocess

subprocess_command = "python fabric_script.py"

process = subprocess.Popen(subprocess_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

while True:
  output = process.stdout.readline()
  if output == '' and process.poll() is not None:
    break
  if output:
    print(output.strip())