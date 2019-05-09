#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt

coinName = ["USD/JPY", "NZD/JPY", "GBP/JPY", "EUR/USD", "AUD/USD", "AUD/JPY"]

with open('RateLog_0.txt', 'r') as f:
	reader = csv.reader(f)

	for row in reader	:
		print row[0]