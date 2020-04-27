from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

#this sign " < > " tells flask that what is inbetween is smth we pass on to the function underneath 
@app.route("/")  
def my_home(): 
    # it is not working anw idk why honestly 
    # print(url_for('static', filename='face.png'))
    return render_template("index.html")


#notice the dynamic shit we did in the next line insted of using a lot of lines we just compressed it into that 
@app.route("/<string:page_name>")
def html_page(page_name): 
    return render_template(page_name)

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\nemail: {email}, subje: {subject}, message: {message}')

def write_to_csv(data):
    with open("database.csv", "a", newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return "didn't save to database."
    else: 
        return "smth went wrong try again"


