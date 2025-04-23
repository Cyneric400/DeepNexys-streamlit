FROM python:latest
LABEL authors="cyneric"

WORKDIR /usr/server
RUN apt-get update && apt-get install git && apt-get install sqlite3
RUN git clone https://github.com/Cyneric400/DeepNexys-streamlit.git
WORKDIR /usr/server/DeepNexys-streamlit
RUN python -m pip install -r requirements.txt
#WORKDIR /usr/server/DeepNexys-streamlit/VTI64_db
RUN sqlite3 VTI64_db/vti64.db -init VTI64_db/schema.sql ".read VTI64_db/insert_test.sql"
#WORKDIR /usr/server/DeepNexys-streamlit
RUN curl -fsSL https://ollama.com/install.sh | sh
#RUN #ollama serve

CMD ["sh", "-c", "streamlit run app.py && ollama serve"]

EXPOSE 11434