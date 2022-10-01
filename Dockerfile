FROM python:3.10.4

WORKDIR /usr/bin/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit","run", "web\\app.py"]



