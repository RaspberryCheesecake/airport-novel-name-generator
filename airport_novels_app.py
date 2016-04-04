from flask import Flask
from airport_novel_titles_generator import airport_novel_generator

app = Flask(__name__)


@app.route('/airport_novels')
def an():
    return airport_novel_generator()

if __name__ == '__main__':
    app.run()
