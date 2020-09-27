import datetime

start_time = datetime.datetime.now()

def start():
    global start_time
    start_time = datetime.datetime.now()

def finish():
    finish_time = datetime.datetime.now()
    return finish_time - start_time

if __name__ == "__main__":
    print("running as main")

if __name__ == "tracker":
    print("running as module")