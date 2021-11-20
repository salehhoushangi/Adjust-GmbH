# Adjust-GmbH



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://a.storyblok.com/f/47007/850x283/4ceff16f7e/adjust_logo_black.png">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Adjust-GmbH</h3>

  <p align="center">
   adjust challange for Platform engineer opportunity!
    <br />
  </p>
</div>







<!-- ABOUT THE PROJECT -->
## About The Project
Creating a utility to process that YAML and output an /etc/fstab file based on
that yaml.
Please provide your code along with a README describing the use. The code will
form part of the future conversations you will have with the hiring team.
You are free to use languages and environments regarding a system of your choice
but the tasks must run on a Linux system.
Note: You should use a programming/scripting language to achieve this task, and
not Ansible or such.


Suppose we have a YAML file describing the mount points of a system as follows.
```yaml
fstab:
  /dev/sda1:
    mount: /boot
    type: xfs
  /dev/sda2:
    mount: /
    type: ext4
  /dev/sdb1:
    mount: /var/lib/postgresql
    type: ext4
    root-reserve: 10%
  192.168.4.5:
    mount: /home
    export: /var/nfs/home
    type: nfs
    options:
     - noexec
     - nosuid
```

### Built With

python3.0 or greater 



<!-- GETTING STARTED -->
## Getting Started

To setup some Prerequisites please run  install_requirments.sh
### Prerequisites

To start befor running fstab_change pyhton program make sure you have pyhton 3.0 or greater

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/salehhoushangi/Adjust-GmbH.git
   ```
2. Run install_requirments.sh shellscript
   ```sh
   sudo bash install_requirments.sh 
   ```
3. Run ftsab_change with pyhton on your system
   ```sh
   pyhton fstab_change.py
   ```



<!-- USAGE EXAMPLES -->
## Usage

This program is be used to read configration from yaml file then write it in /etc/fstab file 




<!-- ROADMAP -->
## Roadmap

- [ ] Add Changelog
- [ ] Add Automation mount or remount after change






<!-- LICENSE -->
## License

Distributed under the Adjust License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

 salehstu8dentl@gmail.com

Project Link: [https://github.com/salehhoushangi/Adjust-GmbH]




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments







