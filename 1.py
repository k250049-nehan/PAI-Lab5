def create_file():
    file=open("experiments.txt","w")

    file.write("E001,Linear Regression,Diabetes,0.01,100\n")
    file.write("E002,Decision Tree,Heart Disease,0.05,50\n")
    file.write("E003,Neural Network,Images,0.001,200\n")

    file.close()


def display_experiments():
    file=open("experiments.txt","r")

    print("\nExperiments:")
    for line in file:
        data=line.strip().split(",")

        print("ID:",data[0])
        print("Model:",data[1])
        print("Dataset:",data[2])
        print("Learning Rate:",data[3])
        print("Epochs:",data[4])
        print()

    file.close()


def search_experiment(exp_id):
    file=open("experiments.txt","r")

    found=False

    for line in file:
        data=line.strip().split(",")

        if data[0]==exp_id:
            print("\nExperiment Found:")
            print("ID:",data[0])
            print("Model:",data[1])
            print("Dataset:",data[2])
            print("Learning Rate:",data[3])
            print("Epochs:",data[4])
            found=True
            break

    file.close()

    if not found:
        print("Experiment does not exist.")


def add_experiment():
    exp_id=input("Enter experiment ID: ")
    model=input("Enter model name: ")
    dataset=input("Enter dataset name: ")
    rate=input("Enter learning rate: ")
    epochs=input("Enter number of epochs: ")

    file=open("experiments.txt","a")
    file.write(exp_id+","+model+","+dataset+","+rate+","+epochs+"\n")
    file.close()

    print("Experiment added successfully.")


def update_experiment(exp_id):
    file=open("experiments.txt","r")
    lines=file.readlines()
    file.close()

    found=False

    file=open("experiments.txt","w")

    for line in lines:
        data=line.strip().split(",")

        if data[0]==exp_id:
            model=input("Enter new model name: ")
            dataset=input("Enter new dataset name: ")
            rate=input("Enter new learning rate: ")
            epochs=input("Enter new number of epochs: ")

            file.write(exp_id+","+model+","+dataset+","+rate+","+epochs+"\n")
            found=True
        else:
            file.write(line)

    file.close()

    if found:
        print("Experiment updated successfully.")
    else:
        print("Experiment does not exist.")


def delete_experiment(exp_id):
    file=open("experiments.txt","r")
    lines=file.readlines()
    file.close()

    found=False

    file=open("experiments.txt","w")

    for line in lines:
        data=line.strip().split(",")

        if data[0]==exp_id:
            found=True
        else:
            file.write(line)

    file.close()

    if found:
        print("Experiment deleted successfully.")
    else:
        print("Experiment does not exist.")


create_file()

display_experiments()

search_experiment("E002")

add_experiment()

update_experiment("E001")

delete_experiment("E003")

display_experiments()
