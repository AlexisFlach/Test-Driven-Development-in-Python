FROM python as builder
WORKDIR /app
COPY . .

FROM nginx
EXPOSE 80
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/index.html /usr/share/nginx/html