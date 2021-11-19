#/bin/bash!
###adjust_task
#Ensure script run as root or user with privilege

if [ "$EUID" -ne 0 ]
  then echo "Please run as privileged user,because we need to install some packages on your system."
fi



#Ensure python  is installed on your system

if ! hash python; then
    echo "python is not installed"
    exit 1
fi

ver=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
if [ "$ver" -lt "30" ]; then
    echo "This script requires python 3.0 or greater.Please install python 3.0 or greater. if you have another version of python on your system you can change with update-alternatives --config python, befor do this command please do [ update-alternatives --install /usr/bin/python python /usr/bin/python3.6 3]&[update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2]"
    exit 1
fi

#Ensure the PIP package install in your system
if ! hash pip-3; then
    echo "pip is not installed,in order to install some module you need to manage via pip"
 while true; do
   read -p "Do you wish to install this (pip)program?" yn
   case $yn in
        [Yy]* ) yum install epel-release python-pip -y; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
 done
fi
sleep 10
### install requirment of python
python3 -m pip install -r requirements.txt --user
#####
echo "All configuration have already done. now you can run fstab change program now. be careful any manipulation with out knowledge  in fstab file will cause damage to your system."
