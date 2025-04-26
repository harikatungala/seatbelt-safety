
from flask import Flask, render_template_string, redirect, url_for, request

app = Flask(_name_)

# Initialize seatbelt status
seatbelt_worn = True

# HTML template
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Seatbelt Detector</title>
    <style>
        body { text-align: center; font-family: Arial, sans-serif; margin-top: 50px; }
        h1 { font-size: 36px; }
        p { font-size: 24px; }
        .safe { color: green; font-weight: bold; }
        .warning { color: red; font-weight: bold; }
        .buttons { margin-top: 30px; }
        button { font-size: 18px; padding: 10px 20px; margin: 10px; }
    </style>
</head>
<body>
    <h1>Seatbelt Detector</h1>
    <p class="{{ status_class }}">{{ status_message }}</p>
    
    <div class="buttons">
        <form action="/toggle" method="post" style="display:inline;">
            <button type="submit">Toggle Status</button>
        </form>
        <form action="/force_safe" method="post" style="display:inline;">
            <button type="submit">Force Safe</button>
        </form>
        <form action="/force_warning" method="post" style="display:inline;">
            <button type="submit">Force Warning</button>
        </form>
        <form action="/reset" method="post" style="display:inline;">
            <button type="submit">Reset</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    global seatbelt_worn
    if seatbelt_worn:
        status_message = "✅ Seatbelt Detected. Safe to drive!"
        status_class = "safe"
    else:
        status_message = "❗ No Seatbelt Detected! Please wear it."
        status_class = "warning"
    return render_template_string(html_template, status_message=status_message, status_class=status_class)

# Toggle seatbelt status
@app.route('/toggle', methods=['POST'])
def toggle():
    global seatbelt_worn
    seatbelt_worn = not seatbelt_worn
    return redirect(url_for('home'))

# Force safe (seatbelt worn)
@app.route('/force_safe', methods=['POST'])
def force_safe():
    global seatbelt_worn
    seatbelt_worn = True
    return redirect(url_for('home'))

# Force warning (seatbelt not worn)
@app.route('/force_warning', methods=['POST'])
def force_warning():
    global seatbelt_worn
    seatbelt_worn = False
    return redirect(url_for('home'))

# Reset (set to default - seatbelt worn)
@app.route('/reset', methods=['POST'])
def reset():
    global seatbelt_worn
    seatbelt_worn = True
    return redirect(url_for('home'))

# Run the app
if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8000)
