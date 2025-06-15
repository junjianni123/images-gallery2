# Image Gallery API

A Flask-based backend API for the Image Gallery application that interfaces with the Unsplash API.

## Features

- Search for images using Unsplash API
- Get random images
- CORS enabled for frontend integration
- Environment variable configuration
- Health check endpoint

## Setup

### Option 1: Using pipenv (Recommended)

1. **Install pipenv** (if not already installed):
   ```bash
   pip install pipenv
   ```

2. **Create virtual environment and install dependencies:**
   ```bash
   pipenv install
   ```

3. **Environment Configuration:**
   - Copy `.env.example` to `.env`
   - Add your Unsplash API key to the `.env` file
   ```
   UNSPLASH_ACCESS_KEY=your_actual_api_key_here
   ```

4. **Get Unsplash API Key:**
   - Go to [Unsplash Developers](https://unsplash.com/developers)
   - Create a new application
   - Copy the Access Key

5. **Run the server:**
   ```bash
   pipenv run python main.py
   ```

### Option 2: Using pip and requirements.txt

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Configuration:**
   - Copy `.env.example` to `.env`
   - Add your Unsplash API key to the `.env` file
   ```
   UNSPLASH_ACCESS_KEY=your_actual_api_key_here
   ```

3. **Get Unsplash API Key:**
   - Go to [Unsplash Developers](https://unsplash.com/developers)
   - Create a new application
   - Copy the Access Key

4. **Run the server:**
   ```bash
   python main.py
   ```

The API will be available at `http://localhost:5000`

## API Endpoints

### GET /
- **Description:** API information
- **Response:** Basic API information and status

### GET /api/images/search
- **Description:** Search for images
- **Parameters:**
  - `query` (required): Search term
  - `per_page` (optional): Number of results per page (default: 12)
  - `page` (optional): Page number (default: 1)
- **Example:** `/api/images/search?query=nature&per_page=10&page=1`

### GET /api/images/random
- **Description:** Get a random image
- **Parameters:**
  - `query` (optional): Search term for random image
- **Example:** `/api/images/random?query=landscape`

### GET /health
- **Description:** Health check endpoint
- **Response:** API health status

## Usage with Frontend

The frontend can now use this backend instead of directly calling the Unsplash API:

```javascript
// Instead of calling Unsplash directly
fetch(`https://api.unsplash.com/photos/random/?query=${word}&client_id=${UNSPLASH_KEY}`)

// Call your backend API
fetch(`http://localhost:5000/api/images/random?query=${word}`)
```

## Development

- The server runs in debug mode by default
- CORS is enabled for all origins
- Environment variables are loaded from `.env` file
