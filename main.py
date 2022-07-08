import os
import datetime
from flask import Flask, render_template, request, redirect, session, url_for, Blueprint
from werkzeug.utils import secure_filename
from xml.dom.minidom import parse
from graphviz import Digraph
from alphaminer import test_data
from handle_xes import handle_test
# from alphaminer import s_TITO,s_NoTITO,g,TI, TO,TL ,Digraph,YL
hai = Blueprint("hai", __name__, url_prefix="/ports/9012")

app = Flask(__name__)

# @app.route("/index", methods = ["GET", "POST"])
@app.route("/index", methods = ["GET"])
def hello_world():
	image=None
	if request.method == "POST":
		file = request.files['file']
		print(file)
		if file:
			filename = secure_filename(file.filename)
			image= os.path.join("upload_folder", filename)
			file.save(os.path.join("upload_folder", filename))
			print('file uploaded successfully!') 
		return redirect(url_for("index"), code=302)
	return render_template("index.html", image=image)

def parse_xes_file(path):
    # dom1 = parse('webservice/upload_folder/L1.xes')
	
    dom1 = parse(path)

    traces = dom1.getElementsByTagName("trace")
    L = []
    for trace in traces:
        event_list = []
        events = trace.getElementsByTagName("event")
        for event in events:
            for n in event.childNodes:
                try:
                    if n.attributes['key'].value == "concept:name":
                        event_list.append(n.attributes["value"].value)
                except:
                    pass

    L.append(event_list)
    return L

def parse_data(data):
	# TODO 在这里处理解析出来的数据生成图片后
	# 并保存到static目录下,并将图片名返回
	return test_data(data)

# @app.route("/image/<image>", methods = ["GET"])
@hai.route("/image/<image>", methods = ["GET"])
def image(image):
	image = "ports/9012/static/{}".format(image)
	print(image)
	return render_template("index.html", image=image)

# @app.route("/upload", methods = ["POST"])
@hai.route("/upload", methods = ["POST"])
def upload():
	image=None
	file = request.files['file']
	print(file)
	if file:
		filename = secure_filename(file.filename)
		image= os.path.join("upload_folder", filename)
		file.save(os.path.join("upload_folder", filename))
		lll = handle_test(image)

		# TODO 完成图片生成函数, 保存图片到 static 目录下
		# 这里合适算法生成图片后保存到 static 目录下
		# 并把文件名赋值给 image 变量
		image = parse_data(lll)
		print(lll)
	# return redirect(url_for(".ports/image", image=image), code=302)
	return render_template("index.html", image=image)

app.register_blueprint(hai)

if __name__ == '__main__':
    app.run(debug=True)