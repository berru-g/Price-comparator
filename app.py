from flask import Flask, request, jsonify
from scrap_amazon import my_function
app = Flask(__name__)

@app.route('/api/search', methods=['POST'])
def search():
    query = request.json['query']
    result = my_function(query)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
