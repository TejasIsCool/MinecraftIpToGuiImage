from PIL import Image
from src import motdtoimage
import requests
def loadandrun(servername,serverip):
    if servername == "":
        servername = None
    if serverip == "":
        raise Exception("No Ip address detected")
    logo = Image.open(requests.get(f"https://api.mcsrvstat.us/icon/{serverip}", stream=True).raw)
    r = requests.get(url=f"https://api.mcsrvstat.us/2/{serverip}")
    r=r.json()
    html = r['motd']['html']
    onlineplayers = str(r['players']['online'])
    playerstotal = str(r['players']['max'])
    motdtoimage.getmotdtoimg(html,logo,(onlineplayers,playerstotal),servername)