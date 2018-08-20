from grammex.nodes import String, CharClass
from grammex.modifiers import NoneOrOne, Any



def make_regex():
    dot = String('.')
    sign = CharClass('+-') * NoneOrOne()
    digits = CharClass('0-9') * Any()
    eye = CharClass('iIjJ')
    number = digits | (dot + digits) | (digits + dot + digits)
    scientific = number + CharClass('eE') + sign + digits
    real = (sign + number) | (sign + scientific)
    imag = (number + eye) | (scientific + eye)
    return real | (sign + imag) | (real + CharClass('+-') + imag)
