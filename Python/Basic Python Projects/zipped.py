from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Calculator API</h1>
    <p>Use /add?num1=5&num2=3</p>
    <p>Use /health for health checks</p>
    """

@app.route('/add')
def add_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        result = num1 + num2
        return jsonify({
            "operation": "addition",
            "num1": num1,
            "num2": num2, 
            "result": result
        })
    except ValueError:
        return jsonify({"error": "Please provide valid numbers"}), 400

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "service": "calculator"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)