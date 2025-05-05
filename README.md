# Notepad Application

A full-stack notepad application featuring user authentication and sentiment analysis, built with React (frontend) and FastAPI (backend).

## Features

-   **User Authentication**: Secure user login and registration using JWT tokens.
-   **CRUD Operations**: Full Create, Read, Update, and Delete functionality for notes.
-   **Sentiment Analysis**: Automatic analysis of note content to determine positive, neutral, or negative sentiment.
-   **Responsive Design**: User interface adapts to various screen sizes.
-   **Data Validation**: Robust input sanitization and validation to ensure data integrity.
-   **Persistent Storage**: Utilizes an SQLite database for persistent storage of application data.

## Technologies Used

### Frontend

-   [React.js](https://react.dev/)
-   [Axios](https://axios-http.com/docs/intro) for making HTTP requests.
-   [React Router](https://reactrouter.com/en/main) (if implemented) for navigation.
-   CSS for styling.

### Backend

-   [Python FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance), web framework for building APIs.
-   [SQLAlchemy](https://www.sqlalchemy.org/) - A powerful Python SQL toolkit and Object-Relational Mapper.
-   [SQLite](https://www.sqlite.org/index.html) - A lightweight, disk-based database.
-   [PyJWT](https://pyjwt.readthedocs.io/en/stable/) for JSON Web Token implementation.
-   [TextBlob](https://textblob.readthedocs.io/en/dev/) - A Python library for processing textual data, used here for sentiment analysis.

## Prerequisites

Before getting started, ensure you have the following installed on your system:

-   [Docker](https://www.docker.com/get-started/) and [Docker Compose](https://docs.docker.com/compose/install/)
-   [Node.js](https://nodejs.org/) (version 18 or higher is recommended) for frontend development.
-   [Python](https://www.python.org/downloads/) (version 3.9 or higher) for backend development.

## Installation

There are two primary ways to install and run the Notepad Application: using Docker (recommended for ease of setup) or manual installation.

### Using Docker (Recommended)

This method sets up the entire application stack (frontend, backend, and database) using Docker containers.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/notepad-app.git](https://github.com/yourusername/notepad-app.git)
    cd notepad-app
    ```

2.  **Build and start all services:**
    ```bash
    docker-compose up --build
    ```
    This command will perform the following actions:
    -   Build the Docker images for both the frontend and backend based on their respective `Dockerfile`.
    -   Start all the containers defined in the `docker-compose.yml` file.
    -   Mount the project code as volumes into the containers, enabling hot-reloading during development (changes in your code will be reflected automatically within the running containers).

3.  **Access the application:**
    -   **Frontend**: Open your web browser and navigate to `http://localhost:3000`.
    -   **Backend API**: The backend API is accessible at `http://localhost:8000`.
    -   **API Documentation (Swagger UI)**: Explore the backend API endpoints using Swagger UI at `http://localhost:8000/docs`.

#### Optional Docker Commands:

-   **Run in detached mode (background):**
    ```bash
    docker-compose up --build -d
    ```

-   **Stop all services:**
    ```bash
    docker-compose down
    ```

-   **View logs:**
    ```bash
    docker-compose logs -f # Follow logs in real-time
    ```

#### Key Notes for Docker Setup:

-   The first time you run `docker-compose up --build`, it will take a few minutes as Docker needs to:
    -   Install the Python dependencies for the backend.
    -   Build the production-ready React frontend.
    -   Initialize the SQLite database (`notes.db`).
-   **Hot-reloading:**
    -   **Frontend**: Changes made to the React code in the `notepad-frontend` directory will automatically refresh in your browser, thanks to the `npm start` command running within the frontend container.
    -   **Backend**: The FastAPI backend is configured to automatically reload upon file changes due to the `--reload` flag used with `uvicorn`.
-   **Database Persistence:** The SQLite database file (`notes.db`) is stored in the `./backend` directory on your host machine. This ensures that your notes and user data persist even after the Docker containers are stopped and restarted.
-   **Troubleshooting:**
    -   If you encounter issues with ports already being in use (e.g., port 3000 or 8000), you can either stop the conflicting services running on your machine or modify the port mappings in the `docker-compose.yml` file.
    -   If you experience build cache issues during the Docker image creation process, you can try running `docker system prune` to remove unused Docker data, including build cache.

### Manual Installation

This method involves setting up the frontend and backend environments separately on your local machine.

#### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```
    The backend server will start at `http://localhost:8000`.

#### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd notepad-frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Start the development server:**
    ```bash
    npm start
    ```
    The frontend application will typically start at `http://localhost:3000`.

## API Endpoints

The backend API provides the following endpoints for interacting with the application:

-   `POST /token`: Authenticates a user and returns a JWT access token.
-   `POST /users/`: Creates a new user account.
-   `GET /users/me/`: Retrieves the details of the currently authenticated user.
-   `GET /notes/`: Retrieves all notes belonging to the currently authenticated user.
-   `POST /notes/`: Creates a new note.
-   `PUT /notes/{note_id}`: Updates an existing note with the specified ID.
-   `DELETE /notes/{note_id}`: Deletes the note with the specified ID.

You can explore these endpoints in more detail using the Swagger UI available at `http://localhost:8000/docs` when the backend server is running.

## Configuration

### Backend Environment Variables

You can configure the backend application using environment variables. It is recommended to create a `.env` file in the `backend` directory and define the following variables:

dotenv
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30```
DATABASE_URL=sqlite:///./notes.db
SECRET_KEY: A secret key used for signing JWT tokens. Ensure this is a strong, unique value in a production environment.
ALGORITHM: The algorithm used for JWT encoding and decoding (default is HS256).
ACCESS_TOKEN_EXPIRE_MINUTES: The lifespan of the access tokens in minutes.
DATABASE_URL: The SQLAlchemy database connection URL. The default is set to a local SQLite database file.

Markdown

# Notepad Application

A full-stack notepad application featuring user authentication and sentiment analysis, built with React (frontend) and FastAPI (backend).

## Features

-   **User Authentication**: Secure user login and registration using JWT tokens.
-   **CRUD Operations**: Full Create, Read, Update, and Delete functionality for notes.
-   **Sentiment Analysis**: Automatic analysis of note content to determine positive, neutral, or negative sentiment.
-   **Responsive Design**: User interface adapts to various screen sizes.
-   **Data Validation**: Robust input sanitization and validation to ensure data integrity.
-   **Persistent Storage**: Utilizes an SQLite database for persistent storage of application data.

## Technologies Used

### Frontend

-   [React.js](https://react.dev/)
-   [Axios](https://axios-http.com/docs/intro) for making HTTP requests.
-   [React Router](https://reactrouter.com/en/main) (if implemented) for navigation.
-   CSS for styling.

### Backend

-   [Python FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance), web framework for building APIs.
-   [SQLAlchemy](https://www.sqlalchemy.org/) - A powerful Python SQL toolkit and Object-Relational Mapper.
-   [SQLite](https://www.sqlite.org/index.html) - A lightweight, disk-based database.
-   [PyJWT](https://pyjwt.readthedocs.io/en/stable/) for JSON Web Token implementation.
-   [TextBlob](https://textblob.readthedocs.io/en/dev/) - A Python library for processing textual data, used here for sentiment analysis.

## Prerequisites

Before getting started, ensure you have the following installed on your system:

-   [Docker](https://www.docker.com/get-started/) and [Docker Compose](https://docs.docker.com/compose/install/)
-   [Node.js](https://nodejs.org/) (version 18 or higher is recommended) for frontend development.
-   [Python](https://www.python.org/downloads/) (version 3.9 or higher) for backend development.

## Installation

There are two primary ways to install and run the Notepad Application: using Docker (recommended for ease of setup) or manual installation.

### Using Docker (Recommended)

This method sets up the entire application stack (frontend, backend, and database) using Docker containers.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/notepad-app.git](https://github.com/yourusername/notepad-app.git)
    cd notepad-app
    ```

2.  **Build and start all services:**
    ```bash
    docker-compose up --build
    ```
    This command will perform the following actions:
    -   Build the Docker images for both the frontend and backend based on their respective `Dockerfile`.
    -   Start all the containers defined in the `docker-compose.yml` file.
    -   Mount the project code as volumes into the containers, enabling hot-reloading during development (changes in your code will be reflected automatically within the running containers).

3.  **Access the application:**
    -   **Frontend**: Open your web browser and navigate to `http://localhost:3000`.
    -   **Backend API**: The backend API is accessible at `http://localhost:8000`.
    -   **API Documentation (Swagger UI)**: Explore the backend API endpoints using Swagger UI at `http://localhost:8000/docs`.

#### Optional Docker Commands:

-   **Run in detached mode (background):**
    ```bash
    docker-compose up --build -d
    ```

-   **Stop all services:**
    ```bash
    docker-compose down
    ```

-   **View logs:**
    ```bash
    docker-compose logs -f # Follow logs in real-time
    ```

#### Key Notes for Docker Setup:

-   The first time you run `docker-compose up --build`, it will take a few minutes as Docker needs to:
    -   Install the Python dependencies for the backend.
    -   Build the production-ready React frontend.
    -   Initialize the SQLite database (`notes.db`).
-   **Hot-reloading:**
    -   **Frontend**: Changes made to the React code in the `notepad-frontend` directory will automatically refresh in your browser, thanks to the `npm start` command running within the frontend container.
    -   **Backend**: The FastAPI backend is configured to automatically reload upon file changes due to the `--reload` flag used with `uvicorn`.
-   **Database Persistence:** The SQLite database file (`notes.db`) is stored in the `./backend` directory on your host machine. This ensures that your notes and user data persist even after the Docker containers are stopped and restarted.
-   **Troubleshooting:**
    -   If you encounter issues with ports already being in use (e.g., port 3000 or 8000), you can either stop the conflicting services running on your machine or modify the port mappings in the `docker-compose.yml` file.
    -   If you experience build cache issues during the Docker image creation process, you can try running `docker system prune` to remove unused Docker data, including build cache.

### Manual Installation

This method involves setting up the frontend and backend environments separately on your local machine.

#### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```
    The backend server will start at `http://localhost:8000`.

#### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd notepad-frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Start the development server:**
    ```bash
    npm start
    ```
    The frontend application will typically start at `http://localhost:3000`.

## API Endpoints

The backend API provides the following endpoints for interacting with the application:

-   `POST /token`: Authenticates a user and returns a JWT access token.
-   `POST /users/`: Creates a new user account.
-   `GET /users/me/`: Retrieves the details of the currently authenticated user.
-   `GET /notes/`: Retrieves all notes belonging to the currently authenticated user.
-   `POST /notes/`: Creates a new note.
-   `PUT /notes/{note_id}`: Updates an existing note with the specified ID.
-   `DELETE /notes/{note_id}`: Deletes the note with the specified ID.

You can explore these endpoints in more detail using the Swagger UI available at `http://localhost:8000/docs` when the backend server is running.

## Configuration

### Backend Environment Variables

You can configure the backend application using environment variables. It is recommended to create a `.env` file in the `backend` directory and define the following variables:

```dotenv
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./notes.db
```
SECRET_KEY: A secret key used for signing JWT tokens. Ensure this is a strong, unique value in a production environment.
ALGORITHM: The algorithm used for JWT encoding and decoding (default is HS256).
ACCESS_TOKEN_EXPIRE_MINUTES: The lifespan of the access tokens in minutes.
DATABASE_URL: The SQLAlchemy database connection URL. The default is set to a local SQLite database file.
Testing
The application includes automated tests to ensure code quality and functionality. GitHub Actions are configured for Continuous Integration/Continuous Deployment (CI/CD), automatically running tests on push and pull requests to the main branch.

Running Tests Locally
Backend Tests
```bash
pytest
```

Deployment
The application is designed to be easily deployed using Docker. The included GitHub Actions workflow (.github/workflows/CICD.yml) provides a basic CI/CD pipeline that includes automated testing. You can extend this workflow to include deployment steps for your preferred hosting provider (e.g., AWS, Google Cloud, Heroku).

Usage
Register or Log In:

You can register a new user account through the frontend.
Alternatively, you can use the default test credentials (auto-created on the first Docker run):/n
Username: testuser
Password: testpass
Create, Edit, and Delete Notes: Once logged in, you can create new notes, edit their content, and delete them.

View Sentiment Analysis: As you create or edit notes, the application automatically analyzes the text content and displays the sentiment (Positive, Neutral, or Negative) for each note.

Project Structure
notepad-app/
├── backend/                     # FastAPI backend
│   ├── auth.py                  # Authentication logic
│   ├── crud.py                  # Database operations
│   ├── database.py              # Database configuration
│   ├── Dockerfile               # Backend Docker configuration
│   ├── main.py                  # FastAPI application entry point
│   ├── models.py                # SQLAlchemy database models
│   ├── nlpmodel.py              # Sentiment analysis functionality
│   ├── requirements.txt         # Python dependencies
│   └── schemas.py               # Pydantic data validation schemas
├── notepad-frontend/            # React frontend
│   ├── public/
│   ├── src/
│   │   ├── api.js               # Configuration for API calls
│   │   ├── App.js               # Main application component
│   │   ├── components/          # Reusable React UI components
│   │   └── styles/              # CSS stylesheets
│   ├── Dockerfile               # Frontend Docker configuration
│   └── package.json             # Frontend dependencies and scripts
├── docker-compose.yml           # Docker Compose configuration for multi-container setup
└── .github/workflows/          # GitHub Actions workflows
    └── CICD.yml                 # CI/CD pipeline definition

