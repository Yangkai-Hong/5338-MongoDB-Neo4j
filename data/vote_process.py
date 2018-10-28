#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:04:37 2017

@author: hyk
"""

import pandas as pd
import time

df = pd.read_csv("/Users/hyk/Desktop/5338/project/odqa/Votes.csv")

CreationTime = []
for i in df["CreationDate"].values:
    CreationTime.append(int(time.mktime(time.strptime(i,'%d/%m/%Y %H:%M'))))  
df["CreationTime"] = pd.Series(CreationTime)

Id = []
for i in df["Id"].values:
    try:
        Id.append(int(i))
    except ValueError:
        Id.append(0)
df["Id"] = pd.Series(Id)

PostId = []
for i in df["PostId"].values:
    try:
        PostId.append(int(i))
    except ValueError:
        PostId.append(0)
df["PostId"] = pd.Series(PostId)

VoteTypeId = []
for i in df["VoteTypeId"].values:
    try:
        VoteTypeId.append(int(i))
    except ValueError:
        VoteTypeId.append(0)
df["VoteTypeId"] = pd.Series(VoteTypeId)

df.to_csv('Votes1.csv')

