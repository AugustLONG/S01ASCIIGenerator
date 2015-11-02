from PIL import Image
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-0', '--output')
parser.add_argument('--width', type = int, default = 80)
parser.add_argument('--height', type = int, default = 80)

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("@#$%^**HGFDRE$##%%%%%%%%%%%%%************&&&&&&&&&&&&&&&&&&&%%%%%%%$#****************%%%%%%@@@@@@@@")
def get_char(r,b,g,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r+0.7152*g+0.0722*b)
    
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""
    
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print txt
    f = open("output.txt", 'wb')
    f.write(txt)
    f.close()
