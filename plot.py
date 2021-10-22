import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # plot SCH
    # elements = ["C1", "C2", "C3", "C4", "C5", "C6", "C12", "C13", "C14", ]
    # Carbons not bonding to Hydrogens where removed
    # elements = ["C1", "C2", "C3", "C4", "C5", "C6",
    #             "C1S", "C2S", "C3S", "C4S", "C5S", "C6S", "C7S", "C8S", "C9S", "C10S",
    #             "C11S", "C12S", "C13S", "C14S", "C15S", "C16S", "C17S", "C18S",
    #             "C2F", "C3F", "C4F", "C5F", "C6F", "C7F", "C8F", "C9F", "C10F",
    #             "C11F", "C12F", "C13F", "C14F", "C15F", "C16F"]  # GalCer
    # # elements = ["C11", "C12", "C13", "C14", "C15", "C1", "C2", "C3",
    # #             "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29", "C210",
    # #             "C211", "C212", "C213", "C214", "C215", "C216", "C217", "C218",
    # #             "C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39", "C310",
    # #             "C311", "C312", "C313", "C314", "C315", "C316"]  # POPC
    # # elements = ["C1", "C2", "C3", "C4", "C6", "C7", "C8", "C9",
    # #             "C11", "C12", "C14", "C15", "C16", "C17", "C18", "C19",
    # #             "C20", "C21", "C22", "C23", "C24", "C25", "C26"]  # Chol
    # # name = "SCH_POPC.dat"
    # # name = "SCH_CHL1.dat"
    # name = "SCH_Cer__POPC20_GalCer20.dat"
    # data = pd.read_csv(name, delimiter=" ", names=["atom1", "atom2", "SCH"])
    # data_atom1 = data.loc[data["atom1"].isin(elements)]
    # # columns_titles = ["atom2", "atom1"]
    # # data_atom2 = data_atom1.append(data.loc[data["atom2"].isin(elements)])
    # # df = df.reindex(columns=columns_titles)
    # data_atom2 = data.loc[data["atom2"].isin(elements)]
    # unique = np.expand_dims(np.asarray((data_atom1["atom1"].unique())), axis=1)
    # # print(unique, unique.shape[0], unique[0, 0])
    # unique = np.hstack((unique, np.zeros((unique.shape[0], 6))))
    # # print(unique)
    #
    # unique_dict = dict.fromkeys(data_atom1["atom1"].unique(), [])
    # print(unique_dict)
    #
    # for i in range(len(data_atom1)):
    #     for j in range(unique.shape[0]):
    #         if data_atom1["atom1"].iloc[i] == unique[j, 0] or data_atom1["atom2"].iloc[i] == unique[j, 0]:
    #             if ((data_atom1["atom1"].iloc[i].find("C") != -1 and data_atom1["atom2"].iloc[i].find("H") != -1) or
    #             (data_atom1["atom2"].iloc[i].find("C") != -1 and data_atom1["atom1"].iloc[i].find("H") != -1)):
    #                 print(i, data_atom1["atom1"].iloc[i], data_atom1["atom2"].iloc[i])
    #                 # unique_dict[data_atom1["atom1"].iloc[i]] = data_atom1["SCH"].iloc[i]
    #                 unique[j, int(unique[j, 4]+1)] += data_atom1["SCH"].iloc[i]
    #                 unique[j, 4] += 1
    #                 # print(unique_dict)
    #                 # print(data_atom1["atom1"].iloc[i], unique_dict[data_atom1["atom1"].iloc[i]], data_atom1["SCH"].iloc[i])
    #                 unique_dict[data_atom1["atom1"].iloc[i]].append(data_atom1["SCH"].iloc[i])
    #                 # np.append(unique_dict[data_atom1["atom1"].iloc[i]], data_atom1["SCH"].iloc[i])
    #             else:
    #                 print("Skipped", i, data_atom1["atom1"].iloc[i], data_atom1["atom2"].iloc[i])
    # print(unique)
    # unique[:, 5] = (unique[:, 1] + unique[:, 2] + unique[:, 3]) / unique[:, 4]
    # for i in range(len(unique)):
    #     for j in range(int(unique[i, 4])):
    #         sum_squ = (unique[i, j+1] - unique[i, 5]) ** 2
    #         unique[i, 6] = np.sqrt(sum_squ/(unique[i, 4]-1))
    # # unique[:, 6] = np.sqrt()
    # print(unique)
    # print(unique_dict)
    # unique1 = unique
    # ###################################################################################################################
    # name = "SCH_Cer__POPC20_GalCer20_Chol5.dat"
    # data = pd.read_csv(name, delimiter=" ", names=["atom1", "atom2", "SCH"])
    # data_atom1 = data.loc[data["atom1"].isin(elements)]
    # # columns_titles = ["atom2", "atom1"]
    # # data_atom2 = data_atom1.append(data.loc[data["atom2"].isin(elements)])
    # # df = df.reindex(columns=columns_titles)
    # data_atom2 = data.loc[data["atom2"].isin(elements)]
    # unique = np.expand_dims(np.asarray((data_atom1["atom1"].unique())), axis=1)
    # # print(unique, unique.shape[0], unique[0, 0])
    # unique = np.hstack((unique, np.zeros((unique.shape[0], 6))))
    # # print(unique)
    #
    # unique_dict = dict.fromkeys(data_atom1["atom1"].unique(), [])
    # print(unique_dict)
    #
    # for i in range(len(data_atom1)):
    #     for j in range(unique.shape[0]):
    #         if data_atom1["atom1"].iloc[i] == unique[j, 0] or data_atom1["atom2"].iloc[i] == unique[j, 0]:
    #             if ((data_atom1["atom1"].iloc[i].find("C") != -1 and data_atom1["atom2"].iloc[i].find("H") != -1) or
    #             (data_atom1["atom2"].iloc[i].find("C") != -1 and data_atom1["atom1"].iloc[i].find("H") != -1)):
    #                 print(i, data_atom1["atom1"].iloc[i], data_atom1["atom2"].iloc[i])
    #                 # unique_dict[data_atom1["atom1"].iloc[i]] = data_atom1["SCH"].iloc[i]
    #                 unique[j, int(unique[j, 4]+1)] += data_atom1["SCH"].iloc[i]
    #                 unique[j, 4] += 1
    #                 # print(unique_dict)
    #                 # print(data_atom1["atom1"].iloc[i], unique_dict[data_atom1["atom1"].iloc[i]], data_atom1["SCH"].iloc[i])
    #                 unique_dict[data_atom1["atom1"].iloc[i]].append(data_atom1["SCH"].iloc[i])
    #                 # np.append(unique_dict[data_atom1["atom1"].iloc[i]], data_atom1["SCH"].iloc[i])
    #             else:
    #                 print("Skipped", i, data_atom1["atom1"].iloc[i], data_atom1["atom2"].iloc[i])
    # print(unique)
    # unique[:, 5] = (unique[:, 1] + unique[:, 2] + unique[:, 3]) / unique[:, 4]
    # for i in range(len(unique)):
    #     for j in range(int(unique[i, 4])):
    #         sum_squ = (unique[i, j+1] - unique[i, 5]) ** 2
    #         unique[i, 6] = np.sqrt(sum_squ/(unique[i, 4]-1))
    # # unique[:, 6] = np.sqrt()
    # print(unique)
    # print(unique_dict)
    # unique2 = unique
    # #################################################################################################################
    # name = "SCH_Cer__POPC20_GalCer20_Chol10.dat"
    # data = pd.read_csv(name, delimiter=" ", names=["atom1", "atom2", "SCH"])
    # data_atom1 = data.loc[data["atom1"].isin(elements)]
    # # columns_titles = ["atom2", "atom1"]
    # # data_atom2 = data_atom1.append(data.loc[data["atom2"].isin(elements)])
    # # df = df.reindex(columns=columns_titles)
    # data_atom2 = data.loc[data["atom2"].isin(elements)]
    # unique = np.expand_dims(np.asarray((data_atom1["atom1"].unique())), axis=1)
    # # print(unique, unique.shape[0], unique[0, 0])
    # unique = np.hstack((unique, np.zeros((unique.shape[0], 6))))
    # # print(unique)
    #
    # unique_dict = dict.fromkeys(data_atom1["atom1"].unique(), [])
    # print(unique_dict)
    #
    # for i in range(len(data_atom1)):
    #     for j in range(unique.shape[0]):
    #         if data_atom1["atom1"].iloc[i] == unique[j, 0] or data_atom1["atom2"].iloc[i] == unique[j, 0]:
    #             if ((data_atom1["atom1"].iloc[i].find("C") != -1 and data_atom1["atom2"].iloc[i].find("H") != -1) or
    #             (data_atom1["atom2"].iloc[i].find("C") != -1 and data_atom1["atom1"].iloc[i].find("H") != -1)):
    #                 print(i, data_atom1["atom1"].iloc[i], data_atom1["atom2"].iloc[i])
    #                 # unique_dict[data_atom1["atom1"].iloc[i]] = data_atom1["SCH"].iloc[i]
    #                 unique[j, int(unique[j, 4]+1)] += data_atom1["SCH"].iloc[i]
    #                 unique[j, 4] += 1
    #                 # print(unique_dict)
    #                 # print(data_atom1["atom1"].iloc[i], unique_dict[data_atom1["atom1"].iloc[i]], data_atom1["SCH"].iloc[i])
    #                 unique_dict[data_atom1["atom1"].iloc[i]].append(data_atom1["SCH"].iloc[i])
    #                 # np.append(unique_dict[data_atom1["atom1"].iloc[i]], data_atom1["SCH"].iloc[i])
    #             else:
    #                 print("Skipped", i, data_atom1["atom1"].iloc[i], data_atom1["atom2"].iloc[i])
    # print(unique)
    # unique[:, 5] = (unique[:, 1] + unique[:, 2] + unique[:, 3]) / unique[:, 4]
    # for i in range(len(unique)):
    #     for j in range(int(unique[i, 4])):
    #         sum_squ = (unique[i, j+1] - unique[i, 5]) ** 2
    #         unique[i, 6] = np.sqrt(sum_squ/(unique[i, 4]-1))
    # # unique[:, 6] = np.sqrt()
    # print(unique)
    # print(unique_dict)
    # unique3 = unique
    #
    # fig, ax = plt.subplots(figsize=(10, 6))
    # plt.errorbar(unique1[:, 0], unique1[:, 5], yerr=unique1[:, 6], color='green', linestyle='None', marker='o', markersize=4, capsize=5, label='Chol 0')
    # plt.errorbar(unique2[:, 0], unique2[:, 5], yerr=unique2[:, 6], color='blue', linestyle='None', marker='o', markersize=3, capsize=3, label='Chol 5')
    # plt.errorbar(unique3[:, 0], unique3[:, 5], yerr=unique3[:, 6], color='red', linestyle='None', marker='o', markersize=2, capsize=1, label='Chol 10')
    # plt.xticks(rotation=60, size=9.5)
    # plt.legend()
    # ax.set(xlabel='Atom', ylabel='Order Parameter S',
    #        title='Order Parameter GalCer of C-H Bonds')
    # ax.grid()
    #
    # # ax = data_atom1.plot.scatter(x="atom1", y="SCH", color="Blue", label="atom1")
    # # data_atom2.plot.scatter(x="atom2", y="SCH", color="Red", label="atom2", ax=ax)
    # plt.show()

    # print(data)
    # print(data_atom1)
    # print(data_atom2)

    # plot correlation
    # name = "correlation_POPC_C1_C2.dat"
    name = "correlation_Cer_C1F_C2F.dat"
    data = pd.read_csv(name, delimiter=" ", names=["time", "C1F-C2F"])

    name = "correlation_Cer_C2F_C3F.dat"
    data1 = pd.read_csv(name, delimiter=" ", names=["time", "C2F-C3F"])

    name = "correlation_Cer_C18S_C17S.dat"
    # name = "correlation_POPC_C12_C11.dat"
    data2 = pd.read_csv(name, delimiter=" ", names=["time", "C18S-C17S"])

    # name = "correlation_POPC_C22_C23.dat"
    name = "correlation_Cer_C2S_C1S.dat"
    data3 = pd.read_csv(name, delimiter=" ", names=["time", "C2S-C1S"])

    # name = "correlation_POPC_C32_C33.dat"
    name = "correlation_Cer_C3S_C2S.dat"
    data4 = pd.read_csv(name, delimiter=" ", names=["time", "C3S-C2S"])

    name = "correlation_Cer_C10S_C9S.dat"
    data5 = pd.read_csv(name, delimiter=" ", names=["time", "C10S-C9S"])

    name = "correlation_Cer_C16S_C15S.dat"
    data6 = pd.read_csv(name, delimiter=" ", names=["time", "C16S-C15S"])

    fig, ax = plt.subplots()
    ax.set(xlabel='Time', ylabel='Correlation',
           title='Correlation of C Bonds in Cer')
    data.plot(x="time", y="C1F-C2F", marker="o", ax=ax)
    data1.plot(x="time", y="C2F-C3F", marker="o", ax=ax)
    data2.plot(x="time", y="C18S-C17S", marker="o", ax=ax)
    data3.plot(x="time", y="C2S-C1S", marker="o", ax=ax)
    data4.plot(x="time", y="C3S-C2S", marker="o", ax=ax)
    data5.plot(x="time", y="C10S-C9S", marker="o", ax=ax)
    data6.plot(x="time", y="C16S-C15S", marker="o", ax=ax)
    plt.legend(loc='upper right')

    plt.show()
    # print(data)
