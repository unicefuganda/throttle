Throttle Project
================

The throttle project expects to recieve HTTP requests from kannel and simply
store them in the database.

A celery task is called frequently to grab the stored messages and then pass 
them onto the service being throttled.

Configuration
-------------

Change ROUTER_URL, and ROUTER_PASSWORD in throttle/throttle/settings/base.py
