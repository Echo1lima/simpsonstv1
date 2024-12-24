nano ~/play_simpsons.sh
#!/bin/bash
while true; do
    for file in ~/simpsonstv/videos/*; do
        mpv --no-window --vo=drm --hwdec=auto "$file"
    done
done
chmod +x ~/play_simpsons.sh
nano ~/.bashrc
if [ $(tty) == /dev/tty1 ]; then
    ~/play_simpsons.sh
fi
