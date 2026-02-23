#subprocess module - execute external system commands
# interact with os processess
#capture output, error and return codes
# control the process execution
# run the os level commands - linux macos windows

import subprocess

from Labsessions.day2_feb6.programs1 import result

# subprocess.run - n command and wait
# subprocess.Popen()  - run process asynchronously
#subprocess.PIPE - capture the output
#subprocess.CompleteProcess - result
# subprocess.TimeoutExpired - Timeout exeception
# subprocess.CalledProcessError - command failure

result = subprocess.run("dir", shell=True, capture_output=True,text=True)
print(result)

result = subprocess.run("ipconfig", shell=True, capture_output=True,text=True)
print(result)

result = subprocess.run("python --version", shell=True, capture_output=True,text=True)
print(result.stdout)
print(result.stderr)




