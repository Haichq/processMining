import os
import datetime
from flask import Flask, render_template, request, redirect, session, url_for, abort
from werkzeug.utils import secure_filename
from xml.dom.minidom import parse
from graphviz import Digraph
from alphaminer import test_data
from handle_xes import handle_test

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
	return test_data(data)

@app.route("/image/<image>", methods = ["GET"])
def image(image):
	image = "/static/{}".format(image)
	print(image)
	return render_template("index.html", image=image)


@hai.route("/upload", methods = ["POST"])
# @app.route("/upload", methods = ["POST"])
def upload():
	image=None
	file = request.files['file']
	print(file)
	if file:
		filename = secure_filename(file.filename)
		image= os.path.join("upload_folder", filename)
		file.save(os.path.join("upload_folder", filename))
		lll = handle_test(image)

		image = parse_data(lll)
		print(lll)
	# return redirect(url_for("image", image=image), code=302)
	return redirect(url_for("/ports/9012/static/somefile.png", image=image), code=302)
	
app.register_blueprint(hai)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")




if __name__ == '__main__':
    app.run(debug=True)

def main():
	if __name__ == '__main__':
		app.run(host="::1", port = 9012)
main()