from flask import Flask, request, jsonify
import json


app = Flask(__name__)


with open('words_dictionary.json', 'r') as file:
    words = json.load(file)
    word_list = words.keys()

@app.route('/search-words', methods = ['POST'])
def search_words():
    try:
        letters = request.get_json()
        letters = letters.split()
        words = []
        results = []

        for word in word_list:
            if all(letter in letters for letter in word):
                words.append(word)

        for word in words:
            if len(word) >= 4 and len(word) <= 10:
                results.append(word)
        # Reset word list
        words.clear()
        words = results.copy()
        results.clear()

        primary = letters[-1]
        for word in words:
            if primary in word:
                results.append(word)

        return jsonify({"results": results})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)