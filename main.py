from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import pywintypes
from win10toast import ToastNotifier
import shutil

toast = ToastNotifier()
toast.show_toast("File Oragniser", "The process has been started", duration = 30)
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            d = 0
            if filename != 'Download':
                    try:
                        extension = 'noname'
                        new_name = filename
                        try:
                            extension = str(os.path.splitext(folder_to_track + "\\" + new_name)[1])
                            path = extensions_folder[extension]
                        except Exception:
                            extension = 'noname'
                        file_exist = os.path.isfile(extensions_folder[extension] + "\\" + new_name)
                        while file_exist:
                            i += 1
                            new_name = os.path.splitext(folder_to_track + "\\" + new_name)[0] + str(i) + os.path.splitext(folder_to_track + "\\" + new_name)[1]
                            new_name = new_name.split("\\")[3]
                            file_exist = os.path.isfile(extensions_folder[extension] + "\\" + new_name)

                        src = folder_to_track + "\\" + filename
                        new_name = extensions_folder[extension] + "\\" + new_name
                        #shutil.move(src, new_name)
                        #os.replace(src, new_name)
                        os.rename(src, new_name)
                    except Exception:
                        d = 1
extensions_folder = {
    #Others
    'noname' : "D:\\Download\\Other",
    #Text files
    '.txt' : "D:\\Download\\Text",
    '.doc' : "D:\\Download\\Text",
    '.docx' : "D:\\Download\\Text",
    '.wpd': "D:\\Download\\Text",
    #PDFs
    '.pdf': "D:\\Download\\PDF",
    #Applications
    '.dll': "D:\\Download\\application",
    '.msi': "D:\\Download\\application",
    '.exe': "D:\\Download\\application",
    '.sys': "D:\\Download\\application",
    '.tmp': "D:\\Download\\application",
    '.lnk': "D:\\Download\\application",
    '.apk': "D:\\Download\\application",
    '.iso': "D:\\Download\\application",
    #Media
    '.ico': "D:\\Download\\Media",
    '.jpeg': "D:\\Download\\Media",
    '.jpg': "D:\\Download\\Media",
    '.png': "D:\\Download\\Media",
    '.mp3': "D:\\Download\\Media",
    '.wav': "D:\\Download\\Media",
    '.3g2': "D:\\Download\\Media",
    '.3gp': "D:\\Download\\Media",
    '.flv': "D:\\Download\\Media",
    '.mp4': "D:\\Download\\Media",
    '.mpg': "D:\\Download\\Media",
    '.mpeg': "D:\\Download\\Media",
    '.wmv': "D:\\Download\\Media",
    '.rm': "D:\\Download\\Media",
    #zip
    '.zip': "D:\\Download\\zip",
    '.pkg': "D:\\Download\\zip",
    '.rar': "D:\\Download\\zip",
    '.rpm': "D:\\Download\\zip",
    '.z': "D:\\Download\\zip",
    '.7z': "D:\\Download\\zip"
}

folder_to_track = 'D:\\Download\\0'
#folder_destination = 'D:\\Download'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
