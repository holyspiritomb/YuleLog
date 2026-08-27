FROM python:3.13-slim-trixie

RUN useradd --create-home --shell /bin/bash app_user
RUN apt-get -y update && apt-get install -y libjpeg-dev
ENV LDFLAGS=-L/usr/lib/x86_64-linux-gnu/
RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /log
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY yule_log/fire.py .

USER app_user
ENV TOP_TEXT="HAPPY"
ENV BOTTOM_TEXT="LOG"
ENTRYPOINT [ "python3" ]
CMD [ "fire.py" ]
