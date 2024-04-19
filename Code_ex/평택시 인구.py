import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import os
import warnings
import openpyxl
warnings.filterwarnings("ignore")

path = os.chdir('/Users/bestw/Library/CloudStorage/OneDrive-개인/개인_교육_자료/평택시_인구/이전')
sheet = openpyxl.load_workbook('/Users/bestw/Library/CloudStorage/OneDrive-개인/개인_교육_자료/평택시_인구/이전/2016년+1월말+평택시+연령별+인구현황.xlsx').sheetnames


