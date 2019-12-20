from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")   # 装饰器
def index():
    iindexhtml = '''
    <!DOCTYPE html>
<html>
<head>
  <title>Bootstrap 实例</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css">
  <script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script>
  <script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center">
  <h1>智哥测试教学</h1>
  <p>厉害！厉害！</p> 
</div>
 
<div class="container">
  <div class="row">
    <div class="col-sm-4">
      <h3>第一列</h3>
      <p>智哥秀场</p>
      <p>学的不仅是技术，更是梦想！！！</p>
    </div>
    <div class="col-sm-4">
      <h3>第二列</h3>
      <p>智哥秀场..</p>
      <p>学的不仅是技术，更是梦想！！！</p>
    </div>
    <div class="col-sm-4">
      <h3>第三列</h3> 
      <p>智哥秀场..</p>
      <p>学的不仅是技术，更是梦想！！！</p>
    </div>
  </div>
</div>

</body>
</html>
    '''
    return iindexhtml

@app.route("/userinfo")
def getuserinfo():
    hdict = {
        "name":"zhangdezhi",
        "phone":"18262620731"
    }
    return jsonify(hdict)

if __name__ == "__main__":
    app.run(debug=True)