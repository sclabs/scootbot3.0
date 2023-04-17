# dep builder: builds wheels for all deps
FROM python:3.8 AS dep-builder

# build wheels for all deps in requirements.txt
COPY requirements.txt /build/requirements.txt
RUN pip wheel --no-deps -w /build/dist -r /build/requirements.txt

# base image: installs wheels for all dependencies
FROM python:3.8-slim AS base

# copy all wheels from builder and install
COPY --from=dep-builder [ "/build/dist/*.whl", "/install/" ]
RUN pip install --no-index /install/*.whl \
    && rm -rf /install

# app builder: builds wheel for just our app
FROM python:3.8 as app-builder

# copy app code and build wheel for our app
# the only file we've used above this line is requirements.txt
# therefore only the lines below will be re-run when app code changes
COPY . /build
RUN pip wheel --no-deps -w /build/dist /build

# final image: start from base and add just our app
FROM base AS final

# copy all wheels from builder and install
COPY --from=app-builder [ "/build/dist/*.whl", "/install/" ]
RUN pip install --no-index /install/*.whl \
    && rm -rf /install

# run our app
ENTRYPOINT [ "scootbot3" ]
