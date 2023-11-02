FROM node:14

WORKDIR /app

COPY app.js /app/
COPY package.json /app/
COPY package-lock.json /app/

RUN npm install

EXPOSE 8501

CMD ["node", "app.js"]
