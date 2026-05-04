from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger # 使用 astrbot 提供的 logger 接口
import astrbot.api.message_components as Comp
from astrbot.api import AstrBotConfig
from astrbot.api.provider import ProviderRequest

@register("astrbot_plugin_astrbot_dev_plg", "c1f5d2dd", "收到任何消息时打印消息链", "v1.0")
class MessageLoggerPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.event_message_type(filter.EventMessageType.ALL)

    async def on_message(self, event: AstrMessageEvent):
        """收到任何消息时，用 logger 打印消息链"""
        message_chain = event.message_obj.message
        logger.info(f"收到消息链: {message_chain}")
        # 不阻断消息，让其他插件继续处理
        return None
