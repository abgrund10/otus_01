FROM python:3.8.10-alpine
FROM alpine:3.12

LABEL version="1"
LABEL TAG=sintina1
WORKDIR /app
ADD . /app

ENV USR=appuser
ENV GRP=appgroup

#docker client.
#RUN apk --no-cache add curl

# create a group and user
RUN set -x ; addgroup -g 101 -S "$GRP" && \
	adduser \
	--disabled-password \
	-g 101 \
	-D \
	-s "/bin/bash" \
	-h "/home/$USR" \
	-G "$GRP" "$USR" && exit 0 ; exit 1

#install dependancies & selenoid
#RUN apk add --no-cache bash \
#    && apk add --no-cache shadow
#CMD ["/bin/bash", "/bin/sh"]

ARG container_id="docker ps --format \"{{.ID}}\""
COPY src/test_collection.py ${container_id}
CMD ["python3", "./src/test_collection.py"]
COPY ./requirements1.txt ./
RUN apk add py3-pip
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps
RUN pip install --no-cache-dir -r requirements1.txt
