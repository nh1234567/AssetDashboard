from flask import Flask, request, render_template, jsonify, redirect, url_for

app = Flask(__name__)

counter = 0  # To keep track of the 'Normal' state count

@app.route('/')
def index():
  return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"Received username: {username}, password: {password}")  # Debugging line
    if username == "AAA" and password == "xyz":
      return redirect(url_for('dashboard'))
    return jsonify({"status": "failed", "message": "Invalid credentials"}), 401
  return render_template('login.html')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')


@app.route('/asset_state', methods=['GET'])
def asset_state():
  global counter
  counter += 1

  if counter % 4 == 0:  # Anomaly will occur every 4th request
    return jsonify({"state": "Anomaly", "color": "red"})
  return jsonify({"state": f"Normal {counter}", "color": "green"})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
