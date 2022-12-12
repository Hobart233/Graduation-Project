from flask import Flask
app = Flask(__name__)
@app.route("/show/info")
#网页路径URL
#创建了网站/show/info和函数index的对应关系
#以后用户在浏览器上访问/show/s
def index():
    return "中国<span style='color:red;'>联通</span>"

if __name__ == '__main__':
   app.run()
