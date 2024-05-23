FROM jetpackio/devbox:latest AS base

# Installing your devbox project
WORKDIR /code
USER root:root
RUN chown ${DEVBOX_USER}:${DEVBOX_USER} /code
USER ${DEVBOX_USER}:${DEVBOX_USER}
COPY --chown=${DEVBOX_USER}:${DEVBOX_USER} devbox.json devbox.json
COPY --chown=${DEVBOX_USER}:${DEVBOX_USER} devbox.lock devbox.lock

RUN devbox install

FROM base AS runner

COPY --chown=${DEVBOX_USER}:${DEVBOX_USER} requirements.txt requirements.txt
RUN devbox run pip-install

COPY --chown=${DEVBOX_USER}:${DEVBOX_USER} main.py main.py
CMD ["devbox", "run", "serve-gunicorn"]
