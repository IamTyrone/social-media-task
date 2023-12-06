

class ValidateJsonResponse:

    def __init__(self, data: list | str):
        self.data = data

    def validate_twitter_data(self)  -> bool:
        for entry in iter(self.data):
            username = entry.get("username")
            tweet = entry.get("tweet")
            data_has_no_username = username is None
            data_has_no_tweet = tweet is None
        
            if data_has_no_username and data_has_no_tweet:
                return False
        
        return True

    def validate_facebook_data(self) -> bool:
        for entry in iter(self.data):
            name = entry.get("name")
            status = entry.get("status")
            data_has_no_name = name is None
            data_has_no_status = status is None

            print(data_has_no_name, data_has_no_status)
        
            if data_has_no_name and data_has_no_status:
                return False
        
        return True

    def validate_instagram_data(self) -> bool:
        for entry in iter(self.data):
            username = entry.get("username")
            picture = entry.get("picture")
            data_has_no_username = username is None
            data_has_no_picture = picture is None
        
            if data_has_no_username and data_has_no_picture:
                return False
        
        return True