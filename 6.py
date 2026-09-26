import requests


url="https://jsonplaceholder.typicode.com/posts"


try:

    response=requests.get(url+"/1",timeout=5)

    print("GET Status:",response.status_code)
    print("GET Response:",response.json())

    new_data={
        "title":"AI Image Prediction",
        "body":"Image classified successfully",
        "userId":1
    }

    response=requests.post(url,json=new_data,timeout=5)

    print("\nPOST Status:",response.status_code)
    print("POST Response:",response.json())

    updated_data={
        "id":1,
        "title":"Updated AI Prediction",
        "body":"Prediction has been updated",
        "userId":1
    }

    response=requests.put(url+"/1",json=updated_data,timeout=5)

    print("\nPUT Status:",response.status_code)
    print("PUT Response:",response.json())

    response=requests.delete(url+"/1",timeout=5)

    print("\nDELETE Status:",response.status_code)
    print("DELETE Response:",response.text)


except requests.exceptions.ConnectionError:
    print("Connection error.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.HTTPError:
    print("HTTP error occurred.")

except ValueError:
    print("Invalid JSON response.")

except requests.exceptions.RequestException:
    print("API request failed.")

finally:
    print("\nREST API operations completed.")
