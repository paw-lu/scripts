# https://jacobian.org/2019/nov/11/python-environment-2020/
FROM python:3.7

WORKDIR /code

RUN pip install -U pip && \
    pip install poetry

COPY poetry.lock pyproject.toml ./
COPY src/ ./src/

# Install poetry globally - with the current version of
# poetry, there is a known issue where poetry config will
# not create config.toml: https://github.com/sdispater/poetry/issues/1179
# As such, we create it ourselves.
RUN mkdir -p ${HOME}/.config/pypoetry/ && \
    touch ${HOME}/.config/pypoetry/config.toml && \
    poetry config settings.virtualenvs.create false && \

    # Set PRODUCTION to anything to invoke installation with --no-dev
    ARG PRODUCTION
RUN poetry install ${PRODUCTION:+--no-dev}
