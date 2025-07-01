# Rag-Attacks

A Python-based project for experimenting with Retrieval-Augmented Generation (RAG) and security-related tasks. This project includes a Flask web server, prompt management, user resources, and simple tool APIs for demonstration and testing.

## Features
- **Flask API server** with authentication
- **Prompt management** (dynamic prompt loading and greeting)
- **Simple tool APIs**: add and search
- **User resource endpoint**
- **Extensible structure** for adding more tools and prompts

## Project Structure
```
RAG TASK 1/
├── attack.py                # Attack logic
├── attack_runner.py         # Script to run attacks
├── context/                 # Context files (e.g., email1.txt)
├── models/                  # (Empty, for future model files)
├── openai.env               # OpenAI API key (excluded from git)
├── prompts/                 # Prompt templates (e.g., greet.json)
├── requirements.txt         # Python dependencies
├── resources/               # Resource files (e.g., users.json)
├── server.py                # Main Flask server
├── templates/               # HTML templates (e.g., index.html)
├── tool/                    # Tool modules (add.py, search.py)
└── .gitignore               # Git ignore rules
```

## API Endpoints

### Authentication
All API endpoints (except `/greet-form` and `/prompt/greet-site`) require an API key via the `X-API-KEY` header or `apikey` query parameter.

### Main Endpoints
- `GET /` — Health check
- `GET /greet-form` — HTML greeting form
- `GET /prompt/greet-site?name=YourName` — Render a greeting using a prompt template
- `GET /prompt/<prompt_name>` — Get a prompt template by name
- `POST /tool/search` — Search tool (expects `{ "query": "..." }`)
- `POST /tool/add` — Add tool (expects `{ "a": 1, "b": 2 }`)
- `GET /resource/users` — List users from `resources/users.json`

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshilkgp/Rag-Attacks.git
   cd "RAG TASK 1"
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Copy `openai.env.example` to `openai.env` and add your OpenAI API key.
4. **Run the server:**
   ```bash
   python server.py
   ```

## Example Usage
- Access the greeting form at `http://localhost:5000/greet-form`
- Use API tools with an API key:
  ```bash
  curl -X POST http://localhost:5000/tool/add -H "X-API-KEY: my-secret-key" -H "Content-Type: application/json" -d '{"a": 2, "b": 3}'
  ```

## License
This project is for educational and research purposes.

---
For more details, see the code and explore the endpoints! 