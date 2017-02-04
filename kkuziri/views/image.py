import os, json
from flask import request, jsonify
from kkuziri import app
from werkzeug import secure_filename
from shortid import ShortId

@app.route('/image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            sid = ShortId()
            filename = sid.generate()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify(**{'success':True, 'image_url':'image.kkuziri.io/'+filename}), 200, {'ContentType':'application/json'}
    else:
        return jsonify(**{'success':False}), 405, {'ContentType':'application/json'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
