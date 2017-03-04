import os, json
from flask import request, jsonify
from kkuziri import app
from kkuziri import s3_client
from werkzeug import secure_filename
from shortid import ShortId

@app.route('/image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            _, ext = os.path.splitext(file.filename)
            filename = ShortId().generate() + ext
            s3_client.upload_fileobj(file, app.config['AWS_S3_BUCKET_NAME'],
                     filename)
            return jsonify(**{'success':True,
                'image_url':app.config['AWS_S3_BASE_URL'] + filename})\
                        , 200, {'ContentType':'application/json'}
    else:
        return jsonify(**{'success':False}), 405,\
            {'ContentType':'application/json'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
