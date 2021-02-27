import os, util, requests, urllib.parse


log = util.get_logger()

def ping(url = None):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        log.info('{code} Successful'.format(code=r.status_code))
    except Exception as e:
        log.error(e)

def main():
    ping(os.environ.get('TARGET'))


if __name__ == '__main__':
    main()
