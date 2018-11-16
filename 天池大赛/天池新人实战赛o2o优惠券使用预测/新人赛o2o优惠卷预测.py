#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 22:57:01 2018

@author: jinyong
"""
import numpy as np
import pandas as pd

offline_train = pd.read_csv("data/ccf_offline_stage1_train.csv")
online_train = pd.read_csv("data/ccf_online_stage1_train.csv")
offline_test = pd.read_csv("data/ccf_offline_stage1_test_revised.csv")


