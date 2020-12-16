import requests
import json
import time

def test1 ():
    """
    Тест граничных значений 1
    """
    url = 'https://api.hh.ru/vacancies'
    text = "a" * 4096
    send = {"text": text}
    response = requests.get(url, send)
    if response.status_code == 200:
        print("test1 OK")
    else:
        print("test1 fail")


def test2 ():
    """
    Тест граничных значений 2
    """
    url = 'https://api.hh.ru/vacancies'
    text = "a" * 4097
    send = {"text": text}
    response = requests.get(url, send)
    if response.status_code == 502:
        print("test2 OK")
    else:
        print("test2 fail")


def test3 ():
    """
    Принимает ли пустое поле ?
    """
    url = 'https://api.hh.ru/vacancies'
    text = ""
    send = {"text": text}
    response = requests.get(url, send)
    if response.status_code == 200:
        print("test3 OK")
    else:
        print("test3 fail")


def test4 ():
    """
    Принимает ли специфические символы ?
    """
    url = 'https://api.hh.ru/vacancies'
    text = "プログラマー"
    send = {"text": text}
    response = requests.get(url, send)
    if response.status_code == 200:
        print("test4 OK")
    else:
        print("test4 fail")


def test5 ():
    """
    Получим ли одни и те же данные на выходе,
    при одних и тех же данных на входе ?
    """
    url = 'https://api.hh.ru/vacancies'
    text = "Java"
    send = {"text": text}
    response1 = requests.get(url, send)
    time.sleep(0.2)
    response2 = requests.get(url, send)
    dict1 = json.loads(response1.text)
    dict2 = json.loads(response2.text)
    if (dict1["found"] == dict2["found"]):
        print("test5 OK")
    else:
        print("test5 fail")


def test6 ():
    """
    Получим ли разные данные на выходе,
    при разных данных на входе ?
    """
    url = 'https://api.hh.ru/vacancies'
    text = "Java"
    send = {"text": text}
    response1 = requests.get(url, send)
    time.sleep(0.2)
    text = "Python"
    send = {"text": text}
    response2 = requests.get(url, send)
    dict1 = json.loads(response1.text)
    dict2 = json.loads(response2.text)
    if (dict1["found"] != dict2["found"]):
        print("test6 OK")
    else:
        print("test6 fail")


def test7 ():
    """
    Будет ли что то найденно, при бессмысленном запросе ?
    """
    url = 'https://api.hh.ru/vacancies'
    text = "nvk;lrjn ;an;g5nj4g jlgng jglk"
    send = {"text": text}
    response = requests.get(url, send)
    t = json.loads(response.text)
    if t["found"] == 0:
        print("test7 OK")
    else:
        print("test7 fail")


test1()
test2()
test3()
test4()
test5()
test6()
test7()
