# SinglePageBlog

A blog writing platform written in DjangoRestFramework and React.

## Run Locally

#### Note: Make .env file and add configurations according to .env.example

- with Docker (recommended)
- without Docker (not recommended)

Clone the project

```bash
  git clone https://github.com/Neeraj319/SinglePageBlog
```

#### With Docker

Go to the project directory

```bash
cd SinglePageBlog
```

```
sudo docker-compose up --build
```

#### NOTE: make sure to comment out line no 4 and 6 in entrypoint.sh after building the image  



##### Visit http://localhost:8000/docs for the documentation of the API
##### Visit http://localhost:3000 for the frontend