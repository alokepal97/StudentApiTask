## StudentApiTask
Student api from database

# Installation
Create virtual enviroment then install requirements.txt using pip command.

Create migration and migrate

Run  django server

## Usage

API urls

For student
* <p> List </p>
    
        ```
        /api/student/ 
        ```

        * <p> Response</p>
           
            ```
               [
                    {
                        "id": 6,
                        "first_name": "Aloke",
                        "last_name": "Pal",
                        "phone": "8116828315",
                        "username": "aloke97pal@gmail.com",
                        "email": "aloke97pal@gmail.com",
                        "password": "pbkdf2_sha256$216000$f475V2hK7Btn$gx5DIVvRmG5np7qCR1velkCGrFByhz5ieBVtvkpD/WA=",
                        "is_active": "True"
                    },
                    {
                        "id": 7,
                        "first_name": "demo",
                        "last_name": "demo",
                        "phone": "8116828315",
                        "username": "ram@gmail.com",
                        "email": "ram@gmail.com",
                        "password": "pbkdf2_sha256$216000$qEwR9uprs2sp$iIGTFH/jQZcBcnvhWqj/YBte3gkjZewJ6znN/vpp200=",
                        "is_active": "True"
                    },
                    {
                        "id": 8,
                        "first_name": "demo",
                        "last_name": "demo",
                        "phone": "8116828315",
                        "username": "demo@gmail.com",
                        "email": "demo@gmail.com",
                        "password": "pbkdf2_sha256$216000$gxFqGiqnywTb$e+PtIBlX+zGbSrWIbAARsgCVkIrQQPxOuD5oE0Gfi24=",
                        "is_active": "True"
                    }
                ]
                
            ```
    
    * Post
        + <p>Parameters</p>
        ``` 
            {
                "first_name": "demo",
                "last_name": "demo",
                "phone": "8116828315",
                "username": "demo@123",
                "email": "demo@123",
                "password": "demo@123",
            }
        ```
         ```
        /api/student/ 
        ```
        + <p> Response </p>

            ```
                {
                        "id": 8,
                        "first_name": "demo",
                        "last_name": "demo",
                        "phone": "8116828315",
                        "username": "demo@gmail.com",
                        "email": "demo@gmail.com",
                        "password": "pbkdf2_sha256$216000$gxFqGiqnywTb$e+PtIBlX+zGbSrWIbAARsgCVkIrQQPxOuD5oE0Gfi24=",
                        "is_active": "True"
                }
            ```
    * Get
        ```
        /api/student/:userid/
        ```
        * <p> Response</p>

            ```
                {   
                        "id": 8,
                        "first_name": "demo",
                        "last_name": "demo",
                        "phone": "8116828315",
                        "username": "demo@gmail.com",
                        "email": "demo@gmail.com",
                        "password": "pbkdf2_sha256$216000$gxFqGiqnywTb$e+PtIBlX+zGbSrWIbAARsgCVkIrQQPxOuD5oE0Gfi24=",
                        "is_active": "True"
                }
            ```
                

    * Put 
        ```
        /api/student/:userid/
        ```
        * <p> Parameters </p>
        ``` 
            {
                        "first_name": "demo",
                        "last_name": "demo",
                        "phone": "8116828315",
                        "username": "demo@gmail.com",
                        "email": "demo@gmail.com",
                        "password": "12345",
                        "is_active": "True"
            }
        ```
        * <p>Response</p>

            ```
                {
                        "id": 8,
                        "first_name": "demo",
                        "last_name": "demo",
                        "phone": "8116828315",
                        "username": "demo@gmail.com",
                        "email": "demo@gmail.com",
                        "password": "pbkdf2_sha256$216000$gxFqGiqnywTb$e+PtIBlX+zGbSrWIbAARsgCVkIrQQPxOuD5oE0Gfi24=",
                        "is_active": "True"
                }
            ```
    
* ## Login
    POST
    ```
     /api/authenticate/
    ```
    * <p>Parameter</p>

         ```
                {
                    "username" : "demo@gmail.com",
                    "password": "12345"
                }
        ```
    * Response 
        ```
            {
                "token": "895f3011f53bb8cfab3af0cc96ca96d345156b3f",
                "expires_in": "676.733317",
                "user_id": 8,
                "email": "demo@gmail.com"
            }
        ```

