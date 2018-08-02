#!/usr/bin/env python

from parsimonious.grammar import Grammar, Literal, OneOf

grammar = Grammar(
    """
    dot = "\\."
    sign = "[+-]?"
    digits = "[0-9]*"
    complex = "[iIjJ]"
    number = digits / (dot digits) / (digits dot digits)
    scientific = number "[eE]" sign digits
    real = (sign number) / (sign scientific)
    """)


def build_regex(node):

    if isinstance(node, Literal):
        return node.literal

    if isinstance(node, OneOf):
        regex = "|".join(["({})".format(build_regex(x)) for x in node.members])
        return "({})".format(regex)

    result = ''
    for m in node.members:
        result += build_regex(m)

    return result


def create_regex(gram, start):

    assert start in gram

    return build_regex(gram[start])
