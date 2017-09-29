from . import ColoredString
from .grammars.dp import parse as parse_dp


class BaseAdapter:
    def part_to_string(self, part):
        raise NotImplementedError

    def to_string(self, colored_string):
        return ''.join([self.part_to_string(i) for i in colored_string.parts])

    def from_bytes(self, text):
        raise NotImplementedError


class DPColors(BaseAdapter):
    dec_to_rgb = [
        (128, 128, 128),
        (255, 0, 0),
        (51, 255, 0),
        (255, 255, 0),
        (51, 102, 255),
        (51, 255, 255),
        (255, 51, 102),
        None,
        (153, 153, 153),
        (128, 128, 128)
    ]

    def part_to_string(self, part):
        return '^x%x%x%x%s' % (part.fg_color.r,
                               part.fg_color.g,
                               part.fg_color.b,
                               part.text.replace('^', '^^'))

    def from_bytes(self, text):
        s = text.decode('utf8')
        parse_result = parse_dp(s)
        result = ColoredString([])




class IRCColors(BaseAdapter):
    pass


class HTMLColors(BaseAdapter):
    pass


class TerminalColors(BaseAdapter):
    pass
