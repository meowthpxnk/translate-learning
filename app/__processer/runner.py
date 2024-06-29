import asyncio
import logging
import os
import sys
import time

from watchdog.events import FileSystemEvent

from .observer import FileObserver, NotFiltered
from .processes import Application


logger = logging.getLogger()


def filter(event: FileSystemEvent):
    if "__pycache__" in event.src_path:
        raise NotFiltered
    if "__processer" in event.src_path:
        raise NotFiltered
    if "__root" in event.src_path:
        raise NotFiltered


class Runner:
    def __init__(self, dir, target, args):
        self.loop = asyncio.new_event_loop()
        self.app_path = os.path.join(os.path.abspath("."), dir)

        self.target = target
        self.args = args

        self.reload = bool("--reload" in sys.argv)
        self.observer = None

    def run_forever(self, reload=False):
        self.loop.create_task(self.run())
        self.loop.run_forever()

    def run(self):
        self.start_app()
        self.app.join()

        logger.info("Shutting down process\n")

        if self.app.exception:
            error, traceback = self.app.exception
            logger.error(traceback)

            if not self.observer:
                sys.exit(0)

            self.observer.disable_process()
            self.observer.join()

        if not self.observer:
            sys.exit(0)

        logger.info("Restarting process\n")
        time.sleep(1)

        self.loop.create_task(self.run())

    def start_app(self):
        self.app = Application(target=self.target, args=self.args)
        self.app.start()
        logger.info("Start process")

        if self.reload:
            self.observer = FileObserver(self.app.pid, self.app_path, filter)
