# Stage 1: Python setup
FROM tiangolo/uwsgi-nginx-flask:python3.8 as python-stage

USER root

# Change the permissions of the /etc/nginx/ directory
RUN chmod 777 /etc/nginx/

# Install the requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
RUN rm /app/requirements.txt

# Copy the application code and the uwsgi.ini file
COPY ./app /app

# Stage 2: Node.js setup
FROM node:14 as node-stage

WORKDIR /app/client

# Copy the client code
COPY ./app/client /app/client

# Install npm dependencies and run autobuild
RUN npm install
RUN npm run build

# Stage 3: Final stage
FROM python-stage

# Copy the built client code from the node-stage
COPY --from=node-stage /app/client /app/client

WORKDIR /app

CMD ["python", "app.py"]