import os
from typing import Self

import httpx


class JD:
    def __init__(self: Self) -> None:
        self.client = httpx.Client(follow_redirects=True)
        self.url = "https://api.m.jd.com"
        self.params = {
            "appid": "item-v3",
            "functionId": "pc_club_productPageComments",
            "score": "0",
            "sortType": "5",
        }

    def get_comments(self: Self, productId: str, page: str, pageSize: str) -> dict:
        params = {"productId": productId, "page": page, "pageSize": pageSize}
        params.update(self.params)

        return self.client.get(self.url, params=params).json()

    def save_comments(
        self: Self,
        productId: str,
        page: str,
        pageSize: str,
        filename: str | None = None,
    ) -> None:
        params = {"productId": productId, "page": page, "pageSize": pageSize}
        params.update(self.params)

        if filename is None:
            if not os.path.exists("comments"):
                os.mkdir("comments")
            filename = f"comments/{productId}_{page}_{pageSize}.json"

        with open(filename, "w") as f:
            f.write(self.client.get(self.url, params=params).text)


if __name__ == "__main__":
    productId = input("please input productId: ")
    content = ""

    jd = JD()
    for i in range(100):
        comments = jd.get_comments(productId, str(i), "10")
        for j in comments["comments"]:
            content += j["content"]
        print(f"page {i} resolved, {len(content)} characters in total")

    with open(f"{productId}.txt", "w") as f:
        f.write(content)
