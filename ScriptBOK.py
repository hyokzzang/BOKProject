# -*- coding: <utf-8> -*-

# ------------------------------------------------------------------------------
#
# News Data Analysis Project
#
# Code Author : Kim, Hyok Jung, and Jihyeon Lee
# Date : April 22nd, 2016
#
# ------------------------------------------------------------------------------

# Python standard libraries
import time
import os

# Other packages
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# User defined classes

# Work path
WorkPath = os.path.dirname(os.path.abspath(__file__))


# ------------------------------------------------------------------------------
# Part 1: Read Naver website
# ------------------------------------------------------------------------------

# The target url
BaseURL = 'http://www.google.com'

# Read URL as requests object by upper query
URLobj = requests.Session().get(BaseURL)

# Request object as BeautifulSoup object
soup = BeautifulSoup(URLobj.content, 'lxml')

InputAll = soup.find_all("input")

DictQuery = {}
for inputs in InputAll:
    try:
        DictQuery[inputs['q']] = inputs['value']
    except KeyError:
        pass

SearchWord = "catastrophe"
#SearchWord = SearchWord.encode('utf-8')

DictQuery['query'] = SearchWord

URLobj = requests.Session().post(BaseURL, data=DictQuery)

# Request object as BeautifulSoup object
soup = BeautifulSoup(URLobj.content, 'lxml')