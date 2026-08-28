FROM python:3.13-slim-trixie

RUN apt-get -y update && apt-get install -y libjpeg-dev

WORKDIR /log
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY yule_log/fire.py .

# ENV TOP_TEXT=
# ENV BOTTOM_TEXT=
ENTRYPOINT [ "python3" ]
CMD [ "fire.py" ]
