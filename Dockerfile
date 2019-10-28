FROM python:3.7-alpine
WORKDIR /app
RUN pip install pyPDF2
RUN pip install reportlab
COPY . .
