# subprocess module allows to run external commands
import subprocess

# to run any command
subprocess.run('dir',shell=True)
# dir command is passed into the shell, so we need to set sheel=true

p = subprocess.run(['dir', 'la'],shell=True) #adding arguments to directory
print(p) #completed prcess object 
print(p.args) #tells arguments passed
print(p.returncode) #tells error in the program

# to print standard output, which is the actual output of the directory
p1 = subprocess.run(['dir','la'], capture_output=True)
print(p1.stdout) #this give standard output after capturing
# output is in bytes, so to get rid of it 
print(p1.stdout.decode()) #way1
# way2: also by adding text=true in p1

p2=subprocess.run(['cat','Learning Python/21subproces.txt'], capture_output=True)

