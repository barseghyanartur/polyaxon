# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from polyaxon.utils import config

SECRET_KEY = config.get_string('POLYAXON_SECRET_KEY', is_secret=True)
