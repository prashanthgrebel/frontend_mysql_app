# start by pulling the python image
FROM python:3.8-alpine

# Install Flask
RUN pip3 install flask
RUN pip3 install mysql-connector-python

# Maintainer
MAINTAINER app_runner

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
#RUN pip3.8 install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]
