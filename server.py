from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify,abort,render_template,send_from_directory
from tool.add import add as add_tool
from tool.search import search as search_tool
import json

load_dotenv(dotenv_path="openai.env")  # Load from your .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Now accessible

app = Flask(__name__)

PROMPT_DIR="prompts"
# 🔐 AUTHENTICATION BLOCK
API_KEY = os.getenv("MCP_API_KEY", "my-secret-key")

@app.before_request
def authenticate():
    # Skip authentication for frontend routes
    if request.path in ['/greet-form', '/prompt/greet-site']:
        return  # Allow without API key

    key = request.headers.get("X-API-KEY") or request.args.get("apikey")
    if key != API_KEY:
        abort(401, "Unauthorized")

@app.route('/tool/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({"error": "Missing 'query'"}), 400
    result = search_tool(query)
    return jsonify({"result": result})

@app.route('/')
def home():
    return "✅ MCP Server is running!"

@app.route('/greet-form')
def greet_form():
    return render_template('index.html')

@app.route('/prompt/greet-site')
def greet_site():
    name = request.args.get('name', 'Guest')
    with open('prompts/greet.json') as f:
        template = json.load(f)
        message = template["prompt"].format(name=name)
        return f"<h2>{message}</h2>"


@app.route('/tool/add', methods=['POST'])
def add():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({"error": "Missing 'a' or 'b' in request"}), 400
    result = add_tool(a, b)
    return jsonify({"result": result})

@app.route('/resource/users', methods=['GET'])
def users():
    with open('resources/users.json') as f:
        return jsonify(json.load(f))

# ✅ ✅ ✅ Add this new route below your existing ones:
@app.route('/prompt/<prompt_name>', methods=['GET'])
def get_prompt(prompt_name):
    filename = f"{prompt_name}.json"
    filepath = os.path.join(PROMPT_DIR, filename)
    
    if os.path.exists(filepath):
        with open(filepath) as f:
            return f.read()
    else:
        return jsonify({"error": f"Prompt '{prompt_name}' not found."}), 404



if __name__ == '__main__':
    app.run(debug=True)
    
