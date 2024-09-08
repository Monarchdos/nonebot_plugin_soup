"""
Name: ChickenSoup
Author: Monarchdos
Date: 2023-01-11 16:04:41
LastEditTime: 2024-07-15 15:51:41
"""

from httpx import AsyncClient, HTTPError
from nonebot import get_plugin_config, logger, on_command, require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

from .config import Config

require("nonebot_plugin_alconna")

from nonebot_plugin_alconna.uniseg import UniMessage  # noqa: E402

__plugin_meta__ = PluginMetadata(
    name="心灵鸡汤",
    description="来一碗心灵鸡汤吧",
    usage="鸡汤,毒鸡汤",
    type="application",
    homepage="https://github.com/Monarchdos/nonebot_plugin_soup",
    config=Config,
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
)

plugin_config = get_plugin_config(Config)

jt = on_command("鸡汤", priority=1, block=True)


@jt.handle()
async def _():
    await handle("https://api.ayfre.com/jt?type=bot&ver=1.1.0")


djt = on_command("毒鸡汤", priority=1, block=True)


@djt.handle()
async def _():
    await handle("https://api.ayfre.com/djt?type=bot&ver=1.1.0")


async def handle(url: str):
    try:
        async with AsyncClient() as client:
            res = ("\n" if plugin_config.chickensoup_reply_at else "") + (
                await client.get(url, follow_redirects=True)
            ).text
        if "wwwroot" in res or "html" in res or len(res) == 1:
            return
        await UniMessage(res).finish(at_sender=plugin_config.chickensoup_reply_at)
    except HTTPError:
        logger.warning("Server connection failed.")
