#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import time

from requests import Response, Session

from common import BASE_URL, cookies

url: str = "{base}/api/ctf/5?uid={uid}"
uid: int = 100336889


def solve(url: str, uid: int) -> None:
    session: Session = Session()
    while True:
        resp: Response = session.get(
            url.format(base=BASE_URL, uid=uid), cookies=cookies
        )
        if resp.status_code != 200:
            print(f"error: {resp.status_code}")
            break

        data: dict[str, str] = resp.json()
        if data["code"] != 200:
            time.sleep(0.1)
            uid += 1
        else:
            print(f'flag5: {uid=}, {data["data"]=}')
            break


if __name__ == "__main__":
    solve(url=url, uid=uid)
