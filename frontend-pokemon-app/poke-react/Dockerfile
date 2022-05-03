# pull the base image
FROM node:12.2.0-alpine

# set the working direction
WORKDIR /poke-react
# add `/app/node_modules/.bin` to $PATH
ENV PATH /poke-react/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./

COPY package-lock.json ./

RUN npm install

# add app
COPY . ./

# start app
CMD ["npm","start"]