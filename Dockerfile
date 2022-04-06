FROM python:3.9.10-slim-buster
RUN useradd ansu_fati
ENV PYTHONUNBUFFERED=1
WORKDIR /ansu_fati
COPY --chown=ansu_fati:ansu_fati . .
RUN pip install -r requirements.txt
USER ansu_fati
