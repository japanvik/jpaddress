#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" jpaddress.py : file created Mon Jun 29 09:46:28 JST 2015 by vjkumar """

import re

REG_JPADDRESS = ur'((北海道|東京都|(大阪|京都)府|(神奈川|和歌山|鹿児島)県|[^\s\w\d　]{2}県)?([^\s\w\d　]{1,6}[市郡区町村][^\s\w\d　]{1,20})[\d０-９〇一-九十上下東西]+[^\s　\'"<）」】]*[\dル号F])[^\d]'


def get_jp_address(data):
    """ return the Address string based on regular expression given a unicode string
    """
    reg = re.compile(REG_JPADDRESS)
    return re.findall(reg, data)

