import os
import datetime
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.utils import secure_filename
from xml.dom.minidom import parse
from alphaminer import s_TITO,s_NoTITO,g,TI, TO,TL ,Digraph,YL


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
	s_TITO = TI|TO
	s_NoTITO = TL - s_TITO
	g = Digraph(comment='petri-net',format='png')
	g.node('iL',shape = 'circle') 
	for first in TI:
		g.node(name = first,shape = 'square')		
	for s_no in s_NoTITO:
		g.node(name = s_no,shape='square')
	for last in TO:
		g.node(name = last,shape = 'square')
	g.node('oL',shape = 'doublecircle')

	i = 0
	def circle_nodes():
		global i 
		i +=1
	# return str(i)
		example_image = "Digraph.gv.png"
		return example_image

	for set_pairs in YL:
		(set_first,set_second) = set_pairs
		name1 =circle_nodes()   
		g.node(name=name1,label='',shape = 'circle') 

		for set_name in set_second:
			g.edge(tail_name=name1,head_name=set_name)
		for set_name in set_first:
			g.edge(tail_name=set_name,head_name= name1)
	g.edges(('iL', first) for first in TI)
	g.edges((last,'oL') for last in TO)

	#g.view()
	# example_image = "21084-err.png"
	# example_image = "Digraph.gv.png"
	# return example_image

@app.route("/image/<image>", methods = ["GET"])
def image(image):
	image = "/static/{}".format(image)
	return render_template("index.html", image=image)

@app.route("/upload", methods = ["POST"])
def upload():
	image=None
	file = request.files['file']
	print(file)
	if file:
		filename = secure_filename(file.filename)
		image= os.path.join("upload_folder", filename)
		file.save(os.path.join("upload_folder", filename))
		lll = parse_xes_file(image)

		# TODO 完成图片生成函数, 保存图片到 static 目录下
		# 这里合适算法生成图片后保存到 static 目录下
		# 并把文件名赋值给 image 变量
		image = parse_data(lll)
		print(lll)
	return redirect(url_for("image", image=image), code=302)

if __name__ == '__main__':
    app.run(debug=True)