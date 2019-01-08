# Instructions copied from - https://hub.docker.com/_/python/
FROM python:3-onbuild

# tell the port number the container should expose
EXPOSE 8000

# run the command
#CMD ["chmod", "u+x", "gunicorn.sh"]
CMD ["pip", "install", "-r", "requirements.txt"]
CMD ["sh", "gunicorn.sh"]
#CMD ["python", "./api.py"]
