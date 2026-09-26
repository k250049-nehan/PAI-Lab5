import requests


try:
    url="https://jsonplaceholder.typicode.com/posts"

    params={
        "userId":1
    }

    response=requests.get(url,params=params,timeout=5)

    response.raise_for_status()

    data=response.json()

    if len(data)>0:
        result=data[0]

        print("Prediction Result:",result["title"])
        print("Confidence Score:",0.95)
        print("Input Information:",result["body"])
    else:
        print("No result was returned.")

except requests.exceptions.ConnectionError:
    print("Connection error. Please check your internet connection.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.HTTPError:
    print("HTTP error occurred.")

except ValueError:
    print("Invalid JSON response.")

except requests.exceptions.RequestException:
    print("An API error occurred.")

finally:
    print("API request completed.")
