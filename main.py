import os
import time

import dotenv
import schedule
import typer

from larkapp import LarkApp, LarkRSSBot

cli = typer.Typer()


@cli.command()
def run():
    WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")

    bot = LarkRSSBot(secret=WEBHOOK_SECRET, url=WEBHOOK_URL)  # type: ignore
    # app = LarkApp(app_id, app_secret)

    schedule.every(10).minutes.do(bot.run)
    # schedule.every(20).minutes.do(app.run)

    schedule.run_all()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    dotenv.load_dotenv(dotenv_path=".env")

    cli()
