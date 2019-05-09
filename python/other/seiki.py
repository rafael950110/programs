#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

regex = r'ab+'
text = "abbabbabaaabb"
pattern = re.compile(regex)
matchObj = pattern.match(text)