from flask import Flask, request, jsonify
import asyncio
from utils.get_data import get_social_network_data
from flask_caching import Cache


app = Flask(__name__)
cache = Cache(config={'CACHE_TYPE': 'redis', "CACHE_REDIS_URL":"redis://redis:6379/0", "CACHE_DEFAULT_TIMEOUT":30})
cache.init_app(app)


urls = [
    {"url": "https://takehome.io/twitter", "name":"twitter"}, 
    {"url":"https://takehome.io/facebook", "name":"facebook"}, 
    {"url": "https://takehome.io/instagram", "name":"instagram"}
]


@app.route("/")
async def social_network_activity():
    time_sensitive = request.args.get('time_sensitive', "True")
    if time_sensitive.lower() == "false":
        cached_data = cache.get("social_media_activity")
        cached_data["message"] = {}
        if cached_data is not None : return jsonify(cached_data)

    data_from_all_social_network = await asyncio.gather(*[get_social_network_data(url["url"], url["name"]) for url in urls])
    json_response = {}
    message = {}

    for index, data in enumerate(data_from_all_social_network):
        if data is not None:
            json_response[urls[index]["name"]] = len(data)
        else:
            cached_data = cache.get("social_media_activity")
            json_response[urls[index]["name"]] = cached_data.get(urls[index]["name"]) if cached_data is not None else 0
            cached_data_fallback_message = "Eratic response from server, falling back to last known cached value."
            failed_cache_fallback_message = "Got an eratic response from server, but cache is empty. Defaulting to 0 activity for now."
            message[urls[index]["name"]] = cached_data_fallback_message if cached_data is not None else failed_cache_fallback_message

    cache.set("social_media_activity", json_response, timeout=300)

    json_response["message"] = message

    return json_response


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host='0.0.0.0')