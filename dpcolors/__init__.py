class ColorBase:
    pass


class ColorRGB(ColorBase):
    def __init__(self, r, g, b, max_value=1):
        self.r = r
        self.g = g
        self.b = b
        self.max = max_value

    def scale(self, new_max_value=1):
        f = new_max_value / self.max
        return ColorRGB(self.r * f,
                        self.g * f,
                        self.b * f,
                        max_value=new_max_value)

    def __repr__(self):
        return 'Color(%s, %s, %s)' % (self.r / self.max,
                                      self.g / self.max,
                                      self.b / self.max)


class NoColor(ColorBase):
    def __bool__(self):
        return False

    def __repr__(self):
        return 'NoColor()'


class ColorPart:
    def __init__(self, text, fg_color, bg_color=None):
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
            return 'ColorPart(%s, %r, %r)' % (self.text, self.color, self.bg_color)
        elif self.color:
            return 'ColorPart(%s, %r)' % (self.text, self.color)
        else:
            return 'ColorPart(%s)' % self.text

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
            text = text.decode('utf8')
        instance = parse_dp(text, use_unicode_for_glyphs=use_unicode_for_glyphs, debug=debug)
        instance.original_type = 'dp'
        instance.original_bytes = text.encode('utf8')
        return instance

    def to_dp(self, preserve_original=True):
        if preserve_original:
            return self.original_bytes
        res = []
        for i in self.parts:
            c = i.color.scale(15)
            res.append('^x%X%X%X%s' % (int(c.r), int(c.g), int(c.b), i.text))
        s = ''.join(res) + '^7'
        return s.encode('utf8')

    def __str__(self):
        return ''.join([str(i) for i in self.parts])

    def __repr__(self):
        parts = [repr(i) for i in self.parts]
        return 'ColorString([%s])' % ', '.join(parts)
