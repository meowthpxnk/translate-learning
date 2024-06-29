import os
import signal

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class NotFiltered(Exception):
    def __init__(self) -> None:
        super().__init__("Not filtered event.")


class MyHandler(FileSystemEventHandler):
    disabled_process_flag: bool

    def __init__(self, observer, pid: int, filter):
        self.disabled_process_flag = False
        self.observer = observer
        self.pid = pid
        self.filter = filter

    def disable_process(self):
        self.disabled_process_flag = True

    def on_any_event(self, event):
        try:
            self.filter(event)
        except NotFiltered:
            return
        self.observer.stop()
        if not self.disabled_process_flag:
            os.kill(self.pid, signal.SIGTERM)


class FileObserver:
    def __init__(self, pid: int, obs_path, filter):
        self.observer = Observer()
        self.event_handler = MyHandler(self.observer, pid, filter)

        self.observer.schedule(
            self.event_handler,
            path=obs_path,
            recursive=True,
        )
        self.observer.start()

    def disable_process(self):
        self.event_handler.disable_process()

    def join(self):
        self.observer.join()
