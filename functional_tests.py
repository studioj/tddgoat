"""
# ==============================================================================
# Name:             functional_tests
#                   -
# Purpose:          -
#                   -
#                   -
# Author:           Jef Neefs
# Created:          13/06/2018
# Copyright:        (c) Jef Neefs 2018
# Licence:          GPLv3
# ==============================================================================
# Extra used pypi modules which may need to be installed:
#
# ==============================================================================
"""
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert 'Django' in browser.title