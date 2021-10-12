import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # plot SCH
    elements = ["C1", "C2", "C3", "C4", "C5", "C6", "C12", "C13", "C14", ]
    data = pd.read_csv("SCH_POPC.dat", delimiter=" ", names=["atom1", "atom2", "SCH"])
    data_atom1 = data.loc[data["atom1"].isin(elements)]
    # columns_titles = ["atom2", "atom1"]
    # data_atom2 = data_atom1.append(data.loc[data["atom2"].isin(elements)])
    # df = df.reindex(columns=columns_titles)
    data_atom2 = data.loc[data["atom2"].isin(elements)]

    ax = data_atom1.plot.scatter(x="atom1", y="SCH", color="Blue", label="atom1")
    data_atom2.plot.scatter(x="atom2", y="SCH", color="Red", label="atom2", ax=ax)
    plt.show()
    print(data)
    print(data_atom1)
    print(data_atom2)

    # plot correlation
    name = "correlation_POPC_C1_C2.dat"
    name = "correlation_POPC_C217_C218.dat"
    name = "correlation_POPC_C34_C35.dat"
    data = pd.read_csv(name, delimiter=" ", names=["time", "correlation"])
    data.plot(x="time", y="correlation", marker="o")
    plt.show()
    print(data)