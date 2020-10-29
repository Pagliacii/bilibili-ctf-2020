#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from requests import Response, request

from common import BASE_URL, cookies, headers

url: str = f"{BASE_URL}/api/ctf/3"
payload: dict[str, str] = {
    "username": "admin",
    "passwd": "bilibili",
}


def solve(url: str, payload: dict[str, str]) -> None:
    resp: Response = request(
        method="POST",
        url=url,
        cookies=cookies,
        headers=headers,
        json=payload,
    )
    if resp.status_code != 200:
        print(f"error: {resp.status_code}")
        return

    data: dict[str, str] = resp.json()
    if data["code"] == 200:
        print(f'flag3: {data["data"]}')
    else:
        print(f"error: {data}")


if __name__ == "__main__":
    solve(url=url, payload=payload)
