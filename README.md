# **Liquid Rocket Engine Cooling Simulation**

# NASA CEA
The implemented class calls NASA CEA via RocketCEA.

# INSTALL GUIDE
### In progress install instructions for rocketcea on WSL (Ubuntu) on Windows

- Setup WSL
  - download and install Ubuntu `https://ubuntu.com/wsl`

- Setup visual output on WSL
  - download and install xming `https://sourceforge.net/projects/xming/`
  - Do the following in Ubuntu terminal
    - `nano ~/.bashrc`
    - `# add the following line to the end of that file`
    - `export DISPLAY=:0`
    - `# to exit Ctrl-X, and save file`

- Setup miniconda as a python 3.x distro and a package manager
  - Do the following in Ubuntu terminal
    - `sudo apt install wget`
    - `cd`
    - `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
    - `install from command line`
  - make sure to know how to open "base" conda virtual environment
  - conda activate base

- Setup dependencies
  - `sudo pip install numpy`
  - `sudo pip install matplotlib`
  - `sudo apt install gfortran`
  - `sudo pip install rocketcea`

- Test installation
  - Do the following in Ubuntu terminal
    - `python -c "from rocketcea.cea_obj import CEA_Obj; C=CEA_Obj(oxName='LOX', fuelName='LH2'); print(C.get_Isp())"`
  - Expected ouput
    - `374.30361765576265`

## NOTES
- you can access all your windows files by doing:
  - `cd /mnt/c/`

- If the above does not work then try the following
  - you can use a symbolic link, for info about this look at point "5. Create a link from your WSL to your C drive" in the following link
`https://janelbrandon.medium.com/a-guide-for-using-wsl-for-development-d135670313a6`
