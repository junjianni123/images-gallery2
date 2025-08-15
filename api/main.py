import os

# from flask_cors import CORS
import requests
import urllib3
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

# from mongo_client import insert_test_document

# Disable SSL warnings for development (when verify=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables
load_dotenv(dotenv_path="./.env.local")

# os.environ['FLASK_ENV'] = 'development'
print(os.environ.get("UNSPLASH_KEY", ""))

UNSPLASH_URL = "https://api.unsplash.com/search/photos"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
    raise EnvironmentError(
        "Please create .env.local file and insert there UNSPLASH_KEY"
    )

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get Unsplash API key from environment
# UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')
app.config["DEBUG"] = DEBUG

# insert_test_document()  # Insert a test document into MongoDB

@app.route("/new-image")
def new_image():
    word = request.args.get("query")
    headers = {"Accept-Version": "v1", "Authorization": f"Client-ID {UNSPLASH_KEY}"}
    params = {"query": word}
    
    try:
        # Add timeout and SSL verification settings for Docker compatibility
        response = requests.get(
            url=UNSPLASH_URL, 
            headers=headers, 
            params=params,
            timeout=30,
            verify=False  # Disable SSL verification for Docker development
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data
    except requests.exceptions.SSLError as e:
        print(f"SSL Error: {e}")
        return jsonify({"error": "SSL connection failed. Please check network configuration."}), 500
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timeout. Please try again."}), 504
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return jsonify({"error": "Failed to fetch images from Unsplash API."}), 500
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500


@app.route("/health")
def health_check():
    """Health check endpoint for Docker and monitoring"""
    return jsonify({
        "status": "healthy",
        "timestamp": "2025-07-09",
        "service": "image-gallery-api"
    })


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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
