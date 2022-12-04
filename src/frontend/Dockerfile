FROM node:lts-alpine

WORKDIR /opt/todo
COPY . .

RUN npm install
RUN npm update

CMD npm run dev