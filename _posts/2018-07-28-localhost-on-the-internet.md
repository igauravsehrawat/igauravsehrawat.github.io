---
layout: post
title: "Localhost on the internet"
permalink: /localhost-on-the-internet/
description: "Show your localhost to the internet, the easy way."
tags: ["localhost", "internet", "ngrok", "localtunnel", "pagekite"]
share: true
comments: true
---

# Your Localhost On The Internet And That Too SSL enabled With No Restrictions.

## Introduction
There are tons of service which provide you the way to expose your localhost on internet. We need it for testing 3rd party APIs or show casing current development server. For example the most popular ones are:
1. [ngrok](https://ngrok.com/)
2. [localtunnel](https://localtunnel.github.io/www/)
3. [pagekite](https://pagekite.net/)

So why reinvent the wheel? Because you gotta get to the roots and understand the simple complexity. It's no big deal.

## Prerequisites
So what all do we need?
1. A Server (I will using $5 [DO](https://www.digitalocean.com/) server)
2. A Domain
3. Curiosity and Patience

### What are the benefits of this setup? You may ask.
+ Total Custom Domain and as many domains you want.
+ No limits on usages
+ More than other services' paid plans

> Let's get started, shall we?

It's just a 4 steps setup
1. Setup the listening port using nginx on the server associating it with the subdomain.
2. Add subdomain in DNS(We will be using awesome Digital Ocean DNS)
3. Add SSL certificate provided by our favorite [Let's Encrypt](https://letsencrypt.org/)
4. Forward the traffic using amazing SSH command.

## Step 1 - Configuring server with nginx to serve traffic for the subdomain
Please install `nginx` on the server first.
You need to add one config file for nginx in `sites-available` folder of `/etc/nginx` assuming you are using Ubutnu. The nginx config file looks like below.

```
map $http_upgrade $connection_upgrade {
    default upgrade;
    ''      close;
}

server {
    server_name 42.igauravsehrawat.com;

    location / {
        proxy_pass http://localhost:4242;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_set_header X-NginX-Proxy true;

        # Enables WS support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }
}

server {
    server_name www.42.igauravsehrawat.com;

    location / {
        proxy_pass http://localhost:4242;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_set_header X-NginX-Proxy true;

        # Enables WS support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }
}
```
Let's take a look at config.
1. There is `server_name` directive which tell what domain to serve the request, `listen` directive for which port to listen on the domain.
2. The `location` directive is important here, here we are just proxing request from `localhost` with port `4242`. This port is important since we will be directing our localhost traffic to it. Then there is setting header on the request.
3. Rest of directive is enabling websocket support on this setup by upgrading the connection. That's all.

Note: You need to change `server_name` as per your required sub-domain instead of `42.igauravsehrawat.com`.

## Step 2 - Configuring Subdomain on DNS
Using [Digital Ocean DNS Service](https://www.digitalocean.com/docs/networking/dns/how-to/manage-records/), we will add a subdomain of our choice, it be 42.igauravsehrawat.com as done in step 1

For adding a subdomain, we will create 3 records(A Record, AAAA record, CNAME record)
A and AAAA records will redirect to our digital ocean server as shown below.
![A & AAAA records](https://preview.ibb.co/iavxYo/Screen_Shot_2018_07_28_at_21_02_25.png)

CNAME is just an alias of our A/AAAA record. All three will appear as shown below
![All three](https://preview.ibb.co/ey6hzT/Screen_Shot_2018_07_28_at_21_03_03.png)

So that's all here, you should be able to access your sub-domain over internet, showing you `502 Bad Gateway` page, which is expected since nothing is being forwarded to port `4242`.


##. Step 3 - Enabling SSL
Enabling SSL is piece of cake, more easy than that.Follow the `certbot` installation sets from [here](https://certbot.eff.org/lets-encrypt/ubuntuxenial-nginx)

Then run the magic command for nginx
`sudo certbot --nginx`

You will see something like below
![certbot-run](https://preview.ibb.co/jgKVm8/Screen_Shot_2018_07_28_at_22_17_52.png)

Run it twice, one for sub-domain and one for CNAME(alias).

Now you should see this we you go to your sub-domain www.42.igauravsehrawat.com
![expected-bad-gateway](https://preview.ibb.co/jxi9Do/Screen_Shot_2018_07_28_at_22_29_50.png)
This is expected since nothing is running on port `4242` of localhost at the server.

Woof, we are just one step away from the happy dance.

## Step 4 - SSH Magic

Just one command to rule them all

`ssh -N -R localhost:4242:localhost:3000 root@42.igauravsehrawat.com`

-N tells "Do not execute a remote command.  This is useful for just forwarding ports."
-R tells "Connections to the given TCP port or Unix socket on the remote (server) host are to be forwarded to the local side."

First localhost is of the server and second is of local machine, then the address of your server. If you set up the SSH keys(Recommended) it would be seamless, no password, nothing.

That's it.

Happy Dance as promised.
![happy-dance](https://media1.tenor.com/images/88848d2067d622de8e4f314e28dc431a/tenor.gif)

> Wait, wait, we haven't tested yet.

## Testing

For testing I will just [create a react](https://github.com/facebook/create-react-app) app using `create-react-app` and do `npm start` to run it on port 3000(default).
And then run the magic SSH command
`ssh -N -R localhost:4242:localhost:3000 root@42.igauravsehrawat.com`

See it in action
![localhost-on-internet](https://preview.ibb.co/mhaAKT/localhost_on_internet.gif)

## Conclusion

With power of Digital Ocean, it is not that hard to have your own setup. You just have your own customized, SSL enable sub domain with no restrictions.
