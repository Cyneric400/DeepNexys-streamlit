FROM python:latest
LABEL authors="cyneric"

ENTRYPOINT ["top", "-b"]

WORKDIR /usr/server
RUN apt-get update && apt-get install git
RUN git clone https://github.com/Cyneric400/DeepNexys-streamlit.git
RUN python -m pip3 install -r requirements.txt
RUN streamlit run app.py

EXPOSE 8501