import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # plot SCH
    # elements = ["C1", "C2", "C3", "C4", "C5", "C6", "C12", "C13", "C14", ]
    # elements = ["C1", "C2", "C3", "C4", "C5", "C6",
    #             "C1S", "C2S", "C3S", "C4S", "C5S", "C6S", "C7S", "C8S", "C9S", "C10S",
    #             "C11S", "C12S", "C13S", "C14S", "C15S", "C16S", "C17S", "C18S",
    #             "C1F", "C2F", "C3F", "C4F", "C5F", "C6F", "C7F", "C8F", "C9F", "C10F",
    #             "C11F", "C12F", "C13F", "C14F", "C15F", "C16F"]  # GalCer
    elements = ["C11", "C12", "C13", "C14", "C15", "C1", "C2", "C3",
                "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29", "C210",
                "C211", "C212", "C213", "C214", "C215", "C216", "C217", "C218",
                "C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39", "C310",
                "C311", "C312", "C313", "C314", "C315", "C316"]  # POPC
    # elements = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10",
    #             "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18", "C19",
    #             "C20", "C21", "C22", "C23", "C24", "C25", "C26"]  # Chol
    data = pd.read_csv("SCH_POPC.dat", delimiter=" ", names=["atom1", "atom2", "SCH"])
    data_atom1 = data.loc[data["atom1"].isin(elements)]
    # columns_titles = ["atom2", "atom1"]
    # data_atom2 = data_atom1.append(data.loc[data["atom2"].isin(elements)])
    # df = df.reindex(columns=columns_titles)
    data_atom2 = data.loc[data["atom2"].isin(elements)]
    unique = np.expand_dims(np.asarray((data_atom1["atom1"].unique())), axis=1)
    # print(unique, unique.shape[0], unique[0, 0])
    unique = np.hstack((unique, np.zeros((unique.shape[0], 6))))
    # print(unique)

    unique_dict = dict.fromkeys(data_atom1["atom1"].unique(), [])
    print(unique_dict)

    for i in range(len(data_atom1)):
        for j in range(unique.shape[0]):
            if data_atom1["atom1"].iloc[i] == unique[j, 0] or data_atom1["atom2"].iloc[i] == unique[j, 0]:
                if ((data_atom1["atom1"].iloc[i].find("C") != -1 and data_atom1["atom2"].iloc[i].find("H") != -1) or
                (data_atom1["atom2"].iloc[i].find("C") != -1 and data_atom1["atom1"].iloc[i].find("H") != -1)):
                    print(i, data_atom1["atom1"].iloc[i], data_atom1["atom2"].iloc[i])
                    # unique_dict[data_atom1["atom1"].iloc[i]] = data_atom1["SCH"].iloc[i]
                    unique[j, int(unique[j, 4]+1)] += data_atom1["SCH"].iloc[i]
                    unique[j, 4] += 1
                    # print(unique_dict)
                    # print(data_atom1["atom1"].iloc[i], unique_dict[data_atom1["atom1"].iloc[i]], data_atom1["SCH"].iloc[i])
                    unique_dict[data_atom1["atom1"].iloc[i]].append(data_atom1["SCH"].iloc[i])
                    # np.append(unique_dict[data_atom1["atom1"].iloc[i]], data_atom1["SCH"].iloc[i])
                else:
                    print("Skipped", i, data_atom1["atom1"].iloc[i], data_atom1["atom2"].iloc[i])
    print(unique)
    unique[:, 5] = (unique[:, 1] + unique[:, 2] + unique[:, 3]) / unique[:, 4]
    for i in range(len(unique)):
        for j in range(int(unique[i, 4])):
            sum_squ = (unique[i, j+1] - unique[i, 5]) ** 2
            unique[i, 6] = np.sqrt(sum_squ/(unique[i, 4]-1))
    # unique[:, 6] = np.sqrt()
    print(unique)
    print(unique_dict)

    fig, ax = plt.subplots(figsize=(10, 6))
    plt.errorbar(unique[:, 0], unique[:, 5], yerr=unique[:, 6], linestyle='None', marker='o', markersize=2, capsize=2)
    plt.xticks(rotation=60, size=9.5)
    ax.set(xlabel='Atom', ylabel='Order Parameter S',
           title='Order Parameter')
    ax.grid()

    # ax = data_atom1.plot.scatter(x="atom1", y="SCH", color="Blue", label="atom1")
    # data_atom2.plot.scatter(x="atom2", y="SCH", color="Red", label="atom2", ax=ax)
    plt.show()

    # print(data)
    # print(data_atom1)
    # print(data_atom2)

    # plot correlation
    # name = "correlation_POPC_C1_C2.dat"
    # name = "correlation_POPC_C217_C218.dat"
    name = "correlation_POPC_C34_C35.dat"
    data = pd.read_csv(name, delimiter=" ", names=["time", "correlation"])
    data.plot(x="time", y="correlation", marker="o")
    plt.show()
    # print(data)