import sys
from PIL import Image, ImageDraw, ImageFont
# usage: pick.py out.jpg label=path ...
out=sys.argv[1]; items=[a.split('=',1) for a in sys.argv[2:]]
tw=520; th=380; cols=3; rows=(len(items)+cols-1)//cols
S=Image.new('RGB',(cols*tw,rows*th),'white'); d=ImageDraw.Draw(S); f=ImageFont.load_default(size=22)
for i,(lab,p) in enumerate(items):
    im=Image.open(p); im.thumbnail((tw-8,th-8)); x=(i%cols)*tw; y=(i//cols)*th; S.paste(im,(x+4,y+4))
    d.rectangle([x+4,y+4,x+120,y+32],fill='black'); d.text((x+8,y+6),lab,fill='yellow',font=f)
S.save(out,quality=82)
