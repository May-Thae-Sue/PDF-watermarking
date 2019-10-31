FROM python:3.7-alpine
WORKDIR /app
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip install Pillow PyPDF2
RUN pip install reportlab==3.2.0
COPY . .
