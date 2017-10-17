import colorsys
import math


class ColorBase:
    pass


class Color8Bit(ColorBase):
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7

    def __init__(self, color, bright):
        self.color = color
        self.bright = bright

    def to_irc(self):
        d = {
            (self.BLACK, True): 14,
            (self.BLACK, False): 1,
            (self.RED, True): 4,
            (self.RED, False): 5,
            (self.GREEN, True): 9,
            (self.GREEN, False): 3,
            (self.YELLOW, True): 8,
            (self.YELLOW, False): 7,
            (self.BLUE, True): 12,
            (self.BLUE, False): 2,
            (self.MAGENTA, True): 13,
            (self.MAGENTA, False): 6,
            (self.CYAN, True): 11,
            (self.CYAN, False): 10,
            (self.WHITE, True): 0,
            (self.WHITE, False): 15
        }
        return d[(self.color, self.bright)]


class ColorRGB(ColorBase):
    def __init__(self, r, g, b, max_value=1):
        self.r = r
        self.g = g
        self.b = b
        self.max = max_value

    def __iter__(self):
        yield self.r
        yield self.g
        yield self.b

    def scale(self, new_max_value=1):
        f = new_max_value / self.max
        return ColorRGB(self.r * f,
                        self.g * f,
                        self.b * f,
                        max_value=new_max_value)

    def to_dp(self):
        return '^x{}{}{}'.format(*self.scale(15))

    def to_8bit(self):
        h, s, v = colorsys.rgb_to_hsv(*self.scale(1))
        # Check if the color is a shade of grey
        if s * v < 0.3:
            if v < 0.3:
                return Color8Bit(Color8Bit.BLACK, False)
            elif v < 0.66:
                return Color8Bit(Color8Bit.BLACK, True)
            elif v < 0.91:
                return Color8Bit(Color8Bit.WHITE, False)
            else:
                return Color8Bit(Color8Bit.WHITE, True)
        # not grey? What color is it then?
        if h < 0.041 or h > 0.92:
            res = Color8Bit.RED
        elif h < 0.11:
            # orange = dark yellow
            return Color8Bit(Color8Bit.YELLOW, False)
        elif h < 0.2:
            res = Color8Bit.YELLOW
        elif h < 0.45:
            res = Color8Bit.GREEN
        elif h < 0.6:
            res = Color8Bit.CYAN
        elif h < 0.74:
            res = Color8Bit.BLUE
        else:
            res = Color8Bit.MAGENTA
        return Color8Bit(res, v > 0.6)

    def __repr__(self):
        return 'Color(%s, %s, %s)' % (self.r / self.max,
                                      self.g / self.max,
                                      self.b / self.max)


class NoColor(ColorBase):
    def __bool__(self):
        return False

    def __repr__(self):
        return 'NoColor()'

    def to_irc(self):
        return '\3'

    def to_dp(self):
        return '^7'


class ColorPart:
    def __init__(self, text, fg_color=None, bg_color=None):
        if fg_color:
            self.color = fg_color
        else:
            self.color = NoColor()
        if bg_color:
            self.bg_color = bg_color
        else:
            self.bg_color = NoColor()
        self.text = text

    def __repr__(self):
        if self.bg_color:
            return 'ColorPart(%r, %r, %r)' % (self.text, self.color, self.bg_color)
        elif self.color:
            return 'ColorPart(%r, %r)' % (self.text, self.color)
        else:
            return 'ColorPart(%r)' % self.text

    def __str__(self):
        return self.text


class ColorString:
    def __init__(self, parts):
        self.parts = parts
        self.original_type = None
        self.original_bytes = None

    @classmethod
    def from_dp(cls, text, use_unicode_for_glyphs=True, debug=False):
        from .grammars.dp import parse as parse_dp
        if isinstance(text, bytes):
            original_bytes = text
            text = text.decode('utf8')
        else:
            original_bytes = text.encode('utf8')
        instance = parse_dp(text, use_unicode_for_glyphs=use_unicode_for_glyphs)
        instance.original_type = 'dp'
        instance.original_bytes = original_bytes
        return instance

    def to_dp(self, preserve_original=True):
        if preserve_original:
            return self.original_bytes
        res = []
        for i in self.parts:
            res.append('^x%s%s' % (i.color.to_dp(), i.text.replace('^', '^^')))
        s = ''.join(res) + '^7'
        return s.encode('utf8')

    @classmethod
    def from_irc(cls, text):
        from .grammars.irc import parse as parse_irc
        if isinstance(text, bytes):
            original_bytes = text
            text = text.decode('utf8')
        else:
            original_bytes = text.encode('utf8')
        instance = parse_irc(text)
        instance.original_type = 'irc'
        instance.original_bytes = original_bytes
        return instance

    def to_irc(self, preserve_original=True, for_light_background=True):
        if preserve_original:
            return self.original_bytes

    def __str__(self):
        return ''.join([str(i) for i in self.parts])

    def __repr__(self):
        parts = [repr(i) for i in self.parts]
        return 'ColorString([%s])' % ', '.join(parts)
