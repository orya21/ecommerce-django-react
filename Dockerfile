# FROM python:3
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# WORKDIR /code
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# COPY . .
# CMD ["python", "manage.py","runserver"]


# Stage 1: Building React application
FROM node:14.16.0 as build

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./

RUN npm install --silent

COPY . .

RUN npm run build

# Stage 2: Running Django application with Nginx
FROM python:3.9.2-alpine

RUN apk add --no-cache nginx

COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
