# **RelyComply Social Media Coding Task**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Docker](https://img.shields.io/badge/docker-grey?style=for-the-badge&logo=docker) ![Rest](https://img.shields.io/badge/rest-16A6E9?style=for-the-badge&logo=json) ![Redis](https://img.shields.io/badge/redis-black?style=for-the-badge&logo=redis)

#### How to run it?

```
docker-compose up
```

#### How to request?

```
curl http://127.0.0.1/
```

Response

```
{
    "facebook": 2,
    "instagram": 5,
    "message": {
        "facebook": "Eratic response from server, falling back to last known cached value.",
        "instagram": "Eratic response from server, falling back to last known cached value.",
        "twitter": "Eratic response from server, falling back to last known cached value.",
    },
    "twitter": 2
}
```

If an erroneous response is returned from the prefetch, the server will fall back to the cached values and then state which of the data returned came from cache for context. Otherwise, should the cache be empty as well, then server will default to an activity count of 0.

_Alternatively, you could choose to prioritze a cached response by adding the time_sensitive query parameter depending on trading requirements._

This cached response will last for 5 minutes and will be invalidated everytime someone makes a request without the time_sensitive query parameter or the when the timeout is reached.

```
curl http://127.0.0.1?time_sensitive=False
```

Response

```
{
    "facebook": 2,
    "instagram": 5,
    "message": {},
    "twitter": 2
}
```

_This request will prioritize a cached response_
