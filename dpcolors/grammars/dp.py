from arpeggio import RegExMatch as _, OrderedChoice, ZeroOrMore, ParserPython

qfont_ascii_table = [
 '\0', '#',  '#',  '#',  '#',  '.',  '#',  '#',
 '#',  '\t', '\n', '#',  ' ',  '\r', '.',  '.',
 '[',  ']',  '0',  '1',  '2',  '3',  '4',  '5',
 '6',  '7',  '8',  '9',  '.',  '<',  '=',  '>',
 ' ',  '!',  '"',  '#',  '$',  '%',  '&',  '\'',
 '(',  ')',  '*',  '+',  ',',  '-',  '.',  '/',
 '0',  '1',  '2',  '3',  '4',  '5',  '6',  '7',
 '8',  '9',  ':',  ';',  '<',  '=',  '>',  '?',
 '@',  'A',  'B',  'C',  'D',  'E',  'F',  'G',
 'H',  'I',  'J',  'K',  'L',  'M',  'N',  'O',
 'P',  'Q',  'R',  'S',  'T',  'U',  'V',  'W',
 'X',  'Y',  'Z',  '[',  '\\', ']',  '^',  '_',
 '`',  'a',  'b',  'c',  'd',  'e',  'f',  'g',
 'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',
 'p',  'q',  'r',  's',  't',  'u',  'v',  'w',
 'x',  'y',  'z',  '{',  '|',  '}',  '~',  '<',

 '<',  '=',  '>',  '#',  '#',  '.',  '#',  '#',
 '#',  '#',  ' ',  '#',  ' ',  '>',  '.',  '.',
 '[',  ']',  '0',  '1',  '2',  '3',  '4',  '5',
 '6',  '7',  '8',  '9',  '.',  '<',  '=',  '>',
 ' ',  '!',  '"',  '#',  '$',  '%',  '&',  '\'',
 '(',  ')',  '*',  '+',  ',',  '-',  '.',  '/',
 '0',  '1',  '2',  '3',  '4',  '5',  '6',  '7',
 '8',  '9',  ':',  ';',  '<',  '=',  '>',  '?',
 '@',  'A',  'B',  'C',  'D',  'E',  'F',  'G',
 'H',  'I',  'J',  'K',  'L',  'M',  'N',  'O',
 'P',  'Q',  'R',  'S',  'T',  'U',  'V',  'W',
 'X',  'Y',  'Z',  '[',  '\\', ']',  '^',  '_',
 '`',  'a',  'b',  'c',  'd',  'e',  'f',  'g',
 'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',
 'p',  'q',  'r',  's',  't',  'u',  'v',  'w',
 'x',  'y',  'z',  '{',  '|',  '}',  '~',  '<'
]


qfont_unicode_glyphs = [
   '\u0020',       '\u0020',       '\u2014',       '\u0020',
   '\u005F',       '\u2747',       '\u2020',       '\u00B7',
   '\U0001F52B',   '\u0020',       '\u0020',       '\u25A0',
   '\u2022',       '\u2192',       '\u2748',       '\u2748',
   '\u005B',       '\u005D',       '\U0001F47D',   '\U0001F603',
   '\U0001F61E',   '\U0001F635',   '\U0001F615',   '\U0001F60A',
   '\u00AB',       '\u00BB',       '\u2022',       '\u203E',
   '\u2748',       '\u25AC',       '\u25AC',       '\u25AC',
   '\u0020',       '\u0021',       '\u0022',       '\u0023',
   '\u0024',       '\u0025',       '\u0026',       '\u0027',
   '\u0028',       '\u0029',       '\u00D7',       '\u002B',
   '\u002C',       '\u002D',       '\u002E',       '\u002F',
   '\u0030',       '\u0031',       '\u0032',       '\u0033',
   '\u0034',       '\u0035',       '\u0036',       '\u0037',
   '\u0038',       '\u0039',       '\u003A',       '\u003B',
   '\u003C',       '\u003D',       '\u003E',       '\u003F',
   '\u0040',       '\u0041',       '\u0042',       '\u0043',
   '\u0044',       '\u0045',       '\u0046',       '\u0047',
   '\u0048',       '\u0049',       '\u004A',       '\u004B',
   '\u004C',       '\u004D',       '\u004E',       '\u004F',
   '\u0050',       '\u0051',       '\u0052',       '\u0053',
   '\u0054',       '\u0055',       '\u0056',       '\u0057',
   '\u0058',       '\u0059',       '\u005A',       '\u005B',
   '\u005C',       '\u005D',       '\u005E',       '\u005F',
   '\u0027',       '\u0061',       '\u0062',       '\u0063',
   '\u0064',       '\u0065',       '\u0066',       '\u0067',
   '\u0068',       '\u0069',       '\u006A',       '\u006B',
   '\u006C',       '\u006D',       '\u006E',       '\u006F',
   '\u0070',       '\u0071',       '\u0072',       '\u0073',
   '\u0074',       '\u0075',       '\u0076',       '\u0077',
   '\u0078',       '\u0079',       '\u007A',       '\u007B',
   '\u007C',       '\u007D',       '\u007E',       '\u2190',
   '\u003C',       '\u003D',       '\u003E',       '\U0001F680',
   '\u00A1',       '\u004F',       '\u0055',       '\u0049',
   '\u0043',       '\u00A9',       '\u00AE',       '\u25A0',
   '\u00BF',       '\u25B6',       '\u2748',       '\u2748',
   '\u2772',       '\u2773',       '\U0001F47D',   '\U0001F603',
   '\U0001F61E',   '\U0001F635',   '\U0001F615',   '\U0001F60A',
   '\u00AB',       '\u00BB',       '\u2747',       '\u0078',
   '\u2748',       '\u2014',       '\u2014',       '\u2014',
   '\u0020',       '\u0021',       '\u0022',       '\u0023',
   '\u0024',       '\u0025',       '\u0026',       '\u0027',
   '\u0028',       '\u0029',       '\u002A',       '\u002B',
   '\u002C',       '\u002D',       '\u002E',       '\u002F',
   '\u0030',       '\u0031',       '\u0032',       '\u0033',
   '\u0034',       '\u0035',       '\u0036',       '\u0037',
   '\u0038',       '\u0039',       '\u003A',       '\u003B',
   '\u003C',       '\u003D',       '\u003E',       '\u003F',
   '\u0040',       '\u0041',       '\u0042',       '\u0043',
   '\u0044',       '\u0045',       '\u0046',       '\u0047',
   '\u0048',       '\u0049',       '\u004A',       '\u004B',
   '\u004C',       '\u004D',       '\u004E',       '\u004F',
   '\u0050',       '\u0051',       '\u0052',       '\u0053',
   '\u0054',       '\u0055',       '\u0056',       '\u0057',
   '\u0058',       '\u0059',       '\u005A',       '\u005B',
   '\u005C',       '\u005D',       '\u005E',       '\u005F',
   '\u0027',       '\u0041',       '\u0042',       '\u0043',
   '\u0044',       '\u0045',       '\u0046',       '\u0047',
   '\u0048',       '\u0049',       '\u004A',       '\u004B',
   '\u004C',       '\u004D',       '\u004E',       '\u004F',
   '\u0050',       '\u0051',       '\u0052',       '\u0053',
   '\u0054',       '\u0055',       '\u0056',       '\u0057',
   '\u0058',       '\u0059',       '\u005A',       '\u007B',
   '\u007C',       '\u007D',       '\u007E',       '\u25C0',
]


def dec_color():
    return _(r'\^\d')


def hex_color():
    return _(r'\^x[0-9a-f]{3}', ignore_case=True)


def literal_caret():
    return '^^'


def character():
    return _('.')


def dp_token():
    return OrderedChoice([dec_color, hex_color, literal_caret, character])


def dp_string():
    return ZeroOrMore(dp_token)


def parse(text, debug=False):
    parser = ParserPython(dp_string, debug=debug)
    return parser.parse(text)