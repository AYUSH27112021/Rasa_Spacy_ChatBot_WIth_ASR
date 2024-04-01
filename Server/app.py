from flask import Flask, request, send_from_directory ,Response
from flask_cors import CORS
import os
#import wave
import nemo.collections.asr as nemo_asr
import glob

app = Flask(__name__)

CORS(app)

# Create a directory to store the uploaded audio files.
UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

# Define a route to accept the AJAX request of the audio file.
@app.route('/upload', methods=['POST'])
def upload():
    
    # Get the uploaded audio file.
    # link to nemo model
    asr_model = nemo_asr.models.EncDecCTCModel.restore_from('/home/siva/Downloads/Model-te.nemo', strict=False)
    audio_file = request.files['audio_data']

    # Save the uploaded audio file to the uploads directory.
    path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    print(path)
    audio_file.save(os.path.join(UPLOAD_FOLDER, audio_file.filename))
    files = [path]
    transcript = asr_model.transcribe(paths2audio_files=files)[0]
    #transcript = "hello"
    print(f'Transcript: "{transcript}"')
    #path of upload folder to clear
    files = glob.glob('/home/siva/Desktop/rasaprojects/TE_final/abc/server/uploads/*')
    for f in files:
        os.remove(f)
        #print('file removed')
    # Return a success response.
    return Response(transcript, mimetype='text/plain')

# Define a route to serve the uploaded audio files.
@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
