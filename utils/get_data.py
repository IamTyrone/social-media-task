import aiohttp
import logging
from .validator import ValidateJsonResponse

async def get_social_network_data(url: str, social_network) -> dict | str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                validator = ValidateJsonResponse(data)
                if social_network == "twitter" and validator.validate_twitter_data(): return data
                if social_network == "facebook" and validator.validate_facebook_data(): return data
                if social_network == "instagram" and validator.validate_instagram_data(): return data

                raise Exception("Invalid social network response. Fall back to cache.")
                
    except Exception as e:
        logging.warning(f"Error getting social network data from the url {url}: {e}")
        return None