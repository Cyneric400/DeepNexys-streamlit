FROM python:latest
LABEL authors="cyneric"

ENTRYPOINT ["top", "-b"]

WORKDIR /usr/server
RUN apt-get update && apt-get install git
RUN git clone https://github.com/Cyneric400/DeepNexys-streamlit.git
WORKDIR /usr/server/DeepNexys-streamlit
RUN python -m pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]

EXPOSE 8501