from flask import Flask, request, jsonify
# from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv(dotenv_path="./.env.local")

# os.environ['FLASK_ENV'] = 'development'
print(os.environ.get("UNSPLASH_KEY", ""))

UNSPLASH_URL = "https://api.unsplash.com/search/photos"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
  raise EnvironmentError("Please create .env.local file and insert there UNSPLASH_KEY")

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get Unsplash API key from environment
# UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')
app.config["DEBUG"] = DEBUG

@app.route('/new-image')
def new_image():
    word = request.args.get("query")
    headers = {
        "Accept-Version": "v1",
        "Authorization": f"Client-ID {UNSPLASH_KEY}"
    }
    params = {"query": word}
    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
    data = (response.json())
    return data
    # headers = {
    #   "Accept-Version": "v1",
    #   "Authorization": "Client-ID " + UNSPLASH_KEY
    # }
    # params = {"query": word}
    # response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
    
    # data = response.json()
    # return data

# @app.route('/api/images/search', methods=['GET'])
# def search_images():
#     """Search for images using Unsplash API"""
#     try:
#         query = request.args.get('query', '')
#         per_page = request.args.get('per_page', 12)
#         page = request.args.get('page', 1)
        
#         if not query:
#             return jsonify({"error": "Query parameter is required"}), 400
            
#         if not UNSPLASH_ACCESS_KEY:
#             return jsonify({"error": "Unsplash API key not configured"}), 500
        
#         # Make request to Unsplash API
#         url = "https://api.unsplash.com/search/photos"
#         headers = {
#             "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
#         }
#         params = {
#             "query": query,
#             "per_page": per_page,
#             "page": page
#         }
        
#         response = requests.get(url, headers=headers, params=params)
        
#         if response.status_code == 200:
#             data = response.json()
#             return jsonify({
#                 "success": True,
#                 "data": data,
#                 "total": data.get('total', 0),
#                 "total_pages": data.get('total_pages', 0)
#             })
#         else:
#             return jsonify({
#                 "error": "Failed to fetch images from Unsplash",
#                 "status_code": response.status_code
#             }), response.status_code
            
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/api/images/random', methods=['GET'])
# def get_random_image():
#     """Get a random image using Unsplash API"""
#     try:
#         query = request.args.get('query', '')
        
#         if not UNSPLASH_ACCESS_KEY:
#             return jsonify({"error": "Unsplash API key not configured"}), 500
        
#         # Make request to Unsplash API
#         url = "https://api.unsplash.com/photos/random"
#         headers = {
#             "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
#         }
#         params = {}
#         if query:
#             params["query"] = query
        
#         response = requests.get(url, headers=headers, params=params)
        
#         if response.status_code == 200:
#             data = response.json()
#             return jsonify({
#                 "success": True,
#                 "data": data
#             })
#         else:
#             return jsonify({
#                 "error": "Failed to fetch random image from Unsplash",
#                 "status_code": response.status_code
#             }), response.status_code
            
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/health', methods=['GET'])
# def health_check():
#     """Health check endpoint"""
#     return jsonify({
#         "status": "healthy",
#         "timestamp": "2025-06-14"
#     })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

