from flask import Flask, request, jsonify nano app.py app = Flask(__name__)

def convert_to_helvetica(text):
    conversion_map = {
        "A": "𝐀", "B": "𝐁", "C": "𝐂", "D": "𝐃", "E": "𝐄", "F": "𝐅", "G": "𝐆", "H": "𝐇", "I": "𝐈", "J": "𝐉", 
        "K": "𝐊", "L": "𝐋", "M": "𝐌", "N": "𝐍", "O": "𝐎", "P": "𝐏", "Q": "𝐐", "R": "𝐑", "S": "𝐒", "T": "𝐓", 
        "U": "𝐔", "V": "𝐕", "W": "𝐖", "X": "𝐗", "Y": "𝐘", "Z": "𝐙", "a": "𝐚", "b": "𝐛", "c": "𝐜", "d": "𝐝", 
        "e": "𝐞", "f": "𝐟", "g": "𝐠", "h": "𝐡", "i": "𝐢", "j": "𝐣", "k": "𝐤", "l": "𝐥", "m": "𝐦", "n": "𝐧", 
        "o": "𝐨", "p": "𝐩", "q": "𝐪", "r": "𝐫", "s": "𝐬", "t": "𝐭", "u": "𝐮", "v": "𝐯", "w": "𝐰", "x": "𝐱", 
        "y": "𝐲", "z": "𝐳", "0": "𝟎", "1": "𝟏", "2": "𝟐", "3": "𝟑", "4": "𝟒", "5": "𝟓", "6": "𝟔", "7": "𝟕", 
        "8": "𝟖", "9": "𝟗"

    }
    return ''.join(conversion_map.get(c, c) for c in text)

@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json()
    input_text = data.get("text", "")
    helvetica_text = convert_to_helvetica(input_text)
    return jsonify({"converted_text": helvetica_text})

if __name__ == "__main__":
    app.run(debug=True)

