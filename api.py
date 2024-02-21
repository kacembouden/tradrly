from flask import Flask, render_template, request, send_file
import analyse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload.html', message='No file part')

        file = request.files['file']

        # If the user does not select a file, browser also
        # submit an empty file without a filename
        if file.filename == '':
            return render_template('upload.html', message='No selected file')

        # Save the uploaded file to a specific directory (you can change this path)
        file_path = 'uploads/' + file.filename
        file.save(file_path)
        text = analyse.run(file_path)
        if text == None:
            text = "Can't find a text" 
        return render_template('upload.html', message='File uploaded successfully.  You will find the report in /results.txt' , file_path=file_path)

    return render_template('upload.html', message='Upload a file')


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug=True)
