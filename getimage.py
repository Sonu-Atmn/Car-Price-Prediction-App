
import serpapi
def get_img_link(search_key):
    params = {
    "q":f"{search_key}",
    "engine": "google_images",
    "ijn": "0",
    "api_key": "1cff78ab577d476d38faf35a9ed4414f28d14d5b5aadc3cf6aec594d1469b791"
    }

    search = serpapi.GoogleSearch(params)
    results = search.get_dict()
    images_results = results["images_results"]
    
    return images_results[0]['original']
 
    