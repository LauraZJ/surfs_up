from flask import Flask
app = Flask (__name__)
@app.route('/')
def this_is_great():
    return 'This is great!'