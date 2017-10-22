from datetime import datetime

def get_time():
    now = datetime.utcnow()
    f = open('start_time.txt', 'r+')
    then = f.read()
    if len(then) == 0:
        then = now.isoformat()
        f.write(then)
        f.close() #if no start time, set start time, isoformat is redundant, but only for first instance
    else:
        f.close()

    format_then = datetime.strptime(then, '%Y-%m-%dT%H:%M:%S.%f') #formats isoformat to readable datetime object
    tdelta = now - format_then
    elapsedSec = tdelta.total_seconds()

    return [now, elapsedSec]


def get_timestamp():
    stamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    return str(stamp)
