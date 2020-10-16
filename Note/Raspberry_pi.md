# Raspberry_pi.md

- [Raspberry_pi.md](file:///C:/Local/Work/ML_Name/Note/Raspberry_pi.md) 

[](#)
## DONE

- [x] Study Raspberry Pi [P_4][v_3] [07-07]
- [x] Read web server setup [](#my-web-server) [07-07]
  - [x] two documents.
 -  [x] buy a super cheap sd_card from top heatter.- [∞](#sd_card-purchase-) 
    - for Raspberry pi door monitor project 
- [x]  buy 64G scandisk drive [Link](#search-for-raspberry-pi-zero-monitor)
- [x] Purchase pi zero & Camera
  - [∞](#purchase-pi-zero--camera)

- [x]  Raspberry pi 4 Camera motioneye
  - [∞](#raspberry-pi-4-camera-motioneye)

- [x] Raspberry pi zero w Camera motioneye 
 
## Todo

- [ ] Raspberry pi zero Camera HW install: 
  -  [∞](#pi-boot-up-install)

- [ ]  Pi 4 Open CV
  - [steps](#smart-security-camera)   
  - [hwo_to](#pi-4-open-cv)
  - [fix_tensor_flow](#fix_tensor_flow)

- [ ] set up actual webpage in Raspberry pi
  - [ ] run simple streamlit work in Raspberry pi :
    - [ ] show publishable web-essential extractor.
 
 -  [ ] check and collect information on the Raspberry pi 

## Objective

- Use of Raspberry_Pi to develop
  - web_server to as free NLP service.
  - object detection for NN study.

- [Raspberry_pi.md](file:///C:/Local/Work/ML_Name/Note/Raspberry_pi.md#raspberry-pi-4-camera-motioneye) 


### Roadmap

[25-06] - [07-07]

- build Raspberry_Pi project in 10 days. [Done]

  - brought a Raspberry pi CanaKit set :
  - Boot up the system.
  - Able to run basic web page.
  - Enabled the remote control: ssh

- [07-07] - [17-07]
  - Boot up a real website : put online
  - Run data science project : article
  - run background scraping of amazon:

## Question :

## About Raspberry pi : Introduction

### One liner

    - 35 USD
    - System on broad
    - Linux computer : Ubuntu system 
    - Many system ports
    - Many Hardware applications

### What is Raspberry pi

  The Raspberry Pi is a **low cost**, credit-card sized computer that plugs into a computer monitor or TV, and uses a standard keyboard and mouse. LINUX based

  It is a capable little device that enables people of all ages to explore computing, and to learn how to program in languages like Scratch and Python

### As a hobby , Raspberry Pi

    - be a simple web server to demonstration of key NLP services.
      - Name identification.
      - Amazon
    - always online and provide my service.
    - Other hobby.

## Content

### Basic information

#### Hardware specs

##### Raspberry_Pi 4

- [Spec Link :](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/specifications/)

- Broadcom BCM2711,
  - **Quad core** Cortex-A72 (ARM v8) 64-bit SoC @ **1.5GHz**
-
- 2 × micro-HDMI port

- [spec lists](https://www.raspberrypi.org/products/)

  - Raspberry_Pi 0 :
  - Raspberry_Pi 1
  - Raspberry_Pi 2
  - Raspberry_Pi 3

#### Software

- Raspian : debian based linux
- full desktop system

#### Price

- Raspberry pi 4 broad : From \$35
- full Canakit:
  - Raspberry pi 4,
  - 4GB RAM
  - 32GB Memory drive
  - Case.
  - 99 USD

### Core use case

- [15 Great Uses for a Raspberry Pi | Tom's Guide](https://www.tomsguide.com/us/pictures-story/1446-uses-for-raspberry-pi.html)

- - **Web server**
  - Laptop
  - Kids' first computer
  - Home theater PC
  - Wi-Fi extender
  - **Network-attached storage drive**
  - **Security Camera**
  - Music streamer with multi-room audio

* Web server
  - less power consumption.

## Hardware

### Hardware Purchasing

  #### Objective

  - Purchase optimal Hardware by comparing different offering from different sites

  Raspberry pi 4 : Price : \$35

    - Raspberry_Pi 0 : 5 USD
    - Raspberry_Pi 1 :
    - Raspberry_Pi 2
    - Raspberry_Pi 3 : 35 USD

  #### Summary

    Purchase list : done

    - Raspberry pi 4 [Purchase]
    - sd card [Have]
    - usb cable [Have]
    - internet cable [have]

  #### Amazon

  #### eBay

  #### hobby site.

- [Raspberrypi home site](https://www.raspberrypi.org/products/)


# System 

## Set up the raspberry pi system.

### Install twisteros :  

  #### Objective 

    1. have both mac and windows UI 
    2. 
  #### what

  1. Twister OS is a `Raspberry Pi OS-based Linux` distro for the RasPi. 
    2. Its name derives from its ability to seamlessly switch between two different desktop environments, one that emulates Windows 10 and the other which appears like macOS.
    3.  Although Twister OS is a small project hailing from a single developer, 
        1.  unlike Raspberry Pi OS, 
        2.  Canonical's Ubuntu, 
        3.  or Manjaro Linux, 
    4. it's an incredibly detail-oriented and polished operating system.

  #### Hwoto
    1. download xz file : 
       - [Twister OS](https://twisteros.com/downloads.html)
     2.  Using Etcher, I was able to mount the TwisterOS.xz straight to my microSD card. 
        - [flash OS](https://www.balena.io/etcher/)

  ##### Reference . 
    - [Getting Started with Twister OS on Raspberry Pi](https://www.electromaker.io/tutorial/blog/getting-started-with-twister-os-on-raspberry-pi)
    - [Twister OS](https://twisteros.com/downloads.html)


### App Installation 
  #### apt-get and pip install 
    - apt-get: for linux system install 
    - pip : install 


### Python lib installation 

  1. Question: where is the rpi original installiation 
    setup in the libary directory . 
    in ~/.bashrc
    export PYTHONPATH="$PYTHONPATH/usr/lib/python3/dist-packages" 

  2. how to set up 

### Editing bashrc
  ~/.bashrc
  goto bash quickly : ebash
  add python3 to py: 
###  Raspberry pi connection setup  

  #### Value
  [10_min] [Priority_4]  [Difficulty_5] [Importance_4]  
  #### Objective 
   1. setup connection between PC and Raspberry pi
  #### Howto
  1. PC -> vnc : myip.sh : get the : ip 
  2. PC -> Ubuntu : -> ssh pi@192.168.1.xx 


### Raspberry pi remote accessing

##### wifi client IPS : SSH access

- - 1. raspberrypi: ip : 192.168.1.6
    2. ssh pi@192.168.1.6
    3. password for pi : tangwin/

#####  wifi client IPS : SSH access

- [linux - ssh connection refused on Raspberry Pi - Stack Overflow](https://stackoverflow.com/questions/41318597/ssh-connection-refused-on-raspberry-pi)


- enable ssh : 
  - - in the Raspberry pi : 
  - From the terminal with raspi-config
        - Enter sudo raspi-config in a terminal window
        - Select Interfacing Options
        - Navigate to and select SSH
        - Choose Yes
        - Select Ok
        - Choose Finish

- in the Raspberry pi : 
  - hostname -I : find the ip address : 
  - 

- SSH into your Raspberry Pi
Default Username and Password is: username: pi. password: raspberry
NOTE : 
  1. It changes from time to time, go to the 192.168.1.1 and find the latest ip address. 

##### VNC access :

- - 1. Install VNC in windows.
    2. run VNC connection 192.168.1.6

####   Transfer files pi 
#### what
  - - transfer files pi between in local wifi network Raspberry pi
#### hwoto
   - filezilla : in windows 10 
   - Get the 

#### Fix the ip of Raspberry pi
#### what
  - - Howto Fix the ip of Raspberry pi
    192.168.1.24
raspberry

##### Reference 


- [Provide Raspberry Pi with a static IP address - IONOS](https://www.ionos.com/digitalguide/server/configuration/provide-raspberry-pi-with-a-static-ip-address/)


#### change the password of pi 
  

### Vscode Sync setting :  PC and RPI  
  Basic vscod 
 `settings` 
 `keybiding` 
  #### Objective 
  - Sync the setting file between `PC and Raspberry pi`
    - find glob in 
    - sync the 3 setup files 
    - installed vscode list : 


  ##### find globle in 
      1. Where is the globals folder in rpi
          settings :  
              ~/.config/Code - OSS (headmelted)/User/settings.json 

          keymappings :
              ~/.config/Code - OSS (headmelted)/User/keybindings.json
          vs snip : 
              snippet : 
                  /home/pi/.config/Code - OSS (headmelted)/User/snippets
      
      2. Download the git in 

      3. Copy and paste 


### Git Edit Actions : Edit in PC and run in Raspberry pi

  [10_min] [Priority_4]  [Difficulty_5] [Importance_4]   

  #### Objective 
    1. Edit in `PC` and run in `Raspberry pi`
    
    2. make powershell file to : 
        1. `Raspberry pi` :  download from git : 
        2. `PC`: upload from PC : 
    

    3. Change all repo into : 

  #### Result

    1. PC : git_web.ps1
    2. Raspberry pi : cd web ; download_web

### Start-up raspberry pi program 

  - [Five Ways to Run a Program On Your Raspberry Pi At Startup](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)
  - run : st.sh in sh 

### VPN : Nordvpn install in rpi : 

    ##### what
      - [Installing and using NordVPN on Debian, Ubuntu, Elementary OS, and Linux Mint | NordVPN Customer Support](https://support.nordvpn.com/Connectivity/Linux/1325531132/Installing-and-using-NordVPN-on-Debian-Ubuntu-Elementary-OS-and-Linux-Mint.htm)

    ##### Setup 
      1. download : 
      https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
      2. sudo apt-get update
      3. nordvpn login
      4. nordvpn connect

### send a email via python. 

  #### what 

    1. Use of yagmail 
    2. oneliner command line to send a 

  #### hwoto 

    1. see semail.py : 
      ~/web/django-todo-react/backend/todo 
    2. set up gmail less secure app. 

  #### Result 
    1. run : python3 semail.py "boidk  slsk"

  #### Get a email 
    no such function 

# Projects

## One liner

    1. My Web server for ML projects. DONE 
    2. Smart Camera Monitor : OpenCV pi 
    3. Tensorflow object detection

## My Web server

### find a introduction work 

#### shutdown

- - - sudo shutdown -h now


## Raspberry pi 4 Camera motioneye
DONE

#### Reference
   [Raspberry Pi Zero W Surveillance Camera](https://www.youtube.com/watch?v=rhIzfRmKHnQ)

  https://www.youtube.com/watch?v=Y2QFu-tTvTI&list=WL&index=59&t=440s

#### Howto 

- - 1. Flash motioneye OS into usb microsb drive.     
    2. Put the wpa configuration file into  
    3. Use remote ssh to login in to 192.168.1.23 

#### Used SW

- [flash OS](https://www.balena.io/etcher/)

NOTE : no need of camera module adapter 
 
## Pi boot up install 
  -
  - [Pi zero w bootup  access over wifi ](https://www.youtube.com/watch?v=LlCr09B2HZI)

### Raspberry pi zero Camera HW install: 

#### what

#### Howto 

  -  https://www.youtube.com/watch?v=LlCr09B2HZI
  - [Raspberry Pi Zero W and Pi Camera Application](https://tutorial.cytron.io/2017/08/16/raspberry-pi-zero-w-pi-camera-application/)
- - 1. hardware : hwo to connect the cable 
    2. 
#### Result 



## Pi Zero monitoring howto 

### Pi 4 Open CV 
  - [∞](#pi-4-open-cv)

### Objective 
- - 1. Simple project to kick of the interest 
    2. 

### Todo 
- - 1. think and solve the questions   - [∞](#question-where-to-mount-the-camera-in-kitchen-)
    2. Buy a housing for the system  

### what
- - 1. Set up a first pi project using pi zero w 
    2. monitor the kitchen 
    3. monitor front door for events 

### fix_tensor_flow 
  Currently the squre is not geting the correct person. 
  Why. 


#### User story 
##### Stage I 
  - As a user, I can monitor the kitchen to see abnormal event. 
    - Fire in the stove 
    - fridge is not closed 
  - 
##### Stage II 
  - have a web server in? 
  - Able to access remotely : web cam : 
    -   access via mobile phone 

##### Stage III 
  - check front door for events 
    - delivery  

##### Stage IV  
  - Able 
  
### Howto 
- - 1. Search for Raspberry pi in youtube DONE
    1. find the door monitor. one DONE
    2. find what is the operation system.  
    3. find How many gigabyte is needed. 
    4. Search for best solution for the monitoring solution   - [∞](#solution-candidate-survey)
        - Search key word : pi zero webcam 
        - 
    5. Solved critical tech questions:  [∞](#question-howto-set-up-the-battery-)
    

### Steps 
- - 1. Boot up the pi zero and have remote access 
    2. install the operational system 
    3. mount in right place in the kitchen

### Existing Material 
- - 1. pi zero w mother broad : 10 USD 
    2. 3 64G sd card : 10 USD each 
    3. Standard Pi camera 

##### Already Have  
  - need 64GB: install  motioneye os : 
  - need card reader. Have : with out pi 
  - power supply 
    - The device needs to be powered with a 5V power supply with a USB connector; USB-C for the Raspberry Pi 4, and micro USB for all other models.

##### Purchase pi zero & Camera

- purchase pi zero broad : 
- purchase pi camera module 
  - Candidate : 
    1. Aamzon: DORHEA Raspberry Pi Mini Camera Video Module 5 Megapixels  ($8.69)
    2. pi zero broad : 
       1. 

##### Purchased  
  - Raspberry Pi Zero W :  https://www.adafruit.com/opensafely
  - Aamzon: DORHEA Raspberry Pi Mini Camera Video Module 5 Megapixels  ($8.69)



### Solution Candidate  survey  
- - 1. Motion eye  OS : 
      - Pro 
      - Con 
    2. 

### General question 

#### Front door 
##### <Question: howto set up the battery >

<Answer: Use the kitchen power cable >

##### <Question: Where to mount the camera in kitchen >
<Answer: >

#### Front door 

##### <Question: howto set up the battery >

<Answer:  >

##### <Question: Where to mount the camera >
where does the camera point to ?
<Answer: >

#### <Question: How to set a web server in pi zero or PC? >
<Answer: >

## Pi Zero monitoring Content 

###  Smart Security Camera

STATUS :  Planed 
Planned : howto do is planned. to be implemented 

- [How to Make a Smart Security Camera with a Raspberry Pi Zero](https://www.youtube.com/watch?v=Y2QFu-tTvTI)
In this video, we use a Raspberry Pi Zero W and a Raspberry Pi camera to make a smart security camera! 

The camera uses object detection (with OpenCV) to send you an email whenever it sees an intruder.
It also runs a webcam so you can view live video from the camera when you are away. 


0:00 -0:30 topics : Important
https://www.hackster.io/hackershack/smart-security-camera-90d7bd


7:12 start the installation 

NOTE : It will really takes long time to install openCV : 8 hours to 12 hours . 

#### Steps 
  - [∞](#smart-security-camera)
First run on pi 4 and then work on pi zero w. 

##### Install 
1. Install standard alone raspian (NOOB) in pi 4 : 

  - [Pi zero w bootup  access over wifi ](https://www.youtube.com/watch?v=LlCr09B2HZI)

- - 1.  Install standard alone raspian (NOOB) in pi 4 :

      1. download : https://www.raspberrypi.org/downloads/noobs/
          https://www.raspberrypi.org/downloads/

      2. download imager 
        https://www.youtube.com/watch?v=y45hsd2AOpw
B8:27:EB.

##### remote control 

2. Enable remote control of pi zero w : 
   [∞](#raspberry-pi-remote-accessing)
  - [Pi zero w bootup  access over wifi ](https://www.youtube.com/watch?v=LlCr09B2HZI)

##### Camera configure  
3. Configure Camera : https://github.com/HackerShackOfficial/Smart-Security-Camera
   1. Setup : sudo raspi-config
   2. still image : raspistill -o image.jpg

##### Install OpenCV 

4. Install OpenCV according to : 
   1. Installing OpenCV in PiZero W
      1. https://towardsdatascience.com/installing-opencv-in-pizero-w-8e46bd42a3d3
   2. Smart-Security-Camera
      1. https://github.com/HackerShackOfficial/Smart-Security-Camera
      2. https://www.hackster.io/hackershack/smart-security-camera-90d7bd#code
   3. Install python 2.7 

https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/
   1. first thing you should do is expand your filesystem to include all available space on your micro-SD card:
      1. already NOOB, no need 

    2. update and upgrade any existing packages:
      $ sudo apt-get update
      $ sudo apt-get upgrade
      

    3. dependence install  
      $ sudo apt-get install build-essential cmake pkg-config
      $ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev 
      
      $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
      $ sudo apt-get install libxvidcore-dev libx264-dev
      
      $ sudo apt-get install libgtk2.0-dev

      $ sudo apt-get install libatlas-base-dev gfortran

    d $ sudo apt-get install python2.7-dev python3-dev

    4.   Download the OpenCV source code
      $ cd ~
      $ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
      $ unzip opencv.zip

       $ wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
       $ unzip opencv_contrib.zip 

##### using  https://medium.com/@aadeshshah/pre-installed-and-pre-configured-raspbian-with-opencv-4-1-0-for-raspberry-pi-3-model-b-b-9c307b9a993a
    
    
    5.   compiling OpenCV : 
        $ wget https://bootstrap.pypa.io/get-pip.py
        $ sudo python get-pip.py
        $ sudo pip install virtualenv virtualenvwrapper
        $ sudo rm -rf ~/.cache/pip

      # virtualenv and virtualenvwrapper
      export WORKON_HOME=$HOME/.virtualenvs
      source /usr/local/bin/virtualenvwrapper.sh

      $ echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.profile
      $ echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
      $ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile

      $ source ~/.profile

    6. Creating your Python virtual environment
        $ mkvirtualenv cv -p python2
        $ mkvirtualenv cv -p python3 ## python 3 



##### Send email 
5. Customization : Send email 


##### Running continuously 
6. Running : 
1. Local : 
  <raspberrypi_ip>:5000 

2. Remote : ngrok
expose 
https://ngrok.com/

Note: To view the live stream on a different network than your Raspberry Pi, you can use ngrok to expose a local tunnel. 

Once downloaded, run ngrok with ./ngrok http 5000 and visit one of the generated links in your browser.



#### Objective 
- - 1. Finish all the planning and read all the material : 
    2. Status : Planed 

    
### Reference 

- [Set Your Raspberry Pi as a Wireless PC Webcam ](https://www.youtube.com/watch?v=2yeso-ikMn0)
[V_1]

- [How to Make a Smart Security Camera with a Raspberry Pi Zero](https://www.youtube.com/watch?v=Y2QFu-tTvTI)

- [Build a Raspberry Pi Webcam Server in Minutes](https://www.youtube.com/watch?v=WNKbZsrsKVs)

- [How to Use Raspberry Pi as a PC Webcam](https://www.tomshardware.com/how-to/use-raspberry-pi-as-pc-webcam) 
[V_3]

  - [Raspberry Pi Zero W and Pi Camera Application](https://tutorial.cytron.io/2017/08/16/raspberry-pi-zero-w-pi-camera-application/)
 

### Host Your Website

ACCESSING

#### Search items :

- Raspberry Pi : web server

#### Reference

- [Host Your Website](https://www.instructables.com/id/Host-your-website-on-Raspberry-pi/)

* [Setting up a web server on a Raspberry Pi - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/remote-access/web-server/)

- [How to Set Up a Raspberry Pi Web Server - Tom's Hardware | Tom's Hardware](https://www.tomshardware.com/news/raspberry-pi-web-server,40174.html)

- [Make a VPN Server with a Raspberry Pi, OpenVPN and Stunnel](https://www.youtube.com/watch?v=nnQDiGBFIXk)

### Introduction

- [Setup a Raspberry Pi Web Server with Your Own .COM Using **Google Domains**](https://www.youtube.com/watch?v=vzojwG7OB7c&t=744s)

In this video I show how to setup a Raspberry Pi web server and how to connect it to your own domain name (.com, .org, etc.).

We
tart be installing **Raspbian**,
hen install software updates, and then install Apache, PHP and MySQL.

#### Step 1: Connect Via SSH

- - - [ ] lock the ip address for the device

##### wifi client remote access :

- - 1. raspberrypi: ip : 192.168.1.6
    2. ssh pi@192.168.1.6
    3. password for pi : tangwin/

- - Also :
  - TeraTerm
  - Swish SFTP
  - We also install TeraTerm and Swish SFTP on the Windows PC in order to interact with the Raspberry Pi over the network.

#### Step 2: Setting Up You Rasberry Pi

- - 1. already setup in Raspberry pi side
  - 2. installed **Raspbian**,

#### Step 3: Installing Your Server

##### install web Infrastructure.

- - 1.  apache : apache2
    2.  php :
    3.  MySQL.

##### Location of html fire.

- - 1.  cd /var/
    1.  sudo chmod 777 /www

##### Launch a apache server.

- - sudo service apache2 restart

#### Step 4: Setup Up PORT Triggers

- - 1.  After verifying that the web server is functioning properly.

#### Step 5: domain name and website

- - 1. how to sign up for a domain name with **Google Domains**,

    - domains.google.com

  - 2.  how to use their **Dynamic** DNS service so your domain will work with typical residential internet service providers.

#### Q n A

<Question: what is google domain >
<Answer: >

<Question: Can I install flask and other web framework >
<Answer: >

<Question: Can I install streamlit in Raspberry pi>
<Answer: >

#### Web logging :

- Log the incoming

## Object Detection

- [How To Run TensorFlow Lite on Raspberry Pi for Object Detection](https://www.youtube.com/watch?v=aimSGOAUI8Y&t=206s)

- scikit-learn will run on a Raspberry Pi just as well as any other Linux machine.

## Raspberry Pi video resource

### Get start

- [Raspberry Pi 4 Getting Started](https://www.youtube.com/watch?v=BpJCAafw2qE&t=939s)

- [Canakit Raspberry Pi 4 Unboxing and Initial Setup](https://www.youtube.com/watch?v=A40GvpEGqpg&t=111s)

- [CanaKit Raspberry Pi 4 (4GB) Starter Kit Unboxing and Initial](https://www.youtube.com/watch?v=Wb1YForDARU)

- [Amazon](https://www.amazon.com/CanaKit-Raspberry-Starter-Clear-Case/dp/B07YLY143F/ref=asc_df_B07YLY143F/?tag=hyprod-20&linkCode=df0&hvadid=385197824350&hvpos=&hvnetw=g&hvrand=13142538446544069510&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9033288&hvtargid=pla-830000654545&psc=1&tag=&ref=&adgrpid=76690811457&hvpone=&hvptwo=&hvadid=385197824350&hvpos=&hvnetw=g&hvrand=13142538446544069510&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9033288&hvtargid=pla-830000654545)

### Surveillance

- [Raspberry Pi Zero W Surveillance Camera](https://www.youtube.com/watch?v=rhIzfRmKHnQ&list=WL&index=2&t=881s)

- [Raspberry Pi Surveillance Monitor v2](https://www.youtube.com/watch?v=0tvX_gsv2ZU&list=WL&index=3&t=90s)

* [How to Make a Smart Security Camera with a Raspberry Pi Zero](https://www.youtube.com/watch?v=Y2QFu-tTvTI&list=WL&index=59&t=440s)

### Pi projects

- [TOP 10 Raspberry Pi projects for 2020](https://www.youtube.com/watch?v=HE6rIU8i8ho)
- [Top 5 Raspberry Pi DIY Projects of All Time](https://www.youtube.com/watch?v=ZXpGNBzHKRY)s

### NAS : ne

- [RASPBERRY Pi 4 - How To Build POWERFUL NAS | ULTIMATE Raspberry Pi 4 NAS Server Setup 2020 Ksk Royal](https://www.youtube.com/watch?v=s0Sc2n3gUqA&list=WL&index=53&t=304s)

### VPN

- [PiVPN : How to Run a VPN Server on a \$35 Raspberry Pi!](https://www.youtube.com/watch?v=15VjDVCISj0&list=WL&index=4&t=109s)

### TensorFlow: Object detection

- [Detect ANY Object with Raspberry Pi and TensorFlow](https://www.youtube.com/watch?v=O-FfOWdZAQ4&list=WL&index=45&t=0s)

* [How to Set Up TensorFlow Object Detection on the Raspberry Pi](https://www.youtube.com/watch?v=npZ-8Nj1YwY&list=WL&index=26&t=1s)

- [#312 Boot a Raspberry Pi4 with an SSD to make it reliable and fast](https://www.youtube.com/watch?v=gp6XW-fGVjo&list=WL&index=34&t=0s)

### Gaming

- [The Raspberry Pi 4 Is A Gaming Beast](https://www.youtube.com/watch?v=DvdiVwx996s&list=WL&index=50&t=769s)

### Android

- [How To Install Android On the Raspberry Pi 4 & Google Play Store](https://www.youtube.com/watch?v=QSgf_-EwfrQ&list=WL&index=60&t=15s)

### DIY

- [Top 5 Raspberry Pi DIY Projects of All Time](https://www.youtube.com/watch?v=ZXpGNBzHKRY&list=WL&index=62&t=47s)

### Amazon Purchase

// STUB
Purchasing list : Compare different seller.

### Basic

- [Build Physical Projects With Python on the Raspberry Pi – Real Python](https://realpython.com/python-raspberry-pi/)
- ###### tensor flow

### Web server

- [Setting up a web server on a Raspberry Pi - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/remote-access/web-server/)
-
- [Setup a Raspberry Pi Web Server with Your Own .COM Using Google Domains - YouTube](https://www.youtube.com/watch?v=vzojwG7OB7c) [Good]

- ###### website

- [How to Set Up a Raspberry Pi Web Server - Tom's Hardware | Tom's Hardware](https://www.tomshardware.com/news/raspberry-pi-web-server,40174.html)

- [Make a VPN Server with a Raspberry Pi, OpenVPN and Stunnel](https://www.youtube.com/watch?v=nnQDiGBFIXk)

#### Object Detection Video.

- [How To Run TensorFlow Lite on Raspberry Pi for Object Detection](https://www.youtube.com/watch?v=aimSGOAUI8Y&t=206s)

### Wiki

- [Raspberry Pi - Wikipedia](https://en.wikipedia.org/wiki/Raspberry_Pi)

