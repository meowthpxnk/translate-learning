from MeowthLogger import Logger

from app.__processer.runner import Runner
from app.settings import settings


logger = Logger(
    use_uvicorn=True,
    logger_level=settings.logger.level.value,
)


def main():
    import app.root
    from app.loop import loop

    loop.run_forever()


def run():
    try:
        Runner("app", main, ()).run_forever()
    except Exception as err:
        logger.error(f"Shutting down, reason {err}")
