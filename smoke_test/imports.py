import string
import playwright
import requests
import allure
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright
from playwright.sync_api import Page
import json
import random
import string
import requests
import datetime
import datetime
import os
from allure_commons.types import AttachmentType
from allure_commons._allure import attach
from playwright.sync_api import expect

def get_report_path(test_name):
    return f"/Users/sun/Projects/gepur_automation_tests/{test_name}.zip"



