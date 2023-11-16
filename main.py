import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


TEST_FILE = "test.csv"
TRAIN_FILE = "train.csv"

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")


def task1() -> None:
    print("\t\t\t================ TASK1 ==============")
    print("\t\t\t===== Survived by class and sex =====")
    print(train_data.groupby(["Pclass", "Sex"])["Survived"].value_counts(normalize=True))


def task2() -> None:
    fields = ["Age", "Fare", "Pclass", "SibSp", "Parch"]

    print("\t\t\t======== TASK2 =========")
    print("\t\t\t===== Train: males =====")
    print(train_data[train_data["Sex"] == "male"][fields].describe())

    print("\t\t\t===== Test: males =====")
    print(test_data[test_data["Sex"] == "male"][fields].describe())

    print("\t\t\t===== Train: females =====")
    print(train_data[train_data["Sex"] == "female"][fields].describe())

    print("\t\t\t===== Test: females =====")
    print(test_data[test_data["Sex"] == "female"][fields].describe())


def task3() -> None:
    print("\t\t\t============ TASK3 ==============")
    print("\t\t\t===== Survived by embarked =====")
    print(train_data.groupby(["Embarked"])["Survived"].value_counts(normalize=True))


def task4() -> None:
    print("\t\t\t================ TASK4 ===============")
    print("\t\t\t===== Popular names and surnames =====")
    data = pd.concat([train_data, test_data])
    names_surnames = [el.split(',') for el in data["Name"]]
    names = [name[1].split()[1].strip(")(") for name in names_surnames]
    surnames = [surname[0] for surname in names_surnames]

    print("===== Popular names =====")
    d = {'Name': names, 'count': len(names) * [1]}
    print(pd.DataFrame(data=d, index=[*range(len(names))]).groupby("Name").count().sort_values("count")[-10:])

    print("===== Popular surnames =====")
    d = {'Surname': surnames, 'count': len(surnames) * [1]}
    print(pd.DataFrame(data=d, index=[*range(len(surnames))]).groupby("Surname").count().sort_values("count")[-10:])


def task5() -> None:
    print("\t\t\t========== TASK5 ==========")
    print("\t\t\t===== Filling columns =====")
    print(train_data["Cabin"])


def task8() -> None:
    print("\t\t\t================ TASK8 ===============")
    print("\t\t\t============== Plotting ==============")

    plt.hist(train_data['Age'], color='blue', edgecolor='black', bins=int(180 / 5))

    plt.title('Histogram of Arrival Delays')
    plt.ylabel('Survives')
    plt.xlabel('Age')
    plt.show()


def main() -> None:
    task1()
    task2()
    task3()
    task4()
    task5()
    task8()


if __name__ == "__main__":
    main()
