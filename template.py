#!/usr/bin/python3.9
# Copyright (c) 2021 MobileCoin Inc.
# Copyright (c) 2021 The Forest Team
import logging
from forest.core import QuestionBot, Message, Response, run_bot
from aiohttp import web


class TemplateBot(QuestionBot):
    async def do_template(self, message: Message) -> str:
        """
        A template you can fill in to make your own bot. Anything after do_ is a / command.
        Return value is used to send a message to the user.
        """
        return "template"

    async def do_echo(self, message: Message) -> str:
        """
        Repeats what you said. Type /echo foo and the bot will say "foo".
        """
        return message.text

    async def do_ask_color(self, message: Message) -> str:
        "Asks for your favorite color"
        answer = await self.ask_freeform_question(
            message.source, "What's your favorite color?"
        )
        return f"That's funny, my favorite color is {answer}, too!"

    async def start_process(self) -> None:
        logging.info("my startup code goes here")
        await super().start_process()

    async def handle_message(self, message: Message) -> Response:
        logging.info("my custom handling logic goes here")
        return await super().handle_message(message)


async def my_webhook_handler(request: web.Request) -> web.Response:
    bot = request.app.get("bot")
    if not bot:
        return web.Response(status=504, text="Sorry, no live workers.")
    data = request.query.get("my_query_parameter")
    await bot.admin(f"webhook got hit. data: {data}")


if __name__ == "__main__":
    run_bot(TemplateBot)
