# **RelyComply Social Media Coding Task**

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
