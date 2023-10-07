# Copyright (c) 2022 Itz-fork

import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "23830477"))
    API_HASH = os.environ.get("API_HASH", "19f8365d98fb11c9cd6c1eaa8b1fa4b8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6491987255:AAFL_prlpMzAQzvW31334AXDGnWIojHhJ0o")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6408116706").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT") in ["False", "False"]
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL")) if os.environ.get("-1001888075413") else None
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "")
