import csv
import random
from flask import Flask, request, jsonify, render_template, Blueprint

old_bp = Blueprint('old_bp', __name__, template_folder='templates')



@old_bp.route('/ohho')
def index():
    # Render the HTML template for the index page
    return render_template('ohho.html')

@old_bp.route('/hooh')
def intwodex():
    return render_template('hooh.html')

@old_bp.route('/landing')
def mf():
    return render_template('page.html')

@old_bp.route('/landing2')
def of():
    return render_template('page2.html')

@old_bp.route('/landing3')
def odds():
    return render_template('page3.html')

@old_bp.route('/kdk')
def ldnsd():
    return render_template('iit.html')

@old_bp.route('/')
def mai():
    return render_template('index.html')

@old_bp.route('/modern')
def modern_predictor():
    return render_template('modern_predictor.html')

@old_bp.route('/hooh/process_data', methods=['POST'])
def proces_data():
    data = request.json

    if data is None:
        return jsonify({'error': 'No JSON data received'}), 400

    # Extracting values from JSON data
    quota = data.get('quota')
    category = data.get('category')
    gender = data.get('gender')
    college = data.get('college')
    branch = data.get('branch')
    collegename = data.get('collegename')

    # Check for missing required fields
    if None in (quota, category, gender, college, branch, collegename):
        return jsonify({'error': 'Missing required fields in JSON data'}), 400

    results = []

    try:
        if college=="ALL":
            with open("oldjosaa.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if collegename=="ALL":
                        if branch=="ALL":
                            if quota==row[2] and gender== "MALE" and row[3] == category:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                        else:
                            if quota==row[2] and gender == "MALE" and row[3] == category and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                    else:
                        if branch=="ALL":
                            if quota==row[2] and gender == "MALE" and row[3] == category and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                        else:
                            if quota==row[2] and gender == "MALE" and row[3] == category and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})


        if college=="NIT":
            with open("oldnit.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if collegename=="ALL":
                        if branch=="ALL":
                            if quota==row[2] and gender == "MALE" and row[3] == category:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                        else:
                            if quota==row[2] and gender == "MALE" and row[3] == category and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                    else:
                        if branch=="ALL":
                            if quota==row[2] and gender == "MALE" and row[3] == category and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                        else:
                            if quota==row[2] and gender == "MALE" and row[3] == category and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})

        if college=="IIIT":
            with open("oldiiit.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if collegename=="ALL":
                        if branch=="ALL":
                            if quota==row[2] and gender == "MALE" and row[3] == category:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                        else:
                            if quota==row[2] and gender == "MALE" and row[3] == category and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                    else:
                        if branch=="ALL":
                            if quota==row[2] and gender == "MALE" and row[3] == category and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                        else:
                            if quota==row[2] and gender == "MALE" and row[3] == category and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
        if college=="GFTI":
            with open("oldgfti.csv", "r") as f:
                reader = csv.reader(f)

                for row in reader:
                    if collegename=="ALL":
                        if branch=="ALL":
                            if quota==row[2] and gender == "MALE" and row[3] == category:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                        else:
                            if quota==row[2] and gender == "MALE" and row[3] == category and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                    else:
                        if branch=="ALL":
                            if quota==row[2] and gender == "MALE" and row[3] == category and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                        else:
                            if quota==row[2] and gender == "MALE" and row[3] == category and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})
                            elif quota==row[2] and gender == "FEMALE" and row[3] == category and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({"College": row[0], "Branch": row[1],"Category" : row[3], "Opening Rank" : row[5], "Closing Rank": row[6]})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(results)


@old_bp.route('/ohho/process_data', methods=['POST'])
def process_data():
    data = request.json

    if data is None:
        return jsonify({'error': 'No JSON data received'}), 400

    rank = data.get('rank')
    category = data.get('category')
    gender = data.get('gender')
    college = data.get('college')
    branch = data.get('branch')
    collegename=data.get('collegename')
    hs=data.get('hs')
    if None in (rank, category, gender,college,branch,collegename,hs):
        return jsonify({'error': 'Missing required fields in JSON data'}), 400

    results = []

    try:
        if college=="ALL":
            with open("josaa.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if collegename=="ALL":
                        if branch=="ALL":
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[2]=="AI":
                                if row[4] == "Neutral":
                                    results.append({ "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI":
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI":
                                if row[4] == "Neutral":
                                    results.append({ "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI":
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                        else:
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[2]!="AI" and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                    else:
                        if branch=="ALL":
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                        else:
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})


        if college=="NIT":
            with open("nit.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if collegename=="ALL":
                        if branch=="ALL":
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[2]=="AI":
                                if row[4] == "Neutral":
                                    results.append({ "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI":
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" :
                                if row[4] == "Neutral":
                                    results.append({ "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI":
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                        else:
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                    else:
                        if branch=="ALL":
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                        else:
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})

        if college=="IIIT":
            with open("iiit.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if collegename=="ALL":
                        if branch=="ALL":
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[2]=="AI":
                                if row[4] == "Neutral":
                                    results.append({ "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI":
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" :
                                if row[4] == "Neutral":
                                    results.append({ "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI":
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                        else:
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                    else:
                        if branch=="ALL":
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                        else:
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
        if college=="GFTI":
            with open("gfti.csv", "r") as f:
                reader = csv.reader(f)

                for row in reader:
                    if collegename=="ALL":
                        if branch=="ALL":
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[2]=="AI":
                                if row[4] == "Neutral":
                                    results.append({ "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI":
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI":
                                if row[4] == "Neutral":
                                    results.append({ "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI":
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                        else:
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                    else:
                        if branch=="ALL":
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                        else:
                            if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]=="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]=="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Neutral":
                                    results.append({  "College": row[0], "Branch": row[1]})
                            elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[2]==hs and row[2]!="AI" and row[1]==branch and collegename==row[0]:
                                if row[4] == "Female":
                                    results.append({  "College": row[0], "Branch": row[1]})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(results)

@old_bp.route('/kdk/process_data', methods=['POST'])
def process_dat():
    data = request.json

    if data is None:
        return jsonify({'error': 'No JSON data received'}), 400

    rank = data.get('rank')
    category = data.get('category')
    gender = data.get('gender')
    branch = data.get('branch')
    collegename=data.get('collegename')
    if None in (rank, category, gender,branch,collegename):
        return jsonify({'error': 'Missing required fields in JSON data'}), 400

    results = []

    try:

        with open("iit.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if collegename=="ALL":
                    if branch=="ALL":
                        if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category:
                            if row[4] == "Neutral":
                                results.append({"Quota" : row[2],  "College": row[0], "Branch": row[1]})
                        elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category :
                            if row[4] == "Female":
                                results.append({ "Quota" : row[2], "College": row[0], "Branch": row[1]})
                    else:
                        if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category and row[1]==branch:
                            if row[4] == "Neutral":
                                results.append({ "Quota" : row[2], "College": row[0], "Branch": row[1]})
                        elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and  row[1]==branch:
                            if row[4] == "Female":
                                results.append({  "Quota" : row[2],"College": row[0], "Branch": row[1]})
                else:
                    if branch=="ALL":
                        if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category  and collegename==row[0]:
                            if row[4] == "Neutral":
                                results.append({ "Quota" : row[2], "College": row[0], "Branch": row[1]})
                        elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category  and collegename==row[0]:
                            if row[4] == "Female":
                                results.append({ "Quota" : row[2], "College": row[0], "Branch": row[1]})
                    else:
                        if int(rank) <= int(row[6]) and gender == "MALE" and  row[3] == category  and row[1]==branch and collegename==row[0]:
                            if row[4] == "Neutral":
                                results.append({ "Quota" : row[2], "College": row[0], "Branch": row[1]})
                        elif int(rank) <= int(row[6]) and gender == "FEMALE" and  row[3] == category and row[1]==branch and collegename==row[0]:
                            if row[4] == "Female":
                                results.append({  "Quota" : row[2],"College": row[0], "Branch": row[1]})


    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(results)

@old_bp.route('/compare')
def compare_page():
    return render_template('compare.html')

@old_bp.route('/improved_ohho')
def improved_ohho():
    return render_template('improved_ohho.html')

@old_bp.route('/get_colleges', methods=['GET'])
def get_colleges():
    college_type = request.args.get('type', 'ALL')
    
    colleges = set()
    
    try:
        # Process 2024 data
        if college_type == 'ALL' or college_type == 'NIT':
            with open("josaa2024.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    
                    college_name = row[0]
                    if "National Institute of Technology" in college_name or "NIT" in college_name:
                        colleges.add(college_name)
                        
            with open("okom.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    
                    college_name = row[0]
                    if "National Institute of Technology" in college_name or "NIT" in college_name:
                        colleges.add(college_name)
                        
        if college_type == 'ALL' or college_type == 'IIIT':
            with open("josaa2024.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    
                    college_name = row[0]
                    if "Indian Institute of Information Technology" in college_name or "IIIT" in college_name:
                        colleges.add(college_name)
                        
        if college_type == 'ALL' or college_type == 'GFTI':
            with open("josaa2024.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    
                    college_name = row[0]
                    if not ("National Institute of Technology" in college_name or "NIT" in college_name) and not ("Indian Institute of Information Technology" in college_name or "IIIT" in college_name) and not ("Indian Institute of Technology" in college_name or "IIT" in college_name):
                        colleges.add(college_name)
        
        return jsonify(sorted(list(colleges)))
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@old_bp.route('/get_branches', methods=['GET'])
def get_branches():
    college_names = request.args.getlist('colleges[]')
    
    branches = set()
    
    try:
        if not college_names:
            # Return all branches if no colleges selected
            with open("josaa2024.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    
                    branches.add(row[1])
                    
            with open("okom.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    
                    branches.add(row[1])
        else:
            # Return branches for specific colleges
            with open("josaa2024.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    
                    if row[0] in college_names:
                        branches.add(row[1])
                        
            with open("okom.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    
                    if row[0] in college_names:
                        branches.add(row[1])
                        
        return jsonify(sorted(list(branches)))
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@old_bp.route('/predict_colleges', methods=['POST'])
def predict_colleges():
    data = request.json
    
    if data is None:
        return jsonify({'error': 'No JSON data received'}), 400
    
    rank = data.get('rank')
    category = data.get('category')
    gender = data.get('gender')
    home_state = data.get('home_state', 'AI')  # Default to All India if not provided
    college_type = data.get('college_type', 'ALL')
    college_names = data.get('college_names', [])
    branches = data.get('branches', [])
    seat_filter = data.get('seat_filter', 'all')  # New parameter for seat type filtering
    
    if None in (rank, category, gender) or not college_names or not branches:
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        rank = int(rank)
    except ValueError:
        return jsonify({'error': 'Rank must be a number'}), 400
    
    results_2023 = []
    results_2024 = []
    
    try:
        # Process 2023 data
        process_data(results_2023, "nit.csv", rank, category, gender, home_state, college_type, college_names, branches, "2023", seat_filter)
        process_data(results_2023, "iiit.csv", rank, category, gender, home_state, college_type, college_names, branches, "2023", seat_filter)
        process_data(results_2023, "gfti.csv", rank, category, gender, home_state, college_type, college_names, branches, "2023", seat_filter)
        
        # Process 2024 data
        process_data(results_2024, "josaa2024.csv", rank, category, gender, home_state, college_type, college_names, branches, "2024", seat_filter)
        process_data(results_2024, "okom.csv", rank, category, gender, home_state, college_type, college_names, branches, "2024", seat_filter)
        
        # Combine results
        combined_results = combine_results(results_2023, results_2024, rank)
        
        return jsonify(combined_results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@old_bp.route('/get_quotas', methods=['GET'])
def get_quotas():
    quotas = set()
    
    try:
        # Process all CSV files to extract unique quota values
        csv_files = ["josaa2024.csv", "okom.csv", "nit.csv", "iiit.csv", "gfti.csv"]
        
        for filename in csv_files:
            try:
                with open(filename, "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if len(row) > 2:  # Make sure the row has a quota column
                            # Only add non-AI quotas
                            if row[2] != "AI":
                                quotas.add(row[2])
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
        
        # Sort quotas alphabetically
        sorted_quotas = sorted(list(quotas))
            
        return jsonify(sorted_quotas)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def process_data(results, csv_file, rank, category, gender, home_state, college_type, college_names, branches, year, seat_filter='all'):
    try:
        # First pass: collect all matches to check for state quota existence
        state_quota_exists = set()  # Store (college, branch) pairs that have state quota
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 7:
                    continue
                
                college_name = row[0]
                branch_name = row[1]
                quota = row[2]
                
                # If this college+branch has a state quota seat, record it
                if quota == home_state and quota != "AI":
                    state_quota_exists.add((college_name, branch_name))
        
        # Second pass: process and add results
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            
            for row in reader:
                if len(row) < 7:  # Ensure row has required columns
                    continue
                
                college_name = row[0]
                branch_name = row[1]
                quota = row[2]
                cat = row[3]
                seat_type = row[4]
                closing_rank = row[6]
                
                # Skip if college or branch not in selected lists
                if college_names != ["ALL"] and college_name not in college_names:
                        continue
                    
                if branches != ["ALL"] and branch_name not in branches:
                        continue
                
                # Check college type match
                if college_type != "ALL":
                    if college_type == "NIT" and not ("National Institute of Technology" in college_name or "NIT" in college_name):
                        continue
                    elif college_type == "IIIT" and not ("Indian Institute of Information Technology" in college_name or "IIIT" in college_name):
                        continue
                    elif college_type == "GFTI" and (
                        "National Institute of Technology" in college_name or 
                        "NIT" in college_name or 
                        "Indian Institute of Information Technology" in college_name or 
                        "IIIT" in college_name or 
                        "Indian Institute of Technology" in college_name or 
                        "IIT" in college_name
                    ):
                        continue
                
                # Continue if rank doesn't match criteria
                try:
                    closing_rank = int(closing_rank)
                except:
                    continue
                
                if rank > closing_rank:
                    continue
                
                # Match category
                if cat != category:
                    continue
                
                # Skip AI quota if state quota exists for this college+branch
                if quota == "AI" and (college_name, branch_name) in state_quota_exists:
                    continue
                
                # Only accept AI or selected home state quota
                if quota != "AI" and quota != home_state:
                    continue
                
                # Apply seat type filtering based on gender and seat_filter parameter
                # For male candidates, only show Gender Neutral seats
                if gender == "MALE":
                    if seat_type != "Neutral" and seat_type != "Gender Neutral":
                        continue
                else:  # Female candidates
                    # Apply additional seat_filter if specified
                    if seat_filter == 'female' and seat_type != "Female" and seat_type != "Female Only":
                        continue
                    elif seat_filter == 'neutral' and seat_type != "Neutral" and seat_type != "Gender Neutral":
                        continue
                    # For 'all', include both types
                
                # Standardize seat type naming
                if seat_type == "Female" or seat_type == "Female Only":
                    seat_type = "Female Only"
                else:
                    seat_type = "Gender Neutral"
                
                # Add the result
                result = {
                            "College": college_name,
                            "Branch": branch_name,
                            "Quota": quota,
                    "Category": cat,
                    "Seat Type": seat_type,
                    "Closing Rank": closing_rank,
                            "Year": year
                        }
                
                results.append(result)
            
    except Exception as e:
        print(f"Error processing {csv_file}: {str(e)}")
        # Continue processing other files even if one fails

def combine_results(results_2023, results_2024, user_rank):
    combined = []
    seen_combinations = set()  # Track unique college-branch combinations
    
    # Process 2024 data first
    for result in results_2024:
        college_branch = (result["College"], result["Branch"])
        
        # Skip if we've already processed this college-branch combination
        if college_branch in seen_combinations:
            continue
            
        seen_combinations.add(college_branch)
        closing_rank = int(result["Closing Rank"])
        
        # Calculate probability based on rank difference
        probability = calculate_probability(user_rank, closing_rank)
        
        # Only include if probability is high enough based on rank
        if should_include_by_probability(user_rank, closing_rank):
            # Ensure we have all required fields
            combined_result = {
                "College": result["College"],
                "Branch": result["Branch"],
                "Category": result.get("Category", ""),
                "Quota": result.get("Quota", "AI"),
                "Seat Type": result.get("Seat Type", "Gender Neutral"),
                "Closing Rank 2024": result["Closing Rank"],
                "Probability": probability
            }
            
            combined.append(combined_result)
    
    # Add 2023 data if not already present - BUT ONLY if it also exists in 2024
    # We're skipping entries that are only in 2023 data
    for result in results_2023:
        college_branch = (result["College"], result["Branch"])
        
        # Check if this college-branch is already in combined results
        exists = False
        for item in combined:
            if (item["College"], item["Branch"]) == college_branch:
                # Update existing entry with 2023 data
                item["Closing Rank 2023"] = result["Closing Rank"]
                # If 2023 has a different quota, note it
                if "Quota" in result and item.get("Quota") != result["Quota"]:
                    item["Quota 2023"] = result["Quota"]
                exists = True
                break
        
        # We're skipping entries that are only in 2023 data
        # So we don't add new entries here
    
    # Sort by closing rank (low to high)
    combined.sort(key=lambda x: int(x.get("Closing Rank 2024", x.get("Closing Rank 2023", "999999"))))
    
    return combined

def calculate_probability(user_rank, closing_rank):
    rank_diff = closing_rank - user_rank
    
    if rank_diff >= 200:
        return "Very High"
    elif rank_diff >= 100:
        return "High"
    elif rank_diff >= 0:
        return "Medium"
    elif rank_diff >= -100:
        return "Low"
    else:
        return "Very Low"

def should_include_by_probability(user_rank, closing_rank):
    rank_diff = closing_rank - user_rank
    
    if user_rank < 1000:
        # For ranks less than 1000, include if within 30 ranks
        return rank_diff >= -30
    else:
        # For ranks 1000+, include if within 300 ranks
        return rank_diff >= -300

@old_bp.route('/get_categories', methods=['GET'])
def get_categories():
    college_name = request.args.get('college', '')
    gender = request.args.get('gender', '')
    
    # Default categories for most colleges
    default_categories = [
        "OPEN", "OBC-NCL", "EWS", "SC", "ST",
        "OPEN-PWD", "OBC-PWD", "EWS-PWD", "SC-PWD", "ST-PWD"
    ]
    
    # Special cases for colleges without certain categories
    special_cases = {
        "Punjab Engineering College Chandigarh": ["OPEN", "EWS", "SC", "ST", "OPEN-PWD", "EWS-PWD"],
        "Indian Institute of Information Technology (IIIT)Kota Rajasthan": ["OPEN", "OBC-NCL", "EWS", "SC", "ST", "OPEN-PWD", "OBC-NCL-PWD", "EWS-PWD"]
        # Add more special cases as needed
    }
    
    # Check if the college is in our special cases
    unavailable_categories = []
    available_categories = default_categories.copy()
    
    if college_name in special_cases:
        available_categories = special_cases[college_name]
        unavailable_categories = list(set(default_categories) - set(available_categories))
    elif "Punjab Engineering College" in college_name:
        available_categories = special_cases["Punjab Engineering College Chandigarh"]
        unavailable_categories = list(set(default_categories) - set(available_categories))
    
    # Return both available categories and unavailable categories
    return jsonify({
        "available": available_categories,
        "unavailable": unavailable_categories
    })


