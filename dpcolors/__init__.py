class Color:
    def __init__(self, r, g, b, max_value=1):
        self.r = r
        self.g = g
        self.b = b
        self.max = max_value


class ColoredPart:
    def __init__(self, fg_color, bg_color, text):
        self.color = fg_color
        self.bg_color = bg_color
        self.text = text

    def __str__(self):
        return self.text


class ColoredString:
    def __init__(self, parts):
        self.parts = parts
        self.original_adapter = None
        self.original_string = None

    @classmethod
    def from_bytes(cls, adapter, text: bytes):
        res = adapter.from_bytes(text)
        res.original_adapter = adapter
        res.original_string = text
        return res

    @classmethod
    def from_string(cls, adapter, text: str):
        return cls.from_bytes(adapter, text.encode('utf8'))

    def to_string(self, adapter, preserve_original=True):
        if preserve_original and self.original_adapter \
                and isinstance(self.original_adapter, type(adapter)) and self.original_string:
            return self.original_string
        return adapter.to_string(self)

    def __str__(self):
        return ''.join([str(i) for i in self.parts])
