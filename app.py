# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
lgc=pickle.load(open('ipl.pkl', 'rb'))
cl=pickle.load(open('toss.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('chalja.html')
@app.route('/index',methods=["GET",'POST'])
def diabetesPage():
    return render_template('index.html')
@app.route('/index',methods=["GET",'POST'])
def mm():
    return render_template('index.html')
@app.route('/toss',methods=["GET",'POST'])
def dia():
    return render_template('toss.html')
@app.route('/toss',methods=["GET",'POST'])
def tt():
    return render_template('toss.html')
@app.route("/predict", methods = ['POST', 'GET'])
def pred():
    temp_arr = list()
    try:

        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_arr = temp_arr + [1,0,0,0,0,0,0,0]
         
        elif batting_team == 'Delhi Capitals':
            temp_arr = temp_arr + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_arr = temp_arr + [0,0,1,0,0,0,0,0]
            
        elif batting_team == 'Mumbai Indians':
            temp_arr = temp_arr + [0,0,0,1,0,0,0,0]
           
        elif batting_team == 'Kings XI Punjab':
            temp_arr = temp_arr + [0,0,0,0,1,0,0,0]
            
        elif batting_team == 'Rajasthan Royals':
            temp_arr = temp_arr + [0,0,0,0,0,1,0,0]
            
        elif batting_team == 'Royal Challengers Bangalore':
            temp_arr = temp_arr + [0,0,0,0,0,0,1,0]
           
        elif batting_team == 'Sunrisers Hyderabad':
            temp_arr = temp_arr + [0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_arr = temp_arr + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Capitals':
            temp_arr = temp_arr + [0,1,0,0,0,0,0,0]
            
        elif bowling_team == 'Kolkata Knight Riders':
            temp_arr = temp_arr + [0,0,1,0,0,0,0,0]
  
        elif bowling_team == 'Mumbai Indians':
            temp_arr = temp_arr + [0,0,0,1,0,0,0,0]
        
        elif bowling_team == 'Kings XI Punjab':
            temp_arr = temp_arr + [0,0,0,0,1,0,0,0]
           
        elif bowling_team == 'Rajasthan Royals':
            temp_arr = temp_arr + [0,0,0,0,0,1,0,0]
        
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_arr = temp_arr + [0,0,0,0,0,0,1,0]
         
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_arr = temp_arr + [0,0,0,0,0,0,0,1]
        data = np.array([temp_arr])
        t1 = cl.predict_proba(data)[0][0]
        t2= cl.predict_proba(data)[0][1]
        f=float(t1)
        p1=f*100
        ff=float(t2)
        p2=ff*100
        
    except:
        message = "Please enter valid Data"
        return render_template("chalja.html", message = message)
    return render_template('after.html', prediction = t1,prediction2=t2,bat=p1,bowl=p2)

        
@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    temp_array = list()
    try:
        if request.method == 'POST':
             toss=request.form['tosswon']
        k="Team1"
        if toss==k:
            temp_array=temp_array+[1]
        else:
            temp_array=temp_array+[2]
        elected=request.form['Elected1']
        if elected=='Bowl':
            temp_array=temp_array+[0]
        else:
            temp_array=temp_array+[1]

        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
            p=[1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Capitals':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
            p=[0,1,0,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
            p=[0,0,1,0,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
            p=[0,0,0,1,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
            p=[0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
            p=[0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
            p=[0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            p=[0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
            pp=[1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Capitals':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
            pp=[0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
            pp=[0,0,1,0,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
            pp=[0,0,0,1,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
            pp=[0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
            pp=[0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
            pp=[0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            pp=[0,0,0,0,0,0,0,1]
        data = np.array([temp_array])
        t1 = lgc.predict_proba(data)[0][1]
        t2= lgc.predict_proba(data)[0][0]
        f=float(t1)
        p1=f*100
        ff=float(t2)
        p2=ff*100
        
    except:
        message = "Please enter valid Data"
        return render_template("chalja.html", message = message)
    return render_template('after.html', prediction = t1,prediction2=t2,bat=p1,bowl=p2)

if __name__ == '__main__':
	app.run(debug=True)