# grabbit.py
Grabbit Like A Rabbit! Provide a 'targets.txt' file with host:port (1 per line) and grabbit will provide service info and screenshots for all discovered hosts/ports.

     Language: Python 2
     Libraries: requests, socket, sys, pyvirtualdisplay, selemium, os
     Purpose: Penetration Testing / Fuzzy Screenshotter


# Install
Follow the steps below to install 'grabbit'.

     git clone https://github.com/lostrabbitlabs/grabbit
     cd grabbit
     chmod 655 grabbit.py
     pip install pyvirtualdisplay
     apt-get install xvfb
     wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
     tar zxvf geckodriver-v0.18.0-linux64.tar.gz
     chmod 655 geckodriver
     cp geckodriver /usr/bin/geckodriver


# Usage
Simply provide a 'targets.txt' file and run the script.

     ./grabbit.py targets.txt


Sample 'targets.txt' file:

     192.168.0.100:80
     192.168.0.100:443
     192.168.0.1:10000
     lost-rabbit.com:80
     www.lost-rabbit.com:443

# Output
When completed will create two (2) output directories with the goods:

     /services
     /screenshots
