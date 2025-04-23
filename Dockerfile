FROM python:3.13.3-slim

# Usuario que executará o container
RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

CMD [ "tail", "-f", "/dev/null" ]