import pickle
from sklearn.cluster import KMeans
from pathlib import Path

FILE_NAME = "./THPYAI25_intro_ml_Lektion_8/kmeans_model.pkl"


def run(model:KMeans):
    while True:
        choice = input("1. Predict\n2. Quit")
        if choice == "1":
            try:
                sex = int(input("Enter sex (0 or 1)"))
                marital = int(input("Enter Marital Status (0 or 1)"))
                age = int(input("Enter Age (18 or 100)"))
                edu = int(input("Enter Education (0, 1, 2 or 3)"))
                inc = float(input("Enter income $ "))
                occ = int(input("Enter occupation (0, 1 or 2)"))
                settle = int(input("Enter settlement size (0, 1, 2)"))

                pred = model.predict([[sex, marital, age, edu, inc, occ, settle]])
                print(f"Your predicted cluster lable is {pred}")

            except ValueError as e:
                print("NOOB!")


        elif choice == "2":
            break
        else:
            print("FFS")


def main():

    with open(FILE_NAME, "rb") as f:
        model:KMeans = pickle.load(f)

    print(model)
    run(model)

if __name__ == "__main__":
    main()