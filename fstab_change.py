__author__      = "Saleh Houshangi"
__copyright__   = "Copyright @Adjust.co"

import yaml
from shutil import copyfile
import os
import sys
import subprocess
## read yaml file and convert to dic
with open("fstab.yaml", 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

## get the all key of fstab distionary and convert dictionary to the lsit in order to access the items of dictionary
for index, i in enumerate(list(data.get('fstab'))):
    globals()["var" + str(index+1)] = i
#####Set default option and default check for mount point 

default_option = "default"
default_check = "0 0"
#storing all options value of each  source mount point
sda1_mount = (data.get('fstab').get(var1).get('mount'))
sda1_type = (data.get('fstab').get(var1).get('type'))
sda2_mount = (data.get('fstab').get(var2).get('mount'))
sda2_type = (data.get('fstab').get(var2).get('type'))
sdb1_mount = (data.get('fstab').get(var3).get('mount'))
sdb1_type = (data.get('fstab').get(var3).get('type'))
ip_mount = (data.get('fstab').get(var4).get('mount'))
ip_export = (data.get('fstab').get(var4).get('export'))
ip_type = (data.get('fstab').get(var4).get('type'))
ip_options = ' '.join(data.get('fstab').get(var4).get('options'))

##check user to be root before doing any change in fstab
def prompt_sudo():
    ret = 0
    if os.geteuid() != 0:
        msg = "[sudo] password for %u:"
        ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
    return ret

if prompt_sudo() != 0:
   sys.exit("This program need 'sudo'")

####creat backup of fstab file
prompt_sudo ()
copyfile('/etc/fstab','/etc/fstab.back')
#edit fstab file and write to it!
exec_fstab = [var1 +'  '+ sda1_mount +'  '+ sda1_type + '    '+ default_option + '   '+default_check , var2 +'  '+ sda2_mount +'  '+ sda2_type + '    '+ default_option + '   '+default_check, var3 +'  '+ sdb1_mount +'  '+ sdb1_type + '    '+ default_option + '   '+default_check, var4 +':'+ ip_export +'  '+ ip_mount + '    '+ip_type+'  '+ ip_options  + '   '+default_check ]
with open("/etc/fstab" , 'w') as f :
    f.write("\n".join(map(str,exec_fstab)))


#### Open file read only for check 
f = open("/etc/fstab", "r")
print(f.read())
