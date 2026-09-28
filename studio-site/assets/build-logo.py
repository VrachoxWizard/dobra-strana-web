# Gradi logotip i znak Dobra Strana. Pokretanje: py assets/build-logo.py <mapa-fontova> assets
import sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen

F = sys.argv[1].rstrip('/') + '/'  # mapa s Fraunces TTF datotekama iz google/fonts
AX = dict(opsz=72, wght=560, SOFT=50, WONK=0)
roman = instantiateVariableFont(TTFont(F+'Fraunces[SOFT,WONK,opsz,wght].ttf'), AX)
ital = instantiateVariableFont(TTFont(F+'Fraunces-Italic[SOFT,WONK,opsz,wght].ttf'), dict(AX, wght=500))

def run(font, text, x0, size, track=0):
    upm = font['head'].unitsPerEm; s = size/upm
    gs = font.getGlyphSet(); cmap = font.getBestCmap(); hmtx = font['hmtx']
    paths = []; x = x0
    for ch in text:
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs); gs[g].draw(pen)
        d = pen.getCommands()
        if d: paths.append((d, x, s))
        x += hmtx[g][0]*s + track
    return paths, x

SIZE = 46; BASE = 52
p1, x = run(roman, 'Dobra', 88, SIZE, -0.6)
x += 10
p2, x2 = run(ital, 'Strana', x, SIZE, -0.4)
W = int(x2 + 6)

def mark(ink, brick):
    return (f'<path d="M8 8H46V19H19V46H8Z" fill="{ink}"/>'
            f'<path d="M64 64H26V53H53V26H64Z" fill="{brick}"/>')

def svg(ink, brick, text, label='Dobra Strana'):
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 72" role="img" aria-label="{label}">', mark(ink, brick)]
    for d, xx, s in p1: out.append(f'<path d="{d}" transform="translate({xx:.2f} {BASE}) scale({s:.5f} -{s:.5f})" fill="{text}"/>')
    for d, xx, s in p2: out.append(f'<path d="{d}" transform="translate({xx:.2f} {BASE}) scale({s:.5f} -{s:.5f})" fill="{brick}"/>')
    out.append('</svg>'); return ''.join(out)

def msvg(ink, brick):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 72 72" role="img" aria-label="Znak Dobra Strana">{mark(ink,brick)}</svg>'

INK, BRICK, PAPER, ORANGE = '#1F2421', '#B8432A', '#F4F0E8', '#EE7A52'
out = sys.argv[2]
files = {
 'logo.svg': svg(INK, BRICK, INK),
 'logo-dark.svg': svg(PAPER, ORANGE, PAPER),
 'logo-mono.svg': svg(INK, INK, INK),
 'mark.svg': msvg(INK, BRICK),
 'mark-dark.svg': msvg(PAPER, ORANGE),
 'mark-mono.svg': msvg(INK, INK),
}
for n, c in files.items():
    open(out+'/'+n, 'w', encoding='utf-8').write(c)
print('W', W)
