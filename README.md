# RPI4-Media-Player

1. Install *unclutter*:

```shell
sudo apt install unclutter
```

2. Install *omxplayer*:

```shell
sudo apt install omxplayer
```

3. Create an folder for *Apps*:

```shell
cd ~/
mkdir Apps
```
4. Put *media-player.py* file inside the created folder.
5. Inside *.config* folder, you'll need to create an *autostart* folder:

```shell
cd ~/.config
mkdir autostart
```

6. Create a shortcut file and script the content:

```shell
nano ~/.config/autostart/rpi4-media-player.desktop
```

Script the file with this code bellow:

````shell
[Desktop Entry]
Name=RPI4 Media Player
Exec=python3 ~/Apps/media-player.py
Type=application
```

7. Put your default mp4 file in Videos folder and rename it to match with *default.mp4*.
8. Reboot RPI4.

### Some tips
After reboot, using RPI4 as a normal computer again, it's kind of hard. Because of that I have added an option to get control of RPI4 again.
Using one usb storage drive, put a dev.txt empty file on root, plug in into RPI4 and turn on the power. The script will verify the usb storage and will find the file and stop the script for you.

For better interface, I recommend:

- Use the background wallpaper as flat black.
- Turn on the auto-hide for top-bar.
- Hide basket icon from desktop.
- Disable mounted drives from desktop.
