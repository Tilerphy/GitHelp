from flask import Flask
from flask import request
import os
import os.path
from urllib import unquote
app=Flask(__name__)

@app.route("/Test", methods=["GET"])
def test():
	print str(request)
	return "OK"

@app.route("/rec/<department>", methods=["GET"])
def rec(department):
	input = open("/home/centos/rec/%s.reck" % department, "a+")
	username = unquote(request.args["u"])
	print username
	input.write("UserName: %s \n" % username.encode("utf-8") )
	input.close();
	return "<script>window.location='/departments'</script>"

@app.route("/list/<department>", methods=["GET"])
def list(department):
	output=open("/home/centos/rec/%s" % department,"r")
	lines = output.readlines()
	result=""
	output.close()
	for line in lines:
		result = "%s%s<br/>" % (result, line)
	return result

@app.route("/departments", methods=["GET"])
def departments():
	result = ""
	for filename in os.listdir("/home/centos/rec/"):
		if not filename.rfind(".reck")==-1:
			print filename
			result = "%s<a href='/list/%s'>%s</a><br/>" % (result, filename, filename)
			print result
	return result


app.run("10.1.54.39",7001)

