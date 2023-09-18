from queue import Queue
from w4af.core.ui.api.utils.scans import start_scan_helper
task_queue = Queue()


#Process the scans
def tasks_processor():
    while True:
        try:
            scan_info = task_queue.get() 
            if scan_info:
                start_scan_helper(scan_info)
        except task_queue.Empty:
            pass
        except Exception as e:
            pass
        finally:
            task_queue.task_done() 

def append_task(scan_info):
    task_queue.put(scan_info)
    