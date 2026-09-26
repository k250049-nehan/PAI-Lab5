import requests
import json
import csv


try:

    url="https://jsonplaceholder.typicode.com/posts"

    params={
        "userId":1
    }

    response=requests.get(url,params=params,timeout=5)

    response.raise_for_status()

    data=response.json()

    processed_data=[]

    for item in data:
        record={
            "id":item["id"],
            "user_id":item["userId"],
            "text":item["title"]
        }

        processed_data.append(record)

    total=len(processed_data)

    print("Total records:",total)


    if total>0:
        longest=processed_data[0]

        for record in processed_data:
            if len(record["text"])>len(longest["text"]):
                longest=record

        print("Longest text:",longest["text"])

    with open("processed_data.json","w") as file:
        json.dump(processed_data,file,indent=4)

    with open("processed_data.csv","w",newline="") as file:
        fieldnames=["id","user_id","text"]

        writer=csv.DictWriter(file,fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(processed_data)


    print("\nData saved successfully.")


    with open("processed_data.json","r") as file:
        json_data=json.load(file)

    print("\nJSON verification:")
    print(json_data)


    with open("processed_data.csv","r") as file:
        reader=csv.DictReader(file)

        csv_data=list(reader)

    print("\nCSV verification:")
    print(csv_data)


except requests.exceptions.ConnectionError:
    print("Could not connect to the API.")

except requests.exceptions.Timeout:
    print("API request timed out.")

except requests.exceptions.HTTPError:
    print("HTTP error occurred.")

except FileNotFoundError:
    print("Required file was not found.")

except json.JSONDecodeError:
    print("Invalid JSON data.")

except OSError:
    print("File handling error.")

except ValueError:
    print("Invalid response received.")

else:
    print("\nProgram executed successfully.")

finally:
    print("Program execution completed.")
