# HNG12 Stage 0 Public API

## Description  

This is a simple Django-based public API for the HNG12 Stage 0 task.

## Endpoint  

- **GET /** - Returns JSON with email, current date-time, and GitHub repo.

## Example Response

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

## Setup

1. Clone the repository
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Install dependencies

   ```sh
   pip install -r requirements.txt
   ```

3. Run the development server

   ```sh
   python manage.py runserver
   ```

4. Access at `http://127.0.0.1:8000/`

## Deployment

This API is deployed at:
```
https://your-deployment-url.com/
```

## Learn More

[Hire Python Developers](https://hng.tech/hire/python-developers)
