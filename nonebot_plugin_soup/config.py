"""
Name: ChickenSoup.Config
Author: Monarchdos
Date: 2024-07-15 15:14:38
LastEditTime: 2024-07-15 15:15:56
"""

from pydantic import BaseModel


class Config(BaseModel):
    chickensoup_reply_at: bool = True
