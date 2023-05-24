from threading import Thread
print('setting_text create')
http_str = ''
coin_hive = ''
conclusion = ''
output_text = {'http': http_str, 'canhive': coin_hive, 'conclusion': conclusion}
failure_warning = 'this is a warning msg'
flag = True
update_text = 'agfsdgdasf'
setting_text = 'setting'
advice_text = 'advice_text'


def scan(url: str):
    pass

def call_scan(url: str):
    t = Thread(target=scan, args=[url])
    t.start()

def change_update_text(text: str):
    global update_text
    update_text = text

def update(text: str):
    # 可能传过来是['a', 'b', 'c']，要重新链接，可能text = text.join()可以连接起来，建议查百度
    pass

def call_update():
    global setting_text
    t = Thread(target=scan, args=[setting_text])
    t.start()
    setting_text = update_text = ''

if __name__ == '__main__':
    a = 'sasdf'
    b = a
    b = 'd'
    print(a)
