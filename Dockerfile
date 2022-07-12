# syntax=docker/dockerfile:1
FROM node:16
WORKDIR /front-end/
RUN npm install
RUN npm run build
WORKDIR /
RUN mkdir /FEProdBuild
COPY /frontend/build /FEProdBuild