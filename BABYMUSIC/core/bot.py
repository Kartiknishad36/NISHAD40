from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
from ..logging import LOGGER


class BABY(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Bot...")
        super().__init__(
            name="BABYMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
            parse_mode=ParseMode.HTML,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = (self.me.first_name or "") + (
            f" {self.me.last_name}" if self.me.last_name else ""
        )
        self.username = self.me.username
        self.mention = self.me.mention

        lid = config.LOGGER_ID
        LOGGER(__name__).info(f"LOGGER_ID from config = {lid!r}")

        if not lid:
            LOGGER(__name__).warning(
                "LOGGER_ID empty/0 — set Railway env LOGGER_ID=-100... "
                "Bot continue without log group."
            )
        else:
            try:
                await self.send_message(
                    chat_id=lid,
                    text=(
                        f"<b>» {self.mention} bot started</b>\n\n"
                        f"ID: <code>{self.id}</code>\n"
                        f"Name: {self.name}\n"
                        f"Username: @{self.username}"
                    ),
                )
                try:
                    a = await self.get_chat_member(lid, self.id)
                    if a.status != ChatMemberStatus.ADMINISTRATOR:
                        LOGGER(__name__).warning(
                            "Bot is not ADMIN in log group — continuing anyway."
                        )
                except Exception as ex:
                    LOGGER(__name__).warning(f"Admin check skipped: {ex}")
            except (errors.ChannelInvalid, errors.PeerIdInvalid) as ex:
                LOGGER(__name__).error(
                    f"Log group invalid (LOGGER_ID={lid}). "
                    f"Add bot to that group & check ID. ({ex})"
                )
                # exit() hata diya — bot band nahi hoga
            except Exception as ex:
                LOGGER(__name__).error(
                    f"Log group fail (LOGGER_ID={lid}): "
                    f"{type(ex).__name__}: {ex}"
                )

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
