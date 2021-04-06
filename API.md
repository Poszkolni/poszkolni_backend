# Contact
- Contact mail (POST) **AllowAny**
    - Example response:
    ```
    {
        "status": "string"
    }
    ```

# Users
- Users data (GET, PUT, DELETE) **Authenticated**
    - Example response:
    ```
    {
        "id": "int",
        "username": "string",
        "email": "string",
        "avatar": "string",
        "last_login": "datetime",
        "preferences": "string",
    }
    ```
- Login (POST) **AllowAny**
    - Example response:
    ```
    {
        "token": "JWT",
        "id": "int",
        "username": "string",
        "email": "string",
        "avatar": "string",
        "last_login": "datetime",
    }
    ```
- Register (POST) **AllowAny**
    - Example response:
    ```
    {
        "email": "string",
    }
    ```
- Change password (PUT) **Authenticated**
    - Example response:
    ```
    {
        "status": "string"
    }
    ```
- Reset password (PUT) **AllowAny**
    - Example response:
    ```
    {
        "email": "string",
        "status": "string"
    }
    ```
- Preferences (POST, PUT) **Authenticated**
    - Example response:
    ```
    {
        "preferences": "string",
        "status": "status"
    }
    ```

# Achievements
- Get info about achievements (GET) **Authenticated**
    - Example response:
    ```
    {
        "achievement_id": "string",
        "name": "string",
        "progress": "int",
        "total_progress": "int"
    }
    ```
- Update achievements progress (POST, PUT) **Authenticated**
    - Example response:
    ```
    {
        "achievement_id": "string",
        "name": "string",
        "progress": "int",
        "total_progress": "int"
    }
    ```
    
# Emotions
- Add daily emotions info (POST, PUT) **Authenticated**
- Get info about emotions history from range (GET) **Authenticated**

# Tasks
- Add, modify task (POST, PUT) **Authenticated**
- Get info abouts users tasks (GET) **Authenticated**
- Get daily tasks - first login of the day (GET) **Authenticated**

# JWT
- Refresh token (POST)
    - Example response:
    ```
    {
        "token": "JWT"
    }
    ```
