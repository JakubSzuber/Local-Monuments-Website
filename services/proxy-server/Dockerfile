## Nginx lightweight alpine image
FROM nginx:1.23-alpine-slim

## Update apk and add curl
RUN apk update; \
    apk add --no-cache curl

## Add nginx configuartion file
COPY conf /etc/nginx/conf.d/default.conf

## Use /app as a working directory
WORKDIR /app

## Add permissions
RUN chown -R nginx:nginx /app && chmod -R 755 /app && \
        chown -R nginx:nginx /var/cache/nginx && \
        chown -R nginx:nginx /var/log/nginx && \
        chown -R nginx:nginx /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R nginx:nginx /var/run/nginx.pid

## Switch to non-root user
USER nginx

## Healthchecks
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
