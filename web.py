from flask import Flask,request
from flask import render_template
import block

app = Flask(__name__)

@app.route("/")
def first_page():
	return render_template("block.html")

@app.route("/create_block/",methods=["GET","POST"])
def create_block():
	if request.method=="POST":
		data = request.form["data"]
		new_block=block.create_block(block.previous_block,data)
		block.blockchain.append(new_block)
		block.previous_block = new_block

		return "Data Saved"
	else:
		return "Faild to Save the Data"

@app.route("/all_data/")
def all_data():
	name = block.get_data(block.blockchain)
	return render_template("all.html",name=name)


if __name__ == "__main__":
	app.run(debug=True)
