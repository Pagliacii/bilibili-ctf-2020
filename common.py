#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import hashlib
import os
from pathlib import Path

from dotenv import load_dotenv

env_path: Path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

BASE_URL: str = "http://45.113.201.36"
cookies: dict[str, str] = {
    "role": os.getenv("ROLE"),
    "session": os.getenv("SESSION"),
}
headers: dict[str, str] = {"User-Agent": "bilibili Security Browser"}


def md5(content: str, *, encoding: str = "utf-8") -> str:
    return hashlib.md5(content.encode(encoding=encoding)).hexdigest()
