import os
import time
import subprocess
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

BOT_SCRIPT = "bot.py"

def start_bot():
    process = subprocess.Popen(["python", BOT_SCRIPT])
    return process

class BotFileHandler(FileSystemEventHandler):
    def __init__(self, process):
        self.process = process
        self.last_mtime = os.path.getmtime(BOT_SCRIPT)

    def on_modified(self, event):
        if event.src_path == os.path.abspath(BOT_SCRIPT):
            current_mtime = os.path.getmtime(BOT_SCRIPT)
            if current_mtime != self.last_mtime:
                print(f"\033[1;32mFile {BOT_SCRIPT} berubah bot akan di restart")
                self.process.terminate()
                self.process.wait()
                self.process = start_bot()
                self.last_mtime = current_mtime

def monitor_changes(process):
    event_handler = BotFileHandler(process)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(os.path.abspath(BOT_SCRIPT)), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    bot_process = start_bot()

    monitor_thread = threading.Thread(target=monitor_changes, args=(bot_process,))
    monitor_thread.daemon = True
    monitor_thread.start()

    # Keep the main thread alive
    while True:
        time.sleep(1)
