from PIL import Image, ImageDraw, ImageFont
import random


def draw_underlined_text(draw, pos, text, font, **options):    
    twidth, theight = draw.textsize(text, font=font)
    lx, ly = pos[0], pos[1] + theight
    draw.text(pos, text, font=font, **options)
    draw.line((lx, ly, lx + twidth, ly), **options)


def toImage(info,icon,players,servername=None):
    img = Image.open("resources/images/mcserverbackground.png")
    draw = ImageDraw.Draw(img)
    fontreg = ImageFont.truetype("resources/fonts/McFontRegular.otf",20)
    fontbold = ImageFont.truetype("resources/fonts/McFontBold.otf",20)
    fontitalic = ImageFont.truetype("resources/fonts/McFontItalic.otf",20)
    fontboldanditalic = ImageFont.truetype("resources/fonts/McFontBoldItalic.otf",20)
    draw.fontmode="1"

    line1 = info[0]
    line2 = info[1]
    font= fontreg
    xalt = 76
    for i,part in enumerate(line1):
        style = part['styles']
        font = fontreg
        if style['font-weight'] == "bold":
            font=fontbold
        if style['font-style'] == "italic":
            font=fontitalic
        if style['font-weight'] == "bold" and style['font-style'] == "italic":
            font = fontboldanditalic
        
        if style['text-decoration'] == "underline":
            draw_underlined_text(draw,(xalt,28),part['text'],fill=info[0][i]['styles']['color'],font=font)
        else:
            draw.text((xalt,34),part['text'],fill=info[0][i]['styles']['color'],font=font,anchor="lm")
        xalt+=font.getbbox(part['text'])[2]
    xalt = 76
    for i,part in enumerate(line2):
        style = part['styles']
        font = fontreg
        if style['font-weight'] == "bold":
            font=fontbold
        if style['font-style'] == "italic":
            font=fontitalic
        if style['font-weight'] == "bold" and style['font-style'] == "italic":
            font = fontboldanditalic
        if style['text-decoration'] == "underline":
            draw_underlined_text(draw,(xalt,46),part['text'],fill=info[1][i]['styles']['color'],font=font)
        else:
            draw.text((xalt,52),part['text'],fill=info[1][i]['styles']['color'],font=font,anchor="lm")
        xalt+=font.getbbox(part['text'])[2]
    #Server name
    if servername != None:
        servname = servername
    else:
        servname = random.choice(['Server','server','something','potato','info'])
    draw.text((76,6),servname,fill='#FFFFFF',font=fontreg,anchor='lt')
    #server logo
    img.paste(icon,(6,4),mask=icon)
    #server players
    xoff = 582
    xoff -= fontreg.getbbox(players[1],anchor='lt')[2]
    draw.text((xoff,6),str(players[1]),fill='#AAAAAA',font=fontreg,anchor='lt')

    xoff -= fontreg.getbbox("/",anchor='lt')[2]
    draw.text((xoff,6),"/",fill='#555555',font=fontreg,anchor='lt')

    xoff -= fontreg.getbbox(players[0],anchor='lt')[2]
    draw.text((xoff,6),str(players[0]),fill='#AAAAAA',font=fontreg,anchor='lt')
    #Logo top left = 6,4
    #Playercount: 438,6 (579,19)rd
    #Text1 : 76,28
    #Text2: 76,46
    #Name: 76,6
    #draw.text((76,28),info[0][0]['text']+info[0][1]['text'],fill=info[0][1]['styles']['color'],font=font,anchor="lt")

    #connection
    randsignal = random.choice(range(1,5))
    for i in range(0,5):
      #586,14  #590,12  +4 -2
      fillbri = "#00FF21"
      filldark = "#00870F"
      if i>=randsignal:
        fillbri = "#5B5B5B"
        filldark = "#383838"
      draw.rectangle([(586+i*4,14-2*i),(587+i*4,17)],fill=fillbri)
      draw.rectangle([(588+i*4,16-2*i),(589+i*4,19)],fill=filldark)

    img.save("output.png")
    img.show()
