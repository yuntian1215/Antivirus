from threading import Thread
import joblib
import pandas as pd

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
test=pd.read_csv("./web/crypto_jacking/test.csv")
X_test=test.drop(["Label","URL"],axis=1)
X_test=X_test.drop(X_test.columns[0],axis=1)

def scan(url: str):
    model=joblib.load("./web/crypto_jacking/model.pkl")
    y_pred=model.predict([[31, 1, 0,0, 0, 1]])
    if y_pred[0]:
        output_text.update([("conclusion","bad")])
    else:
        output_text.update([("conclusion","good")])

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
