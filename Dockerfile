FROM python:3.7-alpine
WORKDIR /app
RUN pip install PyPDF2
RUN pip install reportlab
COPY . .
