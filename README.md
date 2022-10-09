# About the repository
This repository has been developed to boost development of microservices in [Python FastAPI Framework](https://fastapi.tiangolo.com/). You can
extend from it and do not worry about basic staffs like dockerizing app, make files, loggers and etc.

## TLDR
* Clone this repository to local machine
* Delete .git directory
* Setup needs for your project
* Create new repository on github
* Add your project to remote github repository

### Clone this repository to local machine
* [Create new token on github](https://github.com/settings/tokens)
* Copy the generated token
* Clone the repository by running command:
```
git clone https://{token}@github.com/laziest-coder/fastapi-service-blueprint.git
```

### Delete .git directory
* Run the following command:
```
rm -rf .git
```

### Setup needs for your project
* `cp .env.example .env` to create `.env` file.
* Fill in the app settings and credentials in the `.env` file.
* Replace `{port}` parts in `docker-compose.yml` file with your desired port number. Also, replace `{service_container_name}` to give correct name for project container.
* Update `requirements.txt` file in case you need some external libraries. But you can do this step later.
* In case you want some specific version of python, update it in section `FROM python:3.9` of `Dockerfile`
* Run `docker-compose up --build` to build project container
* Make sure everything is working as expected by making API request from your favorite REST Client([Insomnia](https://insomnia.rest/download) or [Postman](https://www.postman.com/))
to endpoint `http://localhost:{port}/v1/example-route?order_id=32123`

### Create new repository on github
* Head to your repositories page
* Create new repository on [this page](https://github.com/new)

### Add your project to remote github repository
* `git init` to start tracking your project.
* `git add . && git commit -m 'initial commit'` to make first commit to the project.
* `git remote add origin {link to your new github repository}`
* `git push --origin master` to push your local changes to remote repository.

### Final steps
That is all! Now you can start doing some magic with your project :)