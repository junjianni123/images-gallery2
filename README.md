# Image Gallery - Full Stack Application

A modern image gallery application built with React frontend and Flask backend, featuring integration with the Unsplash API.

## 🏗️ Architecture

- **Frontend**: React.js with Bootstrap
- **Backend**: Flask (Python) with pipenv
- **Database**: None (stateless application)
- **External API**: Unsplash API for images
- **Deployment**: Docker & Docker Compose

## 🚀 Quick Start with Docker

### Prerequisites
- Docker and Docker Compose installed
- Unsplash API key

### 1. Environment Setup
Create `.env.local` in the `api` folder:
```bash
UNSPLASH_KEY=your_unsplash_access_key_here
DEBUG=True
FLASK_ENV=development
```

### 2. Run with Docker Compose
```bash
# Development mode
docker-compose up --build

# Production mode  
docker-compose -f docker-compose.prod.yml up --build
```

### 3. Access the Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- Health Check: http://localhost:5000/health

## 🛠️ Development Setup

### Backend (Flask API)
```bash
cd api
pipenv install
pipenv shell
python main.py
```

### Frontend (React)
```bash
cd frontend
npm install
npm start
```

## 📁 Project Structure
```
image-gallery1/
├── api/                    # Flask backend
│   ├── main.py            # Main Flask application
│   ├── Pipfile            # Python dependencies
│   ├── Dockerfile         # Development Docker config
│   ├── Dockerfile.prod    # Production Docker config
│   └── requirements.txt   # Alternative pip requirements
├── frontend/              # React frontend
│   ├── src/               # React source code
│   ├── public/            # Static assets
│   ├── package.json       # Node.js dependencies
│   ├── Dockerfile         # Development Docker config
│   └── Dockerfile.prod    # Production Docker config
├── docker-compose.yml     # Development orchestration
└── docker-compose.prod.yml # Production orchestration
```

## 🐳 Docker Commands

### Full Stack
```bash
# Development
docker-compose up --build
docker-compose down

# Production
docker-compose -f docker-compose.prod.yml up --build
docker-compose -f docker-compose.prod.yml down
```

### Individual Services
```bash
# Backend only
cd api
docker build -t image-gallery-api .
docker run -p 5000:5000 --env-file .env.local image-gallery-api

# Frontend only
cd frontend  
docker build -t image-gallery-frontend .
docker run -p 3000:3000 image-gallery-frontend
```

## 🔧 API Endpoints

- `GET /health` - Health check
- `GET /new-image?query=<search_term>` - Search images

## 🎨 Features

- ✅ Search images from Unsplash
- ✅ Responsive design with Bootstrap
- ✅ Delete images from gallery
- ✅ Real-time search
- ✅ Docker containerization
- ✅ Production-ready deployment

## 🚀 Deployment

### Production Deployment
The application includes production-ready Docker configurations:

- **Backend**: Uses Gunicorn WSGI server with multiple workers
- **Frontend**: Uses Nginx for serving static files and reverse proxy
- **Security**: Non-root users, health checks, optimized images

### Environment Variables
- `UNSPLASH_KEY`: Your Unsplash API access key
- `REACT_APP_API_URL`: Backend API URL (default: http://localhost:5000)
- `DEBUG`: Flask debug mode (True/False)
- `FLASK_ENV`: Flask environment (development/production)

## 📚 Getting Unsplash API Key

1. Go to [Unsplash Developers](https://unsplash.com/developers)
2. Create a new application
3. Copy the Access Key
4. Add it to your `.env.local` file

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
