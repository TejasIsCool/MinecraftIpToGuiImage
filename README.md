# MinecraftIpToGuiImage
Give it a valid, online, Minecraft server ip, and the program shall return an image of the server as if its a screenshot taken in Minecraft

# How does it work?
Basically, using the [Minecraft Server Status API](https://api.mcsrvstat.us), and its icon endpoint, the program gets the required information it needs to create an image, which looks as if it was a screenshot of the server menu taken inside Minecraft.

# How to run it?
Prerequisites:
- Python 3+
- Two python libraries, `Pillow` and `BeautifulSoup`

To install the libraries, go to the command line and type

```shell
python3 -m pip install --upgrade Pillow
```

and

```shell
python3 -m pip install --upgrade BeautifulSoup
```

If an error occurs, use google


To run it:
- Go inside the main.py file
- Change the content inside the `serverip` and `servername` to your choice. Then save the file.
- Go to the command line and navigate it to the folder in which main.py is in
- Do 
```shell
python3 main.py
```
- Wait a few seconds. An image should pop up, showing the rendered image. It is also saved to a file called `output.png`.
