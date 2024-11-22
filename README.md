# Simpons Mini TV
**These python scripts are updated to work with Raspios (Bullseye) on Pi Zero 2 W**

On the original instructions where it says "sudo apt-get install omxplayer"

replace with this:

`sudo apt-get update` Update the apt first.

`sudo apt-get install vlc` Install the vlc player as omxplayer is deprecated.

`sudo apt-get install python3-rpi.gpio` Install gpio dependency for python as well (just to be safe), even tho previously Withrow had us install "sudo apt-get install raspi-gpio" already.

`sudo apt-get install git` Install git for downloading the repo

Then where it says "cd ~/ git clone ~~https://github.com/buba447/simpsonstv~~" replace the url with the repo I updated for you here: **https://github.com/corguo/simpsonstv**

Like this:
```python
cd ~/
git clone https://github.com/corguo/simpsonstv
```

Proceed following rest of his guide on Moving the videos...
