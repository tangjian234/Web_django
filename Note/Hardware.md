# Hardware.md

- [Hardware.md](file:///C:/Local/Work/ML_Name/Note/Hardware.md)

## DONE

- [x] Study Raspberry Pi [P_4][v_3] [07-07]
- [x] Read web server setup [](#my-web-server) [07-07]
  - [x] two documents.

## Todo

- [ ] set up actual webpage in Raspberry pi
  - [ ] run simple streamlit work in Raspberry pi :
    - [ ] show publishable web-essential extractor.

## Objective

- Use of Raspberry_Pi to develop
  - web_server to as free NLP service.
  - object detection for NN study.

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
    - Linux computer
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

- [raspberrypi home site](https://www.raspberrypi.org/products/)

# Projects

## One liner

    1. My Web server for ML projects.
    2. Tensorflow object detection

## My Web server

### Raspberry pi remote accessing

##### wifi client IPS : SSH access

- - 1. raspberrypi: ip : 192.168.1.6
    2. ssh pi@192.168.1.6
    3. password for pi : tangwin/

##### VNC access :

- - 1. Install VNC in windows.
    2. run VNC connection 192.168.1.6

#### shutdown

- - - sudo shutdown -h now

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

## Reference

- [What is a Raspberry Pi?](https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/)

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
