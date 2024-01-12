from flask import Flask, redirect, url_for, render_template, request

app = Flask (__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    
    family_name = ""
    first_name = ""
    email = ""
    
    if request.method == "POST":
        
        family_name = request.form["family_name"]
        first_name = request.form["first_name"]
        email = request.form["email"]
        
        if not family_name or not first_name or not email:
            return render_template("petition.html")
        
        
        return render_template("confirm.html", family_name=family_name, first_name=first_name, email=email)
    
    return render_template("petition.html")




if __name__ == "__main__":
    app.run(debug=True)