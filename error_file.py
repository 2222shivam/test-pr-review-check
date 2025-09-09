def foo()
    print("missing colon")

import threading
def run():
    t = threading.Thread(target=print, args=("test",))
    t.start()