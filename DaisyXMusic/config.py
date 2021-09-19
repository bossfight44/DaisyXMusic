# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAw2KqbU8kTHuoH0Pqy4YFMeWftQN_xLRVDRqtM59v5aWkTsZqQ3hBJaVYk-5RuaaLDrUnkevm_QWq3B8mH8-vnxhsTZkyMAX8hCAt4hx-jBW4gQ1nL9loiLdrkw6nscYcfdX9uPqe0y55TvAUODBidJxtoWAcXlCUw3bWrQOuvPbaf-3gxaOJRLZP3bKk3Yl6yjnIwNF8EYsje3pTgPM_48KFNd9gHcJnmLeZgKLYqoMjYoabn067I9qHUG5IU-cRXfPtvPZRZGHVe-5zSHwKBmL59RbcBWv-a8Kmt0iZfC4PgQCydkZGO9fFZ2zrkCj5w-s_8eGpfSsh9vKQEu9-8aShspwA")
BOT_TOKEN = getenv("1728460388:AAHahTqmohOFyNoS9aBOB0_OjfzAuLmCLE4")
BOT_NAME = getenv("XVII MUSIC")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DaisyXupdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", "5873144"))
API_HASH = getenv("2035ebe3af14748404703adbdf461250")
BOT_USERNAME = getenv("Biawakradibot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "lifeisuckx")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "loveiswarxvii")
PROJECT_NAME = getenv("PROJECT_NAME", "serenitymusic")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "240"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
