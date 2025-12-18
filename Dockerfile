FROM python:slim

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

RUN groupadd -r oppprimegroup && useradd -r -g oppprimegroup oppprimeuser

USER oppprimeuser
 
# Set the workdir
WORKDIR /home/oppprimeuser/code

COPY ./app /home/oppprimeuser/code/app

CMD  python /home/oppprimeuser/code/app/worker.py
