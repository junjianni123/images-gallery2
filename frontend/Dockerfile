# Development Dockerfile for React Frontend
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install dependencies first (for better caching)
COPY package*.json ./
RUN npm install --silent

# Copy source code
COPY . .

# Expose port
EXPOSE 3000

# Set environment variables
ENV REACT_APP_API_URL=http://localhost:5000

# Start development server
CMD ["npm", "start"]
