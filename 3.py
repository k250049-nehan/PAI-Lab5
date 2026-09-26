import json


def create_file():
    data=[
        {
            "model":"Linear Regression",
            "accuracy":0.85,
            "precision":0.82,
            "recall":0.80,
            "f1":0.81
        },
        {
            "model":"Decision Tree",
            "accuracy":0.90,
            "precision":0.88,
            "recall":0.86,
            "f1":0.87
        },
        {
            "model":"Neural Network",
            "accuracy":0.94,
            "precision":0.92,
            "recall":0.91,
            "f1":0.915
        }
    ]

    with open("model_results.json","w") as file:
        json.dump(data,file,indent=4)


def read_results():
    with open("model_results.json","r") as file:
        return json.load(file)


def display_results():
    data=read_results()

    for model in data:
        print(model)


def highest_accuracy():
    data=read_results()

    best=data[0]

    for model in data:
        if model["accuracy"]>best["accuracy"]:
            best=model

    print("\nHighest Accuracy:")
    print(best["model"],best["accuracy"])


def highest_f1():
    data=read_results()

    best=data[0]

    for model in data:
        if model["f1"]>best["f1"]:
            best=model

    print("\nHighest F1 Score:")
    print(best["model"],best["f1"])


def add_model():
    data=read_results()

    model={
        "model":input("Model name: "),
        "accuracy":float(input("Accuracy: ")),
        "precision":float(input("Precision: ")),
        "recall":float(input("Recall: ")),
        "f1":float(input("F1 Score: "))
    }

    data.append(model)

    with open("model_results.json","w") as file:
        json.dump(data,file,indent=4)

    print("Model added.")


def update_model(model_name):
    data=read_results()

    found=False

    for model in data:
        if model["model"]==model_name:
            model["accuracy"]=float(input("New accuracy: "))
            model["precision"]=float(input("New precision: "))
            model["recall"]=float(input("New recall: "))
            model["f1"]=float(input("New F1 score: "))

            found=True

    if found:
        with open("model_results.json","w") as file:
            json.dump(data,file,indent=4)

        print("Model updated.")
    else:
        print("Model does not exist.")


def delete_model(model_name):
    data=read_results()

    new_data=[]
    found=False

    for model in data:
        if model["model"]==model_name:
            found=True
        else:
            new_data.append(model)

    if found:
        with open("model_results.json","w") as file:
            json.dump(new_data,file,indent=4)

        print("Model deleted.")
    else:
        print("Model does not exist.")


create_file()

display_results()

highest_accuracy()

highest_f1()

add_model()

update_model("Decision Tree")

delete_model("Linear Regression")
