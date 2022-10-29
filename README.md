##  prepare

```bash
sudo apt install python3-pip
python3 -m pip install --user --upgrade pip

sudo apt-get install python-pip libsdl-mixer1.2 libusb-1.0 \
    python-pyaudio libsdl1.2-dev cython cython3 libudev-dev \
    python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev libsmpeg-dev python-numpy libportmidi-dev \
    libswscale-dev libavformat-dev libavcodec-dev \
    portaudio19-dev nodejs build-essential -y
    
pip3 install -r requirements.txt

```

## test sound

### Record Sound

```bash
pi@raspberrypi:~ $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 2: Camera [USB2.0 Camera], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

```bash
arecord -D hw:2,0 -d 5 -r 48000 -f S16_LE  test.wav
```

### Play Sound

```bash
aplay test.wav
```
