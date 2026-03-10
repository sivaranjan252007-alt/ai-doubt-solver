from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")

    answer = """
AVL Tree is a self-balancing Binary Search Tree (BST).
The difference between heights of left and right subtree
cannot be more than 1.

Balance Factor = Height(left subtree) - Height(right subtree)

If imbalance occurs, AVL tree performs rotations:
1. Left Rotation
2. Right Rotation
3. Left-Right Rotation
4. Right-Left Rotation

Operations like search, insert and delete take O(log n) time.
"""

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)