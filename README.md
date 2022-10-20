# **RelyComply Social Media Coding Task**

#### Problem

Our client, Morgain Stainley, needs an API with live data on the activity levels of different social networks to serve as an input to their AI trading bots. Specifically, they need an endpoint they can query to get a numeric indicator of the amount of content posted on each social network. This should be a quick little task, but the client is paying us a billion dollars so your implementation needs to be robust.

#### Solution

Fortunately, we’ve found some very simple endpoints that returns social media content from the last hour (don't tell the client!):

- [https://takehome.io/twitter](https://takehome.io/twitter)
- [https://takehome.io/facebook](https://takehome.io/facebook)
- https://takehome.io/instagram

(Let's pretending it's 10 years ago and Facebook hasn't yet bought Instagram.)

Complete the Flask server in `app.py` so that it will return a JSON response with a indicator of the activity level for each social network. Something along the lines of `{"instagram": ..., "facebook": ..., "twitter": ...}`.

If you are in doubt of a detail of the spec just use your best judgement and let me know what you decided with the submission.

#### Caveat

Because some of these social networks adopted the slogan *"Move fast and break things"*, they don't always respond predictably. They break. And respond with invalid JSON. Life's hard.

#### Quickstart

To get the project up and running, fork the repo and run:

```
pip install -r requirements.txt
flask --debug run
```

The submission should just be a link to your forked repo.