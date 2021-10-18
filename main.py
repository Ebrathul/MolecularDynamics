import pandas as pd
import csv
from os.path import dirname  # gets parent folder in a path
from os.path import join  # concatenate paths
import numpy as np
import re
import fileinput
import gromacs

def generate_input(file):
    #df = pd.read_csv(file, header=8) #,skipfooter =, header=8)  # skiprows=10  names=range(9) delimiter="\t"
    load_itp = pd.read_fwf(itp_file)
    save_csv = load_itp.to_csv("test.csv")
    df =pd.read_csv("test.csv")

    #file = open(itp_file, "r")
    # print(open(itp_file, "r").readlines())
    # filesplit = file.split()
    # filesplit_atoms = filesplit.
    # print(filesplit)
    #file.replace("    ", "\t")
    # lines = (len(file.readlines()))
    # arr = np.zeros((2, lines))
    # i = 0
    # atomfinder = False
    # with open(itp_file, "r") as f:
    #     while atomfinder == False:
    #         print(f.readline(i),i)
    #         if '[ atoms ]' in f.readline(i):
    #             atomfinder = True
    #             print(i)
    #         i += 1
    # for line in file:
    #     if "atoms" in line:
    #         print("Hey")
    #     arr[0, i] = line
    #     # i += 1
    #     if line == "b'[ atoms ]\n'":
    #         print("HEREREE")
    # print("ich bin arr", arr)
    # print(file)
    # df.dropna(inplace=True)
    # print(df)
    # print(df.columns)
    # # print(df.index)
    # print("filter", df.filter(like="[ atoms ]").columns)
    # # print("loc", df.loc[:, (df == '[ atoms ]').any()])
    # print("str.find", df["[ moleculetype ]"].str.find("bonds", 1))
    # index = df["[ moleculetype ]"].str.find("bonds", 1)
    # for i in range(index):
    #     print("index", index[i])
    # print(df.loc[df['[ moleculetype ]'] == 'bonds'])
    # df["Indexes"] = df["[ moleculetype ]"].str.find("bonds", 1)

    # table_names = ["[ atoms ]", "[ bonds ]"]
    # groups = df[0].isin(table_names).cumsum()
    # tables = {g.iloc[0, 0]: g.iloc[1:] for k, g in df.groupby(groups)}
    # print(list(tables))

    # print(df("[ bonds ]").nuniqeu())

def replace_bonds_index_w_name(atoms, bonds, name):
    df_output = bonds
    df_output = df_output.drop("one", axis=1)
    print("len", len(atoms))
    for i in range(len(atoms)):
        print(i, atoms["residu"].loc[i], atoms["atom"].loc[i])
        current_atom = atoms["atom"].loc[i]
        df_output["ai"] = df_output["ai"].replace(i + 1, current_atom)
        df_output["aj"] = df_output["aj"].replace(i + 1, current_atom)
        # if atoms["residu"].loc[i] == atoms["residu"].loc[0]:
        #     print(i, atoms["residu"].loc[i], atoms["atom"].loc[i])
        #     current_atom = atoms["atom"].loc[i]
        #     df_output["ai"] = df_output["ai"].replace(i + 1, current_atom)
        #     df_output["aj"] = df_output["aj"].replace(i + 1, current_atom)
        # else:
        #     print(i, atoms["residu"].loc[i], "dropped")
        #     df_output = df_output.drop(df_output.index[df_output["ai"] == i])
        #     df_output = df_output.drop(df_output.index[df_output["aj"] == i])
        # print(current_atom)
    with open(str(name + "_input.txt"), 'w') as f:
        dfAsString = df_output.to_string(header=False, index=False)
        f.write(dfAsString)
    print(df_output)

    # df_output.to_csv(str(name + "_input.txt"), index=False, sep="\t")
    return None

if __name__ == '__main__':
    gromacs.config.setup()
    # table_names = ["[ atoms ]", "[ bonds ]"]
    name = "POPC"  # POPC CHL1 GLPA itp
    # generate_input(itp_file)
    # itp = gromacs.fileformats.ITP(str(name + ".itp"))
    # gromacs.fileformats.convert


    # df_bonds = pd.read_csv("GLPA_Bonds.txt", header=1)  # names=["ai", "aj", "one"]
    # df_atoms = pd.read_csv("GLPA_Atoms.txt", header=1)  # names=["nr", "type", "resnr", "residu", "atom", "cgnr", "charge", "mass"]
    df_bonds = pd.read_csv(str(name + "_Bonds.csv"), header=0, skiprows=1, delimiter="\t", names=["ai", "aj", "one"])  # names=["ai", "aj", "one"]
    df_atoms = pd.read_csv(str(name + "_Atoms.csv"), header=0, skiprows=1, delimiter=",")  # names=["nr", "type", "resnr", "residu", "atom", "cgnr", "charge", "mass"]
    print(df_bonds)
    print(df_bonds.columns)
    print(df_atoms)
    print(df_atoms.columns)
    # df_atoms = df_atoms[['nr', 'atom']]
    # print(df_atoms.columns)

    replace_bonds_index_w_name(df_atoms, df_bonds, name)

    # with open("POPC_Atoms.txt", "r") as f:
    #     re.sub("\s+", ",", f.strip())
    #     print(f.readlines())

    # inputFile = open("POPC_Atoms.txt", "r")
    # exportFile = open("POPC_Atoms.csv", "w")
    # for line in inputFile:
    #     new_line = line.replace('    ', '\t')
    #     exportFile.write(new_line)
    # inputFile.close()
    # exportFile.close()
    # for line in fileinput.FileInput("POPC_Atoms.txt", inplace=1):
    #     print(line.replace("    ", "\t"))



    # data = np.loadtxt("GLPA_Bonds.txt")
    # print(data)





