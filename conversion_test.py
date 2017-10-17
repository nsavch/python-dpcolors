import colorsys

from dpcolors import ColorRGB
from dpcolors.grammars.irc import COLORS

html_header = '<!DOCTYPE html><html><head></head><body>'


out = open('test.html', 'w')
out.write(html_header)
out.write('<table style="margin-left: auto; margin-right: auto" cellspacing=0>')
h = 0
for s in range(100, -1, -1):
    out.write('<tr>')
    for v in range(101):
        r, g, b = [int(i * 255) for i in colorsys.hsv_to_rgb(h, s / 100, v / 100)]
        out.write('<td style="width: 5px; height: 5px; background: #%02X%02X%02X"></td>' % (r, g, b))
    out.write('</tr>')
out.write('</table>')

out.close()


out = open('test_hue.html', 'w')
out.write(html_header)
out.write('<div id="color" style="height: 20px; width: 20px">0/0</div>')
out.write('<table style="margin-left: auto; margin-right: auto" cellspacing=0>')
v = 1

for s in range(100, -1, -1):
    out.write('<tr>')
    for h in range(101):
        r, g, b = [int(i * 255) for i in colorsys.hsv_to_rgb(h / 100, s / 100, v)]
        out.write(f'<td onmouseover="document.getElementById(\'color\').innerHTML=\'{h}/{s}\';" style="width: 5px; height: 5px; background: #{r:0=2x}{g:0=2x}{b:0=2x}"></td>')
    out.write('</tr>')
out.write('</table>')

out.close()


out = open('rgb_to_irc.html', 'w')
out.write(html_header)
header = '<table style="float: left"><tr><th>&nbsp;</th><th>RGB</th><th>IRC</th><th>&nbsp;</th></tr>'
footer = '</table>'
row_template = '<tr style="height: 10px"><td>#%X%X%X</td><td style="background: #%X%X%X"></td><td style="background: #%02X%02X%02X"></td><td>%s</td></tr>'
for r in range(16):
    out.write(header)
    for g in range(16):
        for b in range(16):
            c = ColorRGB(r, g, b, 15)
            irc_color = c.to_8bit().to_irc()

            out.write(row_template % (r, g, b, r, g, b, *COLORS[irc_color], irc_color))
    out.write(footer)
out.write('</body></html>')

out.close()
