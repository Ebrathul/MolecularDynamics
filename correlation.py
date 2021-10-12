#!/usr/bin/env python
# Ferreira (2017)
from __future__ import print_function
import time

start = time.time()

import mdtraj as md
import math
import sys
import numpy as np

print('     ')
print('loading trajectory')
name = sys.argv[1]
print(name)
traj = md.load(str("traj_" + name + ".gro"))

time1 = time.time()
totaltime = time1 - start
print('(total time for loading: %d seconds)' % totaltime)
print('     ')

tstep = traj.time[1] - traj.time[0]
print('Simulation trajectory of %s ps with steps of %s ps' % (traj.time[-1], tstep))
print('     ')
lag = traj.n_frames - 1

topology = traj.topology

with open(str(name + "_input.txt")) as f:
    CHlabel = [line.rstrip('\n') for line in open(str(name + "_input.txt"))]

print('labels found in file inputCORR:')
print(CHlabel)
print('     ')

totalCH = len(CHlabel)
# print(totalCH)
nH = 0
for line in CHlabel:
    CHpair = line.split()
    Ccalc = topology.select("name " + str(CHpair[0]))
    Hsurround = topology.select("name " + str(CHpair[1]))
    print(CHpair[0], CHpair[1])
    start = time.time()
    # print(Hsurround)
    totalsurround = len(Hsurround)
    # print(totalsurround)
    densityFILE = open('correlation_' + name + '_' + str(CHpair[0]) + '_' + str(CHpair[1]) + '.dat', 'w+')
    corr = [0] * traj.n_frames
    nsurround = 0
    while nsurround < totalsurround:

        atom2 = topology.atom(Hsurround[nsurround])
        atom1 = topology.atom(Ccalc[nsurround])
        # print('Pair of atoms selected: %s and %s' % (atom1,atom2))
        # print('Calculation of the rotational autocorrelation function started')
        d3 = np.array(traj.xyz[:, Ccalc[nsurround]]) - np.array(traj.xyz[:, Hsurround[nsurround]])
        # print(d3)
        d3x = d3[:, 0]
        d3y = d3[:, 1]
        d3z = d3[:, 2]
        d = np.sqrt(d3x * d3x + d3y * d3y + d3z * d3z)
        # d=d3x*d3x+d3y*d3y+d3z*d3z
        # print(d)

        internucvector = np.array([d3x / d, d3y / d, d3z / d])
        internucvector = internucvector.conj().transpose()
        # print(internucvector)

        j = 0
        k = 0

        while j < lag:
            k = traj.n_frames - j
            c = np.ones((k, 1))
            d1x = internucvector[:k, 0]
            d2x = internucvector[j:, 0]
            d1y = internucvector[:k, 1]
            d2y = internucvector[j:, 1]
            d1z = internucvector[:k, 2]
            d2z = internucvector[j:, 2]
            cdot = d1x * d2x + d1y * d2y + d1z * d2z
            P2 = 1.5 * ((cdot) ** 2) - 0.5
            corr[j] = corr[j] + P2.dot(c) / k / totalsurround
            # print(traj.time[j],*(corr[j]),file=densityFILE)
            j = j + 1
        # print('loop j: %s' % j)
        nsurround = nsurround + 1
    j = 0
    while j < lag:
        print(traj.time[j], *(corr[j]), file=densityFILE)
        j = j + 1
    end = time.time()
    totaltime = end - start
    print('saved! total time of calculation: %d seconds' % totaltime)
    print('     ')
