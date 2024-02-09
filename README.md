# Files upload assignment

This is django web application that allow us to file upload in AWS s3 bucket.

# Prerequisites

- python >= 3.8
- pip 3

1. Clone the repository on your local machin with the commnd 

    ```
    git clone https://github.com/rohitPtechdev21/file_upload_task
   
   and checkout to master branch for the latest code
   
   git checkout master
   ```
   
2. Now move to the directory.

    ```
   cd file_upload_task
   ```
   
3. Create a virtual environment. If you don't have virtualenv installed, you can download it with the command:

    ```
   pip install virtualenv
   ```
   
4. Create a virtual environment with the following command:
    
    ```
    source <virtual environment name>/bin/activate
    ```
5. Install the app dependencies by running:
    
    ```
    pip install -r requirements.txt
   ```
6. Create a .env file in the backend directory using the command line:

    ```
   touch .env
   ```

7. Open the .env file and update it with the Postgres database credentials as follows:
    ```
    DATABASE_NAME=<postgres database name>
    DATABASE_USER=<postgres user name>
    DATABASE_PASSWORD=<postgres password>
    DATABASE_HOST=<host name for postgres>
    DATABASE_PORT=<postgres port>
    AWS_S3_BUCKET_NAME=<AWS s3 bucket name>
    AWS_CLIENT_ID=<AWS s3 access client id>
    AWS_SECRET_KEY=<AWS access secret key>
   ```
   
8. For apply migrations run following command:

    ```
   python manage.py migrate
   ```
   
9. You can now run the backend server by executing the following command:

    ```
   python manage.py runserver
   ```

10. Now you can visit the application with command:
    ```
    http://127.0.0.1:8000/
    ```