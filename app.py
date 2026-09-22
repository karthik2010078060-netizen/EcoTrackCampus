from flask import Flask, render_template, request

app = Flask(_name_)

# Global baseline dashboard metrics
dashboard_data = {
    "wastage": 14.2,
    "drives": 8,
    "avoidance": 92
}

@app.route('/')
def home():
    return render_template('index.html', 
                           wastage=dashboard_data["wastage"], 
                           drives=dashboard_data["drives"], 
                           avoidance=dashboard_data["avoidance"])

@app.route('/update', methods=['POST'])
def update_data():
    if request.method == 'POST':
        dashboard_data["wastage"] = float(request.form['wastage'])
        dashboard_data["drives"] = int(request.form['drives'])
        dashboard_data["avoidance"] = int(request.form['avoidance'])
    
    return render_template('index.html', 
                           wastage=dashboard_data["wastage"], 
                           drives=dashboard_data["drives"], 
                           avoidance=dashboard_data["avoidance"])

if _name_ == '_main_':
    app.run(debug=True)