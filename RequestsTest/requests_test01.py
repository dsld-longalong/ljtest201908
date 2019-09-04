"""
    这是request的内容
"""
import requests

# get方法
def test_01_get():
    """
        http的get方法
    """

    # 请求网址
    # res = requests.get("https://cn.bing.com/")        # 去请求必应这个网址, res是服务器响应的所有信息
    # print(res.text)                                   # 打印服务器返回的内容

    # 请求接口
    res = requests.get("http://132.232.44.158:8080/morning/getAllGoods")
    print(res.text)             # 服务器返回的内容                 
    print(res.headers)          # 响应的信息头
    print(res.status_code)      # 响应的http状态码
    print(res.cookies)          # 响应的cookie


def test_02_post_formdata():
    """
        post方法的form-data
    """
    # u = "http://132.232.44.158:7777/login"
    # d = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n%E5%AD%99%E7%A7%80%E5%A6%82\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n123456\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    # r = requests.post(url=u, data=d)
    # print(r.status_code)
    # print(r.headers)
    # print(r.text)

    u = "http://132.232.44.158:8080/morning/user/userLogin"
    d = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginName\"\r\n\r\n143@qq.com\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginPassword\"\r\n\r\na123456\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    h = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'User-Agent': "PostmanRuntime/7.16.3",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "6affa827-ac6b-42b0-ad1a-d6ff1f997ac4,575248e2-eaad-4128-a4cd-ed7bd6a8e933",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "session=.eJxlkT1OwzAUx69ivTmRnKQOrTcmpk50R25i2jSuHfyhBlWVKi7AXA4AU7lVqbgFdtMEISZbP733_7C34AzXQLfAFhyodEJEUHAhmqWSv0AwY6oS6Li_y0cFFL4On9_7t_PrEa5csrVfghQnEzwOUHNmua3WgxQvXcFspSQTA5JlN7EF5D1gqmSEMozueYOCEkozmhLqyd10BrsIQpKchJNLW9nnXmil5v1VqM7Fy_kYsirqa7TT8XD-2J_eXzxufOKN0sEzSbMRyT3zgU1Y62Q0XyvLC1WG1dwnGE0IIkkYNEwwPVibYqnU0MjwtjM2yumCX1_OWKbtn6azpYsQTtCtW3RNMQlNk5u-qV-xzgBNoss__euw6_iDVTUPXTeLZp6yjMS5bFVcbySLn4pVHQvJceZWeNzaFnY_qYml-g.XW-3gg.RJTuVqsu06GmR9R32oBpiIIUuA8",
    'Referer': "http://132.232.44.158:7777/login",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

    res = requests.post(url=u, data=d, headers=h)
    print(res.text)


def test_03_post_json():
    """
        post方法的json
    """
    u = "http://132.232.44.158:5000/userLogin/"
    d = {"username":"test", "password":"123456", "captcha":"123456"}
    r = requests.post(url=u, json=d)
    print(r.text)



if __name__ == "__main__":
    # test_01_get()
    # test_02_post_formdata()
    test_03_post_json()