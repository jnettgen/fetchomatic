import requests, json, os, sys, csv
from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)
#Avoid using cached file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/targets", methods=["POST"])
def main():
	user_url = request.form.get("user_url")
	if (len(user_url)) <= 0:
		return render_template("error.html", message="You didn't enter a community URL. Please go back and try again.")
	user_url = (f"https://{user_url}/v1/targets")
	try:
		response = requests.get(user_url)
	except requests.ConnectionError:
		return render_template("error.html", message="Couldn't connect to endpoint. Please verify that you entered the URL correctly.")
	data = response.json()
	#Create JSON File
	with open('output.json', 'w', encoding='utf-8') as i:
		json.dump(data, i, ensure_ascii=False, indent=4)
	#Create TXT File from JSON Response
	with open("output.txt", "w") as f:
		for unit in data['definitions']:
			print("\n" + '-'*35, file=f)
			print(f"Target: {unit['name']}", file=f)
			print(f"id:   {unit['id']}", file=f)
			for childTarget in unit['childTargets']:
				print(f"        name:  {childTarget['name']}", file=f)
				print(f"        definitionId:  {childTarget['definitionId']}", file=f)
				print(f"        id:  {childTarget['id']}\n", file=f)
				try:
					for sub in childTarget['childTargets']:
						print(f" 			name:  {sub['name']}", file=f)
						print(f" 			parentId:  {sub['parentId']}", file=f)
						print(f" 			definitionId: {sub['definitionId']}", file=f)
						print(f" 			id: {sub['id']}\n", file=f)
				except:
					continue
				try:
					for sub2 in sub['childTargets']:
						print(f" 				name:  {sub2['name']}", file=f)
						print(f" 				parentId:  {sub2['parentId']}", file=f)
						print(f" 				definitionId: {sub2['definitionId']}", file=f)
						print(f" 				id: {sub2['id']}\n", file=f)
				except:
					continue
				try:
					for sub3 in sub2['childTargets']:
						print(f" 					name:  {sub3['name']}", file=f)
						print(f" 					parentId:  {sub3['parentId']}", file=f)
						print(f" 					definitionId: {sub3['definitionId']}", file=f)
						print(f" 					id: {sub3['id']}\n", file=f)
				except:
					continue
	#Create CSV File....later
	return render_template("success.html")
@app.route('/return-file-txt')
def return_txt():
	return send_file("output.txt")

@app.route('/return-file-csv')
def return_csv():
	return send_file('output.csv')

@app.route('/return-file-json')
def return_json():
	return send_file('output.json')