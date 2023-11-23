import os
from model import style_transfer_image
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/output', methods=['POST', 'GET'])
def output():
    if request.method == 'POST':
        file = request.files['content']
        print('reached here')
        filePath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filePath)

        style_transfer_image(
            filePath, "data/cubism/train/0aou4tal.jpg", save_name="blend-wave", epochs=1,
            style_weight=1e-2, content_weight=1e4, total_variation_weight=30,
        )

    return render_template("output.html")

app.run(debug=True, port=3000)