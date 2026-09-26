import requests
import json
import csv


try:
    query=input("Enter user ID: ")

    url="https://jsonplaceholder.typicode.com/posts"

    params={
        "userId":query
    }

    response=requests.get(url,params=params,timeout=5)

    response.raise_for_status()

    data=response.json()

    if len(data)==0:
        print("No results found.")
    else:
        print("\nRetrieved Text:")

        selected=[]

        for item in data:
            record={
                "text":item["title"],
                "source":"JSONPlaceholder",
                "user_id":item["userId"],
                "post_id":item["id"]
            }

            selected.append(record)

            print("Text:",item["title"])
            print("Source: JSONPlaceholder")
            print()

        with open("text_data.json","w") as file:
            json.dump(selected,file,indent=4)

        with open("text_data.csv","w",newline="") as file:
            fieldnames=["text","source","user_id","post_id"]

            writer=csv.DictWriter(file,fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(selected)

        print("Data saved to JSON and CSV.")

except requests.exceptions.ConnectionError:
    print("Connection error.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.HTTPError:
    print("HTTP error occurred.")

except ValueError:
    print("Invalid JSON response.")

except OSError:
    print("File error occurred.")

finally:
    print("Program completed.")
