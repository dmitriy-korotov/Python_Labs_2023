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

    for col in train_data.columns:
        if train_data[col].isna().value_counts()[False] != train_data.shape[0]:
            try:
                train_data.loc[train_data[col].isna(), col] = train_data[col].median()
            except TypeError:
                continue
    print(train_data)


def task6() -> None:
    print("\t\t\t============ TASK6 ============")
    print("\t\t\t===== Survived prediction =====")

    print(train_data.groupby("Sex")["Survived"].value_counts())
    print(train_data.groupby("Pclass")["Survived"].value_counts())
    print(train_data.groupby("Age")["Survived"].value_counts())
    print(train_data.groupby("SibSp")["Survived"].value_counts())
    print(train_data.groupby("Parch")["Survived"].value_counts())
    print(train_data.groupby("Cabin")["Survived"].value_counts())

    test_data["Survived"] = 1

    test_data.loc[test_data.Pclass == 3, "Survived"][test_data.Parch == 0][test_data.SibSp == 0] = 0

    print(test_data)


def task8() -> None:
    print("\t\t\t================ TASK8 ===============")
    print("\t\t\t============== Plotting ==============")

    train_data.hist(column="Age", by="Survived", bins=40, figsize=(10, 20), legend=True, grid=True, xrot=0, layout=(2, 1))

    plt.title('Histogram survived by age')
    plt.ylabel('Survives')
    plt.xlabel('Age')
    plt.show()


def main() -> None:
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task8()


if __name__ == "__main__":
    main()
