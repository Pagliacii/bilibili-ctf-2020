#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from requests import Response, request

from common import BASE_URL, cookies, headers

url: str = f"{BASE_URL}/api/ctf/2"


def solve(url: str) -> None:
    resp: Response = request(
        method="GET",
        url=url,
        headers=headers,
        cookies=cookies,
    )
    if resp.status_code != 200:
        print(f"error: {resp.status_code}")
        return

    data: dict[str, str] = resp.json()
    if data["code"] == 200:
        print(f'flag2: {data["data"]}')
    else:
        print(f"error: {data}")


if __name__ == "__main__":
    solve(url=url)
