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

_Alternatively, you could choose to prioritze a cached response by adding the time_sensitive query parameter depending on trading requirements._

This cached response will last for 5 minutes and will be invalidated everytime someone makes a request without the time_sensitive query parameter or the when the timeout is reached.

```
curl http://127.0.0.1?time_sensitive=False
```

_This request will prioritize a cached response_
