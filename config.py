#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7407487191:AAHTf4iqO7gQn_ENUAHl37VsOQxgY29SVaI")
    API_ID = int(os.environ.get("API_ID", "21705536"))
    API_HASH = os.environ.get("API_HASH", "c5bb241f6e3ecf33fe68a444e288de2d")
    AUTH_USERS = "1147534909"

