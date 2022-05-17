FROM python:3.8.10-alpine
WORKDIR /code

ENV USR=appuser
ENV GRP=appgroup
ENV PS1='`date "+%F %T"` \u@\h  \w \n\n  '
ENV PRODUCT_DIR="/opt/foobar"
ENV GRP=appgroup
ENV EDITOR="vim"

#docker client.
RUN apk --no-cache add curl
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz

# create a group and user
RUN set -x ; addgroup -g 101 -S "$GRP" && \
	adduser \
	--disabled-password \
	-g 101 \
	-D \
	-s "/bin/bash" \
	-h "/home/$USR" \
	-G "$GRP" "$USR" && exit 0 ; exit 1

ENTRYPOINT ["/usr/bin/selenoid", "-listen", ":8080", "-conf", "/etc/selenoid/browsers.json", "-video-output-dir", "/opt/selenoid/video/"]
ARG container_id=docker ps --format "{{.ID}}"
COPY test_collection.py ${container_id}
CMD ["python3", "./test_collection.py"]
