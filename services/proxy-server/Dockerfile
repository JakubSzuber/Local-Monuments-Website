FROM nginx:1.23-alpine-slim

RUN apk update

COPY conf /etc/nginx/conf.d/default.conf

WORKDIR /app

## add permissions
RUN chown -R nginx:nginx /app && chmod -R 755 /app && \
        chown -R nginx:nginx /var/cache/nginx && \
        chown -R nginx:nginx /var/log/nginx && \
        chown -R nginx:nginx /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R nginx:nginx /var/run/nginx.pid

## switch to non-root user
USER nginx
