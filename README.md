### Information

This is a resource prioritizing app. It uses users **weight** to select an user request.

- Features:
    ```
    1. Implemented by Django and Django-Rest-Framework
    2. Uses python random library to randomly choose user with weight consideration
    ```

- Usage Info:
    ```
    1. First start webserver by: python manage.py runserver
    2. Send POST request to http://127.0.0.1:8000/v1/res/calculate/ endpoint. Your request should has user_id key.
        user_id for this demo must have one of this values: user1, user2, ... user5
    3. One of users will be selected. user with more weight has more chance to selected. You can check logic in views.py file.
    ```

- Video Demonstration:
    * [Download](https://m-gh.info/danaxa.mp4)
