{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ab262adb-de7f-4cb8-bbf9-dac46c8c2771",
   "metadata": {
    "jp-MarkdownHeadingCollapsed": true,
    "tags": []
   },
   "source": [
    "# Machine Learning Regression Startup File\n",
    "\n",
    "Version  | Date | Author | Notes |\n",
    ":-------:|:----:|:-------|:-----:|\n",
    "0.1 |20 July 2023| Ken Dizon | Initial version\n",
    "\n",
    "**Objective**\n",
    "\n",
    "Write a startup ML script for Regression. The aim is to predict continuous values and plot a best-fit line/curve between the data of x and y. \n",
    "\n",
    "### Algorithms\n",
    "Regression | \n",
    ":---------:|\n",
    "ordinal, poisson, linear, polynomial, lasso, bayesian, NNR, decsion forest, KNNR |\n",
    "______________________\n",
    "#### Content\n",
    "1. **Load data**\n",
    "    * 1.1 Data Exploration\n",
    "2. **Data Preprocessing**\n",
    "    * 2.1 Cleaning\n",
    "    * 2.2 Missing Data\n",
    "    * 2.3 Scaling\n",
    "3. **Split - Test & Train**\n",
    "4. **Model Selection**\n",
    "5. **Model Training**\n",
    "5. **Model Evaluation**\n",
    "\n",
    "### Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4e28ce9e-91b0-4e04-8c3e-69fb7ab7450d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://scikit-learn.org/stable/\n",
      "Libraries imported successfully!\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    import numpy as np #math library \n",
    "    import scipy #computation\n",
    "    import matplotlib.pyplot as plt #visualization\n",
    "    %matplotlib inline\n",
    "    import pandas as pd #dataframes\n",
    "    import sklearn #algorithims\n",
    "    '''machine learning library'''\n",
    "    \n",
    "    print('https://scikit-learn.org/stable/')\n",
    "    print(\"Libraries imported successfully!\")\n",
    "except ImportError:\n",
    "    print(\"Libraries not installed. Please install it to use this library.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "332e641a-e434-435d-9e1e-def3df28f17d",
   "metadata": {},
   "source": [
    "_________\n",
    "# [1] Load Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b968b3fb-380a-459c-94a5-4b8eb485bb9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "filepath = \"/Users/Kenny/Documents/DataSets/FuelConsumption.csv\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1dff060-dd42-4ae0-a144-b9a24bfaece5",
   "metadata": {},
   "source": [
    "### `FuelConsumption.csv`:\n",
    "We have downloaded a fuel consumption dataset, **`FuelConsumption.csv`**, which contains model-specific fuel consumption ratings and estimated carbon dioxide emissions for new light-duty vehicles for retail sale in Canada. [Dataset source](http://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork1047-2023-01-01)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4112add4-494e-4c6f-a9d9-3f09bf206d9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data imported successfully!\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>MODELYEAR</th>\n",
       "      <th>MAKE</th>\n",
       "      <th>MODEL</th>\n",
       "      <th>VEHICLECLASS</th>\n",
       "      <th>ENGINESIZE</th>\n",
       "      <th>CYLINDERS</th>\n",
       "      <th>TRANSMISSION</th>\n",
       "      <th>FUELTYPE</th>\n",
       "      <th>FUELCONSUMPTION_CITY</th>\n",
       "      <th>FUELCONSUMPTION_HWY</th>\n",
       "      <th>FUELCONSUMPTION_COMB</th>\n",
       "      <th>FUELCONSUMPTION_COMB_MPG</th>\n",
       "      <th>CO2EMISSIONS</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2014</td>\n",
       "      <td>ACURA</td>\n",
       "      <td>ILX</td>\n",
       "      <td>COMPACT</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4</td>\n",
       "      <td>AS5</td>\n",
       "      <td>Z</td>\n",
       "      <td>9.9</td>\n",
       "      <td>6.7</td>\n",
       "      <td>8.5</td>\n",
       "      <td>33</td>\n",
       "      <td>196</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2014</td>\n",
       "      <td>ACURA</td>\n",
       "      <td>ILX</td>\n",
       "      <td>COMPACT</td>\n",
       "      <td>2.4</td>\n",
       "      <td>4</td>\n",
       "      <td>M6</td>\n",
       "      <td>Z</td>\n",
       "      <td>11.2</td>\n",
       "      <td>7.7</td>\n",
       "      <td>9.6</td>\n",
       "      <td>29</td>\n",
       "      <td>221</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2014</td>\n",
       "      <td>ACURA</td>\n",
       "      <td>ILX HYBRID</td>\n",
       "      <td>COMPACT</td>\n",
       "      <td>1.5</td>\n",
       "      <td>4</td>\n",
       "      <td>AV7</td>\n",
       "      <td>Z</td>\n",
       "      <td>6.0</td>\n",
       "      <td>5.8</td>\n",
       "      <td>5.9</td>\n",
       "      <td>48</td>\n",
       "      <td>136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2014</td>\n",
       "      <td>ACURA</td>\n",
       "      <td>MDX 4WD</td>\n",
       "      <td>SUV - SMALL</td>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>AS6</td>\n",
       "      <td>Z</td>\n",
       "      <td>12.7</td>\n",
       "      <td>9.1</td>\n",
       "      <td>11.1</td>\n",
       "      <td>25</td>\n",
       "      <td>255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2014</td>\n",
       "      <td>ACURA</td>\n",
       "      <td>RDX AWD</td>\n",
       "      <td>SUV - SMALL</td>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>AS6</td>\n",
       "      <td>Z</td>\n",
       "      <td>12.1</td>\n",
       "      <td>8.7</td>\n",
       "      <td>10.6</td>\n",
       "      <td>27</td>\n",
       "      <td>244</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   MODELYEAR   MAKE       MODEL VEHICLECLASS  ENGINESIZE  CYLINDERS  \\\n",
       "0       2014  ACURA         ILX      COMPACT         2.0          4   \n",
       "1       2014  ACURA         ILX      COMPACT         2.4          4   \n",
       "2       2014  ACURA  ILX HYBRID      COMPACT         1.5          4   \n",
       "3       2014  ACURA     MDX 4WD  SUV - SMALL         3.5          6   \n",
       "4       2014  ACURA     RDX AWD  SUV - SMALL         3.5          6   \n",
       "\n",
       "  TRANSMISSION FUELTYPE  FUELCONSUMPTION_CITY  FUELCONSUMPTION_HWY  \\\n",
       "0          AS5        Z                   9.9                  6.7   \n",
       "1           M6        Z                  11.2                  7.7   \n",
       "2          AV7        Z                   6.0                  5.8   \n",
       "3          AS6        Z                  12.7                  9.1   \n",
       "4          AS6        Z                  12.1                  8.7   \n",
       "\n",
       "   FUELCONSUMPTION_COMB  FUELCONSUMPTION_COMB_MPG  CO2EMISSIONS  \n",
       "0                   8.5                        33           196  \n",
       "1                   9.6                        29           221  \n",
       "2                   5.9                        48           136  \n",
       "3                  11.1                        25           255  \n",
       "4                  10.6                        27           244  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Load\n",
    "try:\n",
    "    df = pd.read_csv(filepath)\n",
    "    print(\"Data imported successfully!\")\n",
    "except ImportError:\n",
    "    print(\"Data not installed. Please Load Data.\")\n",
    "# take a look at the dataset\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "70860bcb-891a-4177-95ad-7f9b45ebc06e",
   "metadata": {},
   "source": [
    "## 1.1 Data Exploration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "286957b2-d5bd-4493-86ab-fbcfdaee18ba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>MODELYEAR</th>\n",
       "      <td>1067.0</td>\n",
       "      <td>2014.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2014.0</td>\n",
       "      <td>2014.00</td>\n",
       "      <td>2014.0</td>\n",
       "      <td>2014.00</td>\n",
       "      <td>2014.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ENGINESIZE</th>\n",
       "      <td>1067.0</td>\n",
       "      <td>3.346298</td>\n",
       "      <td>1.415895</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.00</td>\n",
       "      <td>3.4</td>\n",
       "      <td>4.30</td>\n",
       "      <td>8.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>CYLINDERS</th>\n",
       "      <td>1067.0</td>\n",
       "      <td>5.794752</td>\n",
       "      <td>1.797447</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.00</td>\n",
       "      <td>6.0</td>\n",
       "      <td>8.00</td>\n",
       "      <td>12.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>FUELCONSUMPTION_CITY</th>\n",
       "      <td>1067.0</td>\n",
       "      <td>13.296532</td>\n",
       "      <td>4.101253</td>\n",
       "      <td>4.6</td>\n",
       "      <td>10.25</td>\n",
       "      <td>12.6</td>\n",
       "      <td>15.55</td>\n",
       "      <td>30.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>FUELCONSUMPTION_HWY</th>\n",
       "      <td>1067.0</td>\n",
       "      <td>9.474602</td>\n",
       "      <td>2.794510</td>\n",
       "      <td>4.9</td>\n",
       "      <td>7.50</td>\n",
       "      <td>8.8</td>\n",
       "      <td>10.85</td>\n",
       "      <td>20.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>FUELCONSUMPTION_COMB</th>\n",
       "      <td>1067.0</td>\n",
       "      <td>11.580881</td>\n",
       "      <td>3.485595</td>\n",
       "      <td>4.7</td>\n",
       "      <td>9.00</td>\n",
       "      <td>10.9</td>\n",
       "      <td>13.35</td>\n",
       "      <td>25.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>FUELCONSUMPTION_COMB_MPG</th>\n",
       "      <td>1067.0</td>\n",
       "      <td>26.441425</td>\n",
       "      <td>7.468702</td>\n",
       "      <td>11.0</td>\n",
       "      <td>21.00</td>\n",
       "      <td>26.0</td>\n",
       "      <td>31.00</td>\n",
       "      <td>60.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>CO2EMISSIONS</th>\n",
       "      <td>1067.0</td>\n",
       "      <td>256.228679</td>\n",
       "      <td>63.372304</td>\n",
       "      <td>108.0</td>\n",
       "      <td>207.00</td>\n",
       "      <td>251.0</td>\n",
       "      <td>294.00</td>\n",
       "      <td>488.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           count         mean        std     min      25%  \\\n",
       "MODELYEAR                 1067.0  2014.000000   0.000000  2014.0  2014.00   \n",
       "ENGINESIZE                1067.0     3.346298   1.415895     1.0     2.00   \n",
       "CYLINDERS                 1067.0     5.794752   1.797447     3.0     4.00   \n",
       "FUELCONSUMPTION_CITY      1067.0    13.296532   4.101253     4.6    10.25   \n",
       "FUELCONSUMPTION_HWY       1067.0     9.474602   2.794510     4.9     7.50   \n",
       "FUELCONSUMPTION_COMB      1067.0    11.580881   3.485595     4.7     9.00   \n",
       "FUELCONSUMPTION_COMB_MPG  1067.0    26.441425   7.468702    11.0    21.00   \n",
       "CO2EMISSIONS              1067.0   256.228679  63.372304   108.0   207.00   \n",
       "\n",
       "                             50%      75%     max  \n",
       "MODELYEAR                 2014.0  2014.00  2014.0  \n",
       "ENGINESIZE                   3.4     4.30     8.4  \n",
       "CYLINDERS                    6.0     8.00    12.0  \n",
       "FUELCONSUMPTION_CITY        12.6    15.55    30.2  \n",
       "FUELCONSUMPTION_HWY          8.8    10.85    20.5  \n",
       "FUELCONSUMPTION_COMB        10.9    13.35    25.8  \n",
       "FUELCONSUMPTION_COMB_MPG    26.0    31.00    60.0  \n",
       "CO2EMISSIONS               251.0   294.00   488.0  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# summarize the data\n",
    "df.describe().T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e75d9310-29dc-4b5f-96db-d58a8295ce6e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ENGINESIZE</th>\n",
       "      <th>CYLINDERS</th>\n",
       "      <th>FUELCONSUMPTION_COMB</th>\n",
       "      <th>CO2EMISSIONS</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.0</td>\n",
       "      <td>4</td>\n",
       "      <td>8.5</td>\n",
       "      <td>196</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.4</td>\n",
       "      <td>4</td>\n",
       "      <td>9.6</td>\n",
       "      <td>221</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.5</td>\n",
       "      <td>4</td>\n",
       "      <td>5.9</td>\n",
       "      <td>136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>11.1</td>\n",
       "      <td>255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>10.6</td>\n",
       "      <td>244</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>10.0</td>\n",
       "      <td>230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>10.1</td>\n",
       "      <td>232</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>3.7</td>\n",
       "      <td>6</td>\n",
       "      <td>11.1</td>\n",
       "      <td>255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>3.7</td>\n",
       "      <td>6</td>\n",
       "      <td>11.6</td>\n",
       "      <td>267</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ENGINESIZE  CYLINDERS  FUELCONSUMPTION_COMB  CO2EMISSIONS\n",
       "0         2.0          4                   8.5           196\n",
       "1         2.4          4                   9.6           221\n",
       "2         1.5          4                   5.9           136\n",
       "3         3.5          6                  11.1           255\n",
       "4         3.5          6                  10.6           244\n",
       "5         3.5          6                  10.0           230\n",
       "6         3.5          6                  10.1           232\n",
       "7         3.7          6                  11.1           255\n",
       "8         3.7          6                  11.6           267"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Selecting features\n",
    "\n",
    "#cdf = df[['x1','x2','x3', 'x4]]\n",
    "cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]\n",
    "cdf.head(9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "26808e63-e5dc-4d74-bd1c-7944e0b88ee7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 4 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# plot data into histogram\n",
    "viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]\n",
    "viz.hist()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f27d517e-9565-4fb1-a04d-e7a96a0ccb96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEHCAYAAABBW1qbAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAAwDElEQVR4nO2df5xddXnn389MJiGTqMAksoGQGUqBdmItypTWTX+gAbHRF2i3unFHzUt9NZjQFu36smazW7XddNnWttLdJjYVJJqpLFvtyotSlERtV0ulAQFJkCUuCQSykIA/QBBI8uwf59yZM3fOuefHPeeeO3c+79fr+7r3fs/5nvPcm8z3Od/neb7PY+6OEEIIAdBXtwBCCCG6BykFIYQQk0gpCCGEmERKQQghxCRSCkIIISaRUhBCCDHJvCovbmYHgKeB48Axdx8zs1OB/wGMAAeAt7n798LzNwHvDc//bXf/UqvrL1myxEdGRqoSXwghepI777zzqLsvjTtWqVIIea27H418/jCw292vNrMPh59/18xGgbXASuB0YJeZnevux5MuPDIywp49e6qUXQgheg4zO5h0rA7z0eXAjvD9DuDNkf4b3P15d38I2A9c2HnxhBBi7lK1UnDgy2Z2p5mtD/tOc/fDAOHry8P+M4BHImMPhX1CCCE6RNXmo1Xu/piZvRy4zcy+0+Jci+mbkYMjVC7rAVasWFGOlEIIIYCKVwru/lj4+gTwtwTmoMfNbBlA+PpEePoh4MzI8OXAYzHX3O7uY+4+tnRprJ9ECCFEQSpTCma2yMxe0ngPvB64D7gJWBeetg74Yvj+JmCtmS0ws7OAc4A7qpJPCCHETKpcKZwGfN3M7iGY3P/O3W8FrgYuMbMHgUvCz7j7XuBGYB9wK3Blq8gjIcTcYmICRkagry94nZioW6LexGZz6uyxsTFXSKoQvc/EBKxfD88+O9U3OAjbt8P4eH1yzVbM7E53H4s7ph3NQoiuZ/Pm6QoBgs+bN9cjTy8jpSCE6HoefjhfvyiOlIIQoutJij5XVHr5SCkIIbqeLVsCH0KUwcGgX5SLlIIQousZHw+cysPDYBa8yslcDZ1IiCeEEG0zPi4l0Am0UhBCCDGJlIIQQohJpBSEEEJMIqUghBBiEikFIYQQk0gpCCGEmERKQQghxCRSCkIIISaRUhBCCDGJlIIQQohJpBSEEEJMUrlSMLN+M/uWmd0cfv6omT1qZneHbU3k3E1mtt/MHjCzS6uWTQghxHQ6kRDvKuB+4KWRvj9z949HTzKzUWAtsBI4HdhlZueqTrMQQnSOSlcKZrYceCPwqQynXw7c4O7Pu/tDwH7gwirlE0IIMZ2qzUefAD4EnGjq/00zu9fMrjOzU8K+M4BHIuccCvuEEEJ0iMqUgpm9CXjC3e9sOrQNOBs4HzgM/EljSMxlPOa6681sj5ntOXLkSIkSCyGEqHKlsAq4zMwOADcArzOzne7+uLsfd/cTwF8xZSI6BJwZGb8ceKz5ou6+3d3H3H1s6dKlFYovhBBzj8qUgrtvcvfl7j5C4ED+iru/w8yWRU57C3Bf+P4mYK2ZLTCzs4BzgDuqkk8IIcRM6ijH+Udmdj6BaegAcAWAu+81sxuBfcAx4EpFHgkhRGfpyOY1d/+au78pfP9Od/8Zd3+lu1/m7ocj521x97Pd/Tx3//tOyCaEmB1MTMDICPT1Ba8TE3VL1JtoR7MQIpWNG2HePDALXjdu7Oz9JyZg/Xo4eBDcg9f166UYqkBKQQjRko0bYds2OB4ac48fDz53UjFs3gzPPju979lng35RLuY+I+pz1jA2NuZ79uypWwwhepq+vuDpvBkzONG8A6mHZeglzOxOdx+LO6aVghCiJUnPjZ18nlyxIl+/KI6UghCi69myBQYHp/cNDgb9olykFIQQXc/4OGzfDsPDgcloeDj4PD5et2S9h5SCEKIlGzbk66+K8XE4cCDwIRw4IIVQFVIKQvQAVcbwb90aKID+/uBzf3/weevW9q6rfQfdiZSCEBVTdYx/XAz/u98NS5aUN+Fu3QrHjgXXP3asHIWgfQfdiUJShaiQRox/M2U8aTcYGQkm1VYMDnaXDT5J5uHhwDQkqqVVSKqUghAVMm/e1KavKP39wRN3GSTF8DfTTROu9h3Ui/YpCFETcQqhVX8RssbqP/xw8XukmcDy+ge076B7kVIQokIsrnRUi/4ixMXwx1F0wk1Lc1HEP6B9B92LlIIQFVLGbuC0p/TmGP6hIZg/f/o57Uy4n/xk6/4ieYm076B7kVIQc5q6s3+mkTUZXTSG/+hReO97p4eQrltXfMJNU2xJZqk0c5X2HXQnUgpiztKJ7J+NiTlrfzPbt+frh8Bss2PH9O+1Y0d14Z7yD/QWUgpizlJkws3L+vX5+psp4qjudJpp+Qd6i8qVgpn1m9m3zOzm8POpZnabmT0Yvp4SOXeTme03swfM7NKqZRNzm05EBrW7G7jISqOoOSeJtDQX4+OBeaosc5Wol06sFK4C7o98/jCw293PAXaHnzGzUWAtsBJ4A7DVzDIusoXIT7umnay0sxu4yEqjbHNOmmLrtLlKVEulSsHMlgNvBD4V6b4c2BG+3wG8OdJ/g7s/7+4PAfuBC6uUT8xt2jXtdIJVqwIHeJR584L+JOLMOQMD8MwzxdNetFJsqorWW1S9UvgE8CEgukfxNHc/DBC+vjzsPwN4JHLeobBPiEqoKtFbmWzePHPn87FjMyfc6OaxzZsD8000RNUMnnyymjxDZZurRL1UphTM7E3AE+5+Z9YhMX0zguHMbL2Z7TGzPUeOHGlLRiHKTvRWNlkm3LjNYzt2BCuGEydg8WJ44YXp48t8klf0UW9R5UphFXCZmR0AbgBeZ2Y7gcfNbBlA+PpEeP4h4MzI+OXAY80Xdfft7j7m7mNLly6tUHwh6ifLhJtmvqn6Sb6q6KOVK4MVTqOtXNne9UQ2KlMK7r7J3Ze7+wiBA/kr7v4O4CZgXXjaOuCL4fubgLVmtsDMzgLOAe6oSj4hZgNZJty0Sb/qJ/kqdievXAn79k3v27dPiqET1LFP4WrgEjN7ELgk/Iy77wVuBPYBtwJXunuJwYFCzD6yTLhpk34n9hGUvTu5WSGk9c8lKt+F7+6ztl1wwQUuRN3s3Ok+POxuFrzu3Nn5+w8OugcehaANDk6Xo24Z8xL9Ls1tLrNhQ/xvsmFDvusAezxhXtWOZiHaoBsqiGVZTTQ/yYNKYc5GOrELX0pBiDaYjTH6VSiysp3Co6P5+ucKndiFL6UgRBvUEaMfnXwbLW2Sj+5jWLcuvyK7+OLp97v44qljVTiF9+6dqQBGR4P+uUwnduFLKQjRBp2O0U8qztNqkm9eGSQ9VSbVeb74Yti9e3rf7t1TiqEqp/DevdMt53NdIUBnduFLKQjRBt2cIbSxWokzccWR9LTZrBDS+kV1dGIXvpSCEG3QzRXEGquVrKasMu3Sojqq3oUvpSBEDxJdrWQ1ZQ0PVyePmD1IKQjRBt0QktogabUSZ+KKY82a+P7Vq/P1i9mNlIIQLYhG7cTF83c6JLVVveSkHcXNJq4k38Ett8T379o1UwGsXh30Q+fqUojOIKUgRAJZVgF1hKTG7WlNS30Q3bx24kTsZVvKvGvX9Ps1FAKUFxFTefoGkY2krc6zoSnNhaiS4eH4lALDw1PnDA3FnzM0VJ1cGza49/cH9+nvdx8dzZf6IMv3ysvq1dOvtXp1/u9URvoGkQ2U5kKI/HRj8ZiNG2HbtumlL5P2A2zbFm/2KjuMdmICbr99et/tt880tbUyxXUifYPISJK2mA1NKwVRJVmeqM3izzErT45oMrtWieJatSoT5CX9TkNDU/cYGnKfPz9ZJiXA6yxopSBEfrI8USeFe/b1lZNsrtmvUZRnnw3SWzRkgtaprlultWgmaSf0k09Oyf3kk62rv8lZ3T1IKQiRQJaNaUnhnsePlxOimnU3chayypSW1qJMGqa4iy6KP57UL6rDvJ3Hj5oZGxvzPXv21C2GmONMTAST98MPB0/icTuDh4enUlbnoa+vvRVCK/r7g5XCihWBcmsou6T8StFx69dP7aRNO78Vjd9lZCR+xVH0dxOtMbM73X0s7phWCkK0Sbvhnq1CMatKrAfTVw7veU/21czx44ETuyFnURNP1BTXjU79uUplSsHMTjKzO8zsHjPba2YfC/s/amaPmtndYVsTGbPJzPab2QNmdmlVsglRFYsW5euPiyaKTrg/+ZPlyxjHCy/AVVflG9OIDDrvvGznDwzA0FC8Ka7T2WZFC5I80O02wIDF4fsB4JvALwAfBT4Yc/4ocA+wADgL+C7Q3+oeij4S3UDW6KA4GvsNmlt/f+vj0Xb66TPLcRZt7jP3HKSd3+p7Z41wylJSVJQHdUQfhfd+Jvw4ELZW1tHLgRvc/Xl3fwjYD1xYlXxClEG70UFplbRaZS5tTJ+PPpotjUV/fzb7f1xai6TrNeRIolWEU5RuzjY716jUp2Bm/WZ2N/AEcJu7fzM89Jtmdq+ZXWdmp4R9ZwCPRIYfCvuE6Bh5Uy20Gx2UFoqZNVTzG9+AQ4eCCfrEiUD2KIODsGNHcGxoKP6a0f5oWosNG+LPL7OwC8ysIy2FUA+VKgV3P+7u5wPLgQvN7BXANuBs4HzgMPAn4elxzzAznkHMbL2Z7TGzPUeOHKlEbjE3SbPvx5EUo5+VJHt8oz9p4j1+fGoPwfz50+V2D/LsL1489dS9bl2gwPrCv/hmpTIwANdcE3+vtMIuJ50UPy6pX3Q3HQtJNbOPAD9y949H+kaAm939FWa2CcDd/0t47EvAR9399rjrgUJSRbnMmxdvrunvDybZPGOaSQpVbYSFtjp/48bAlJK3CE5D7oaJK7qiGRiAl74UnnpqZkhqXpYsCTanNTM0BEePFrumqJZaQlLNbKmZnRy+XwhcDHzHzJZFTnsLcF/4/iZgrZktMLOzgHOAO6qST4hm0uz7eY9FSQpVzdIfrbSVh4ZscSauF18MJnL3wOz0jW/ku3aUp57K1y+6m3nppxRmGbDDzPoJlM+N7n6zmX3WzM4nMA0dAK4AcPe9ZnYjsA84Blzp7ioQKDpGf3/yJN9w0I6OTi8gPzyczYRUR1WzhrknLda/YSaDYqUdk1ZSSlExO6ky+uhed3+Vu7/S3V/h7r8f9r/T3X8m7L/M3Q9Hxmxx97Pd/Tx3//uqZBOiQdSxnOWpf98+WLly6nPWqmad2m8QpeGPyBrrXzQjaZJpLalfdDfa0SwKk1aVrNtlaHYsN0gL24ymqm4OpUzia1/LLlcrTj45vn9gINkRnFVx5fVZiB4laQPDbGjavFYf3bDZqF0Z0jaOFUnnnHdM3vOLFqPJssGu8b3zUuR3EvVCi81rSognCtENCczalaHVk717+vE48kYw5b1HkQipZhorpGaiq4s8FPmdRL20HX0URhL9BzPbHm44u87MritXTDGb6IYEZu3KkLYxbHQ0/nhzf9SEtXBh/JiyNnoViZBqZtWqqf0KDfr6gv4iJG1uS+oX3U1Wn8IXgZcBu4C/izQxR+mGBGZZZGjlc0grOL9370wF0Bx91Jzm4plnZk64q1cnP4EnPWUn9ZdRjGbz5pmhsCdOTBW8iaMb/EeiQyTZlaINuDvLeZ1u8inUx2zwKWSRccOGKd9Cf3/+QvFJpSiz/i6d8ilEyVtCNO13TPPNiO6DFj6FrErhPwNrspzbySalUC/tTqhl0KrWcJYay+1c3z173eSkexaRsSpFVlRGOZpnH62UQlbz0VXAzWb2YzN7Omw/rGTpImYFExNBgrVonqAdO7rLrNCuz6HZNBRXxjKruSzpnlnqQDcT3eF87Fh+5/CaNfn6037HvCYw0eUkaYvZ0LRSqI8ynsLbJc2ssWhRvIyLFmW7fpbvuHOn+/z56SuF/v7k1UanV1x1rRTSVl2ic9Cu+Si4BpcBHw/bm7KOq7JJKdRHXrt0FvJOGlWbNbKM37nTfWAgXSkkKa648QMDrb973Pl5KNunkPV3ar6vmRRDXbStFICrgd3Ae8J2G3B1lrFVNimF+ih7pVDEcZ02uXVCKST9Do2VQZITtvE7DQ3FHx8aipcpSQHlUQxF/u1aKewsv1PSamr+/Oxyi/IoQyncC/RFPvcD92YZW2WTUqiPsqOP0ibXuJVDN6wU2lVMeWVs9zu5x5u85s8v/m+XZeVRhtyiPFophTy5j06OvH9ZYSeG6AnKLp+Y5Mw8fjyYOuKcvEWctGWTtleijH0FVRA82yV/zsP73pevX3Q5Sdoi2oC3AweB64EdwEPA2ixjq2xaKfQOWeL940wc7Zo1WpFlfLv29qpWCq2c11UECaQ5y7VS6C4oydG8jMDZfDnwr7KOq7JJKfQOO3e69/VlUwxZI3WymDVaKZXR0fjxo6MzZS+6VyLvZJnFp5C2wa2KIIE0Vq+Ov+fq1dXdUyRTWCkAPxW+vjqutRrbiSal0DskTWRZWpJiWLw4/vzFi4PjWWzrzYqhWSGkUUbkTjNp0UdJyrWvL9vvUhXNikEKoT7aUQrbw9evxrSvtBrbiSalUC9lxp0nRelkXTnEkTbh5o38yUrz77JhQ3UmrjjSrtlqF7b2EMwNSjEf5W3ASQQ1lu8B9gIfC/tPJQhpfTB8PSUyZhOwH3gAuDTtHlIK9VF29FFRhdBqAq2iXkIaeX+XOpRClt+z03msRGdppRQy1VMws7cCt7r702b2H0Pz0R+4+7dajDFgkbs/Y2YDwNcJ0mX8GvCUu19tZh8OlcLvmtko8DngQuB0goys53qLOs2qp1AfZddTSKoTkIWitQqqqAOQ93epQoa+vvixZkE21Ky/dSdrY4jO0nY9BeA/hQrhF4FLCSKQPtlqQKiQngk/DoTNCRzVO8L+HcCbw/eXAze4+/Pu/hDBiuHCjPKJDpNUrD5LEfs42qk3kDR28eLW/UND8ceT+rOQFFp78GB5aaejdaXnzQs+R0lSJo3+iy7Kdp9O1sYQ3UNWpdB4rngjsM3dvwjMTxtkZv1mdjfwBHCbu38TOM3dDwOEry8PTz8DeCQy/FDYJ7qQsuPv4wq/xLF48fRaxKtXwy23xE+4P/pR/DUa/ddcE9Q2jjIwEPTnITpJt3q6dw+Uw7vfXVwxNNeVPn48+NysGFqxf3+28zpZG0N0EUl2pWgDbgb+EvguwSa2BcA9WcaG408mcE6/Avh+07Hvha9/Abwj0n8t8G9irrUe2APsWbFiRXlGNpGLLLbwPI7orPsUYOqaQ0Mzo4eK5ORpx1leNGqq4cwu20+Sds2sqb7z+hSU7G52QQlpLgYJfAHnhJ+XAa/PMjZyjY8AHyRwIi+LXOeB8P0mYFPk/C8Br2l1TTma6yMtcqdMh2veVmae/4ULp49buHD68VZRU2kTcJbfMc/vVMZvWWRSL5LUT9RLK6WQ1dF8NnDI3Z83s4uAVwKfcffvtxizFHjR3b9vZguBLwP/FfgV4EmfcjSf6u4fMrOVwF8z5WjeHSohOZq7kLQC8mU6XPPScKgWceJu3Bik62jliF24EJ59dupere6Rdnzx4ngz16JFQWnPZrJ8p3Z+ywzTwQyWLIEnn5zZPzQER48Wl0VURxmO5s8Dx83sJwnMOmcRTOCtWAZ81czuBf6FwKdwM0HG1UvM7EHgkvAz7r4XuBHYB9wKXNlKIfQ6ZdfETXNO5iWtgHy7BW7aoagtvNlen8Rzz029b9e3kub3mA3EKYRW/aLLSVpCRBtwV/j6IeC3wvffyjK2ytar5qOy9wCUUde3mTQzRt78OmWZjtrZLZxnA13W3zbtGnllrNp8VISyryeqhxJ8Ct8kSIp3H3BW2HdflrFVtl5VCmUnLKuisHraRNBpn0IZu4WLTp6tksGl+QyqUAp5nPbRVjTtRFU7w0V1tFIKWc1H7wZeA2xx94fM7CxgZ3nrFRGlbNNLmqmnCspOrZ3GiROBr6Kq60dZuHD651WrYPny4HsuXx58blBW2GuDDRvS++NSijdMhxCYtk4/ffrx1ath165iMl1zDcxvClCfP7/4dxQ1k6QtZkPr1ZVC2U9eaQnSilC2yaCd3EdJ98z7O2YJ12z+zbKsiFqFaxbJHpqlpnP0nkNDM6ODyk5joZDU2QVFVwpmdmP4+m0zuzfSvh06kMUsoPnJNq2/DqpYtZx/fr5+9/Rrnjgx3Um/efNUJFKDZ5+FdeumggQgWMXErWbOPTf+Pkn9AFu3BhFe7sHr1q0zzxkfn7rn4sXw4oszZdy8OfkeeYner1MrNlENLUNSzWyZux82s+G44+5eMKlBOfRqSGpa7pq6r9cYm0SWybWZl7wkPgQzK3H3TAubzXp+q/FJv22UwcFk01leGWF62Gx/f5DmI04xNKji31/MbgqHpPpUOoqDoQL4HvB0pIkKSCvxWPf1qqCKEMy8vpSs+Zei47P8hq2eyvPKWCTNRSf+/csOoRY1kmRXijbgCuBx4ABBKc6HgP+bZWyVrVd9CmUXVm/X7h1H2T6FdvwJ0RYtglMk6ipqr09q0fFxv22e3yWvjEW+U9khzp2+vigfSghJfRBYkuXcTrZeVgplpw1oNekXuV8RpVC0nnJRxVBkf0ZUKSQ5npvHR79XFkXSfL88MhZVxlU6gquo+SyqpQylcCswmOXcTrZeVQqd/iMrEu2Ud3JqpyxlkdYgS6RO9NxW10wbX+R3yStjFXtO2qWOms+iPVophay5j14FfJpgE9vzEdPTb5dmxyqAHM3lUMRpnGXMxERgS3/44eA7xdnJG7mQysx9FJUhD2U4z/PmMsrLypWwb9/M/tFR2Lu3/esXoeyCS6J6ysh99JfAV4B/Bu6MNFEBzRuP0vq7kYmJwHF78GAwoSY5TosW5elWmsNT0/rz8sAD+fo7QdxmucHBoF/MPrIqhWPu/jvu/ml339FolUo2h4kmXMvS3y5VVCCLi9+Po2hRnlaMjpZ/zawkrSharTTyRO7UsTs9jU7vXhfVklUpfNXM1pvZMjM7tdEqlWwOk2QiqiqmvIo0BVlXAGVPZu2YUZLMR2WbtqJMTASV2BorqrTKbGVXvCsLbV7rHbIqhX9HUATnn5gyHfWeMb+HaH763Lgx+Wl0fByuu276k95117X3h511kmpnNRKl4d5sVgh5nsLf9758/WVw1VUzdxu/+GLQH0fSXop2alwLMY0kD/RsaL0afVQ07LBBltj5vr72whLTZMwaJZQlW2iWlhRqmzd+Pk8kUJHfpd3zy5CxCpT7aHZB0ZBU4EOR929tOvaHrcZ2okkpxJM1dfKiRdXJmJSEr10lktaim/zqiJ/vhFLoNrR5bfbRSimkmY/WRt5vajr2hpIWK6KJdh2/We35VVb3yuP/6MtqxMzACy9MmV7qqP6W99+uCid/p0lKClhmwj3ROdL+HC3hfdzn6QfNzjSzr5rZ/Wa218yuCvs/amaPmtndYVsTGbPJzPab2QNmdmmub9JDzLX89MHCszwaZSDryPmU99+uF/6t6yy9KiogaQkRrDCCMpzN7+M+x4xdBrw6fP8S4P8Ao8BHgQ/GnD8K3AMsIKgB/V2gv9U9etV85N6ejTarqSVaG6Ds3EdZahNU2RrfqQ6zRt7fcrbb45XmYvZBC/PRvBSd8bNm9kOCVcHC8D3h55NSlM1hoJFl9Wkzux84o8WQy4Eb3P154CEz2w9cCNyeIqMoyBVXBK+NjWYNE8DBg1PRLEUjkMp++i9CQ/bGruoVK4INVVWHS46P57tH3vO7jS1bpv//AW1em9UkaYsyGzACPAy8lGClcAC4F7gOOCU8578D74iMuRb49VbX7dWVws6dM5+0zbI/QaY9RTdHrBR50kt7Sk/Kp9TJlcJcptOrj9m+2plr0G7uo3Yws8XAPxDUd/6CmZ0GHAUc+ANgmbu/x8z+Arjd3XeG464FbnH3zzddbz2wHmDFihUXHOy1PAnAggWBw7SZ+fPh+edn9jeTN4dPkVxLafdYsmTKtl8H3bBSqYvmlR+0LvQj5h5l5D4qeuMB4PPAhLt/AcDdH3f34+5+AvgrAhMRwCHgzMjw5cBjzdd09+3uPubuY0uXLq1S/NqIUwit+tulCofsU08VHyvaQ9FAoh0qUwpmZgQmoPvd/U8j/csip70FuC98fxOw1swWmNlZwDnAHVXJJ6aoIqHZqUqCUhuKBhLtUOVKYRXwTuB1TeGnf2Rm3zaze4HXAh8AcPe9wI3APoL6DVe6e41pvnoTs6AucLR8YycTmvX1VZtLSMyO8quie0mLPiqMu3+d+L0Mt7QYswVQzELFNOr6QuuC76046ST48Y/j+yHZfOQe+CmqVAyzaeNXFSgaSLRDpT4FUQ9ZU0dv3x68TkzAu941PVPnu97VOnncT/xE6/66nlYHBmbXxq8qUCpr0Q5SChWQJzNnFcRV5oqjkbb6iitmRhmdODG1jyHPPRr9a9bEH0/qb4fFi6cmv09/WpMfKJW1KE5l5qO5ShUbwaL09ZW/CSspB1I7uZFuSTASJvW3w3PPVVdrQoi5hlYKJVN1OGDDvLN+ffsrkCrt+p2MgKmz6pgQvYaUQsl0ajIsQ9FUucGrkz6FuquOCdFLSCmUTCcnw26OO0/b+1DmRK6qY0KUh5RCyXTSwdrNcedpETDnnVf82g2F0t8PGzYUD6sVQsyk8txHVTI2NuZ79nRXqeiknD9DQ3D0aLZrZLH1t8plk8dX4F5N7qM05s0r5gvImv9JCJFMbbmP5iJJSeDKSg5XRdx5HQXrizqHf+mXypVDCDEdhaTOMqoIvWyYX7ZvDybr/v7ATl+lWaa/v5hi+NrXShdFCBFBK4Ua2LgxMJ/E5SGqi61b4dixwPRz7Fj1dvqizmGFnwpRLVoplIxZsn0eAgXQyDsE5eQhqoO075lG8+okKwo/FaJatFIoQKs0FklO1kZ/I99QM0n9nSLv6uWnfzpffxzR1cnpp2cbo/BTIapFK4WctJvGIumpuE6zSJHVy/335+tPY2Cg9fFO+DmEEApJzc3ISKAImhkeDhKPpYVqJoVi9vcHT83Qfrhn3pDULDLluUeR/1JlX08IkYxCUkskqSR01lLRF12Ur79KFi4MXrth9ZLkK5APQYjOIqWQk3Ynr7vvztdfJc89F7wW+U6LF+frT6MbFJMQotoazWea2VfN7H4z22tmV4X9p5rZbWb2YPh6SmTMJjPbb2YPmNmlVcnWDu1OXlVvbitCkvO2lVP3k58MzE5R5s0L+oswPJyvXwhRDVWuFI4B/97dfxr4BeBKMxsFPgzsdvdzgN3hZ8Jja4GVwBuArWbWdcaD2TB5nXxyvvO3bg1yCOXJKTQ+DtdfPz230fXXF99l3cmcUUKIZCpTCu5+2N3vCt8/DdwPnAFcDuwIT9sBvDl8fzlwg7s/7+4PAfuBC6uSryizYfL6/vfzjymyea3M6l6dLMojhEimIz4FMxsBXgV8EzjN3Q9DoDiAl4ennQE8Ehl2KOzrKpImqe3bg30LohidLMojhEim8mnMzBYDnwfe7+4/bHVqTN+MYEQzW29me8xsz5EjR8oSMzNJUUbHj3cmdLKuus9V08k6FEKIZCpVCmY2QKAQJtz9C2H342a2LDy+DHgi7D8EnBkZvhx4rPma7r7d3cfcfWzp0qXVCZ9A3SGSZZbj7CbSivIIITpDldFHBlwL3O/ufxo5dBOwLny/DvhipH+tmS0ws7OAc4A7qpKvKN0SIllm3eeitEr3kZfxcVi3brqze9268tKDCyGyUeVKYRXwTuB1ZnZ32NYAVwOXmNmDwCXhZ9x9L3AjsA+4FbjS3btkCu5OkuztixZlG59n53MzjXQfBw+Ws3qZmAjCWRtK9/jx4HMvrYaEmA0ozUVO2plI3bOlc8h6j0ZqjWYuvhh2704fv2gRPPNMtns1k5buIy8nnRRfUW3BAvjxj/NfTwiRjNJc9CCt7O1f+Uq2a/zoR8XvX3a0UFKJTZXeFKKzSCnMMrKU4+zE4k/RQkL0JkqdPcuoohxnEbZsmZ5CHBQtJEQvoJVCD9KO3yMr4+PBaiWa5qLV6iWN1avz9QshqkGO5pzU7Wgus57C0BAcPZrt3E7Q7CBfvRp27apPHiF6FTma5xhZk/O97W3VypGXc8+dvk/h3HPrlUeIuYiUQg8Stzs4js98pnpZstIoCRrdp7BtW3qtaCFEuUgp9CDN9v4k2glJLZvt2/P1CyGqQUqhR4mmtZ4NqPKaEN2BlEKHSUpBEe0vOxInabXQiSglIcTsQkqhQzSqoWWZoPfvjz8nqV8IIcpCSqFDvOxlwWtSrqFof1LNhqT+NJLCWLspGnk2lDkVYi4gpdAhVEGsNaqnIER3IKUQw8aNMG9eYNKZN6+csMhTT23/Gr1M2TukhRDFUO6jJhrx8g0a8fKQrZh9N7J6dXwq7W5LITE+LiUgRN1opdBEWrz80FCx6z71VLFxZbBr10wFoBQSQog4pBSaSIuXL5oaou6U0rt2BY7lRpNCEELEUWWN5uvM7Akzuy/S91Eze7SpPGfj2CYz229mD5jZpVXJBa1rCzdy7zTT6L/llvz3GxiYcphmCUmdPz/+nKR+IYQoiypXCtcDb4jp/zN3Pz9stwCY2SiwFlgZjtlqZgnTc3uk1RZevz5+XKO/SBRRdMLPEh563XUzlYdZ0C+EEFVSmVJw938EslrSLwducPfn3f0hYD9wYRVybd48vTAMBJ83bw7eb90KGzZMz9a5YcOUkznJDNTfH0zccSuNF16Yun6WePzxcfjsZ6dH4nz2s3LCCiGqpw6fwm+a2b2heemUsO8M4JHIOYfCvtLJUlt41SpYvjyYkJcvDz43SIqn37EjyDOUlGuocf2s8fjR3EUHDkghCCE6Q6eVwjbgbOB84DDwJ2F/nKU91tBiZuvNbI+Z7Tly5EhuAZJSSjf608xLcfH069YFK4G+vqDF0VhhZI3Hb+X3yEK744UQcxR3r6wBI8B9aceATcCmyLEvAa9Ju/4FF1zgeenri8bgTLW+vuD48HD88f5+d7Pg+M6dU9fbudN9cDB+TKMNDk4fk0bcNfNcY+dO9/nzp4+fPz+fDEKI3gXY4wnzaqXlOM1sBLjZ3V8Rfl7m7ofD9x8Aft7d15rZSuCvCfwIpwO7gXPcvWXi5CLlONNKXfb1pecEGhycerofGYnPSdTfH5h+VqwITEN5zD9J1xweDkxJaSxZAk8+ObO/28pvCiHqoZZynGb2OeB24DwzO2Rm7wX+yMy+bWb3Aq8FPgDg7nuBG4F9wK3AlWkKoShpIadZ9hNEHdNJPoqGf6GIPyCL36MVcQqh0V9m6g4hRO9RZfTR2919mbsPuPtyd7/W3d/p7j/j7q9098saq4bw/C3ufra7n+fuf1+VXGkhp2vWxB9vpjFBJymRdjarJeVJKit/kkpdCiGSmHM7mtNCTrNuTmtM+klKJKtyqYKsqThU6lII0cycUwoQKIBjxwLfwbFj0xPdZTHRRENIk5RIkZ3PDZLyJGXNn3TNNcEu6jRU6lII0cycVAqtSNuc1hxC2q79P48MWU1S4+Pw6U9Phb0mkeRfEULMXaQUmkjbnNbsOC4ygaftISij4Ex081tSiuyLLsp+PSHE3EBKoYm8xV7yTuBpm+OKyJCGaj4LIbIipRBDnhQTeSfwtNxLVVCFiUsI0ZtIKRSg2fwD2ZVI3Ka05v4sq4k8VBE2K4ToTaQUctLuhJ22eQ7KX02U4aMQQswNpBRy0u6EnVbZDco395TtoxBC9C7z6hZgttHuhD08nJzXqMGKFfHntGPuGR+XEhBCpKOVQk7atc9nMeXI3COEqAsphZy0O2FnMeXI3COEqItKU2dXTZHU2WUwMRH4EB5+uFhqbCGEqJNaUmf3Mu2WysxSFU2V04QQdSClUAJ5JvAsIa1l71MQQoisyHzUJo0JPBqmGq3M1kyWqmrtVl4TQohWtDIfSSm0Sd4JPKncp1lgjsp6jhBCFKWucpzXmdkTZnZfpO9UM7vNzB4MX0+JHNtkZvvN7AEzu7Qqucom776FLCGtSkshhKiLKn0K1wNvaOr7MLDb3c8BdoefMbNRYC2wMhyz1cxmRbb/vBO49ikIIbqZKms0/yPQXCvscmBH+H4H8OZI/w3u/ry7PwTsBy6sSrYyyTuBa5+CEKKb6XSai9Pc/TCAux82s5eH/WcA/xw571DY1/U0Juo8+xaypJxQWgohRB10S+6juKKRsR5wM1sPrAdY0SVGdk3gQoheodP7FB43s2UA4esTYf8h4MzIecuBx+Iu4O7b3X3M3ceWLl1aqbBCCDHX6LRSuAlYF75fB3wx0r/WzBaY2VnAOcAdHZZNCCHmPJWZj8zsc8BFwBIzOwR8BLgauNHM3gs8DLwVwN33mtmNwD7gGHCluydUHhBCCFEVlSkFd397wqHVCedvARR0KYQQNaLcR0IIISaZ1WkuzOwIEJNkIjNLgKMliVMVkrEcJGM5SMZyqFvGYXePjdSZ1UqhXcxsT1L+j25BMpaDZCwHyVgO3SyjzEdCCCEmkVIQQggxyVxXCtvrFiADkrEcJGM5SMZy6FoZ57RPQQghxHTm+kpBCCFEhDmnFOKK/3QbZnammX3VzO43s71mdlXdMjVjZieZ2R1mdk8o48fqlikJM+s3s2+Z2c11y5KEmR0ws2+b2d1mVm85wQTM7GQz+xsz+074f/M1dcsUxczOC3+/Rvuhmb2/brmaMbMPhH8z95nZ58zspLplijLnzEdm9svAM8Bn3P0VdcsTR5gscJm732VmLwHuBN7s7vtqFm0SMzNgkbs/Y2YDwNeBq9z9n1OGdhwz+x1gDHipu7+pbnniMLMDwJi7d218vZntAP63u3/KzOYDg+7+/ZrFiiUs0vUo8PPu3s5eplIxszMI/lZG3f25ML3PLe5+fb2STTHnVgoJxX+6Cnc/7O53he+fBu6ny+pLeMAz4ceBsHXdE4aZLQfeCHyqbllmM2b2UuCXgWsB3P2FblUIIauB73aTQogwD1hoZvOAQRIyQtfFnFMKsw0zGwFeBXyzZlFmEJpl7iZIgX6bu3edjMAngA8BJ2qWIw0Hvmxmd4Y1Q7qNnwCOAJ8OTXGfMrNFdQvVgrXA5+oWohl3fxT4OEFC0MPAD9z9y/VKNR0phS7GzBYDnwfe7+4/rFueZtz9uLufT1D/4kIz6ypznJm9CXjC3e+sW5YMrHL3VwO/ClwZmjm7iXnAq4Ft7v4q4EeENda7jdC0dRnwP+uWpRkzO4Wg/PBZwOnAIjN7R71STUdKoUsJ7fSfBybc/Qt1y9OK0IzwNeAN9Uoyg1XAZaG9/gbgdWa2s16R4nH3x8LXJ4C/pftqlB8CDkVWg39DoCS6kV8F7nL3x+sWJIaLgYfc/Yi7vwh8AfjXNcs0DSmFLiR04l4L3O/uf1q3PHGY2VIzOzl8v5DgP/t3ahWqCXff5O7L3X2EwJzwFXfvqqcyADNbFAYUEJpkXg90VXScu/8/4BEzOy/sWk1Q/6QbeTtdaDoKeRj4BTMbDP/OVxP4DLuGOacUwuI/twPnmdmhsOBPt7EKeCfBk20jvG5N3UI1sQz4qpndC/wLgU+ha0M+u5zTgK+b2T0EFQf/zt1vrVmmOH4LmAj/zc8H/rBecWZiZoPAJQRP4F1HuNL6G+Au4NsEc3BX7W6ecyGpQgghkplzKwUhhBDJSCkIIYSYREpBCCHEJFIKQgghJpFSEEIIMYmUgpgzmNnxpiyahXfkmtk/lSlb07XHzOzPq7q+EK1QSKqYM5jZM+6+uG45hOhmtFIQc56wlsHHzOyusKbBT4X9S83strD/L83soJktCY89E75eZGZfi9QZmAh3qmJmF5jZP4RJ7r4UpkRvvvdbw7z695jZP0aueXP4/pbIyuYHZrYuTET4x2b2L2Z2r5ld0anfSvQ+UgpiLrGwyXz0byPHjoYJ6bYBHwz7PkKQGuPVBPmIViRc91XA+4FRgmyiq8LcVf8N+HV3vwC4DtgSM/b3gEvd/WcJkrhNw93XhEkH3wscBP5X+P4H7v5zwM8Bv2FmZ2X8DYRoyby6BRCigzwXTrBxNNIi3An8Wvj+F4G3ALj7rWb2vYSxd7j7IYAwlfgI8H3gFcBt4cKhnyBVcjPfAK4Pi63EpmYIVyefBd7m7j8ws9cDrzSzXw9PeRlwDvBQgnxCZEZKQYiA58PX40z9XVjOsdHxBux195YlK939fWb28wSFgO42s/Ojx8MKYjcAv+/ujSR5BvyWu38po3xCZEbmIyGS+TrwNoDw6fyUHGMfAJZaWMfYzAbMbGXzSWZ2trt/091/DzgKnNl0ytXAve5+Q6TvS8CG0ESFmZ3b5QVvxCxCKwUxl1gYmnca3OrurcJSPwZ8LvQ9/AOB+efpLDdy9xdC886fm9nLCP7WPgHsbTr1j83sHIKn/93APcCvRI5/ENgbkfv3CEqLjgB3hU7tI8Cbs8glRBoKSRUiATNbABx392PhE/+2Fj4JIXoCrRSESGYFcKOZ9QEvAL9RszxCVI5WCkIIISaRo1kIIcQkUgpCCCEmkVIQQggxiZSCEEKISaQUhBBCTCKlIIQQYpL/D/ZoRF15citXAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Linear Relationship \n",
    "# x = Features \n",
    "# y = Target 'Emissions'\n",
    "\n",
    "plt.scatter(cdf.FUELCONSUMPTION_COMB, #x\n",
    "            cdf.CO2EMISSIONS, #y\n",
    "            color='blue')\n",
    "plt.xlabel(\"FUELCONSUMPTION_COMB\")\n",
    "plt.ylabel(\"Emission\")\n",
    "plt.show()\n",
    "\n",
    "plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')\n",
    "plt.xlabel(\"Engine size\")\n",
    "plt.ylabel(\"Emission\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "65d0cba2-4b72-44b8-8916-95ceb5e31f3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEWCAYAAACJ0YulAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAAnqElEQVR4nO3de5wcVZ338c83ExKIgNwiGwhJEIOaoKKOKOKuaOLCIg/IPovGHRQFDRJU3PVGZFdh1+z6eAV3n0SjsESJYLytPCyKMIgXRHACiCTAEjchxEQYUO4azPB7/jhnJjWT7pnuZKq7M/19v1796q5fXfpMTVX/qk5VnaOIwMzMDGBcswtgZmatw0nBzMwGOCmYmdkAJwUzMxvgpGBmZgOcFMzMbEBbJgVJfy7p7maXY0dJepukn+7A/N+TdOpolmnI8mdICknjq4z/iKQvl/X9ZmWTtErS0Tswf6n74PYY00lB0jpJc4fGI+InEfHcZpRpKEnnSfqTpMclPSzpZ5KOLOl7Li3GIuKvImLZaH9XrSLiXyLiHc36/kokHSrpG5IelPSIpNsl/b2k2Xn40CHTd0v61/w5JD2nwjIHJe+8Xd4v6RmF2DskXV8YDklP5O2i//WhPG7EbSYn3LV5mg2Svj5qK6lEkqZIukjSJkmPSbpL0vn960rJByXdI+kPktZL+oSkiYVlfFDSHXn+tZI+WFZ5I2J2RFy/A/M3dR+sZEwnhVZT7YgZ+HpE7A7sB/wQ+EbjSmX9JB0C3ATcB7wgIp4JnAx0Ar8BPg1cJEl5+tOBA4Hzt+PrxgNnjzDNiyJi98Lrk4VxVbeZfOT5FmBunqYT6N6OMjaUpH2AG4HdgCMjYg/gdcBewCF5ss8D84G3AnsAfwW8FlhRXFQevzdwLPBuSfMa8CeMDRExZl/AOtKOMTR+NLBhyHQfAG4HHgG+DuxaGH88cBvwMPAz4IWFcecAvwYeA1YDJxXGvQ24Afgc8Dvg4xXKch5waWF4FhDA5Dz8TOAiYBPph+njQEdh+T8tzHsh6QftUWAl8Oc5fizwFPAn4HHglzl+PfCO/Hkc8A/AvcADwFeAZ+ZxM3KZTgXWAw8C5xa+9wigJ3/v/cBna5xv4G8vTDsf2Jj/3vfX+H+ekP8/78nDHXm9f7TO7eVS4L+GGT8euBU4C9g//z2vLIwP4DkV5hv6f1qXt5vfAXvl2DuA60daVo3bzL8DF9T4N58DfHNI7ELg84Wy/w9p+14LdFVYxp8BTwL7FmIvBXqBXepY/x8HfgWMqzJ+JtAHHDEkfhCwGXhtlfk+D/xbYfh5wDV5/d8NvLEw7hJgMfA90r5yQ/77LgB+D9wFvLjSbwzV94Nd87b1EOk35BfA/o3YB7fn1dAf6Ua/qC8p3AwcAOwD3Am8K497Sf4HvZz0Y3Nqnn5iHn9ynm8c8CbgCWBKYYfaAryH9IOyW4WynMfWH8YJwCfyP3x8jv0n8EXgGcCzcjnPKCy/+GNzCrBv/q73A78lJzeG/JBU2CBPA9YAzwZ2B74NfHXIBvkl0lHci0g74fPz+BuBt+TPuwOvqHG+4t/eP+1l+W99AelHpX+HexXw8DD/68NIO+3zgXOBn7M1ef4taWes9pqWp/st8PYRtqkXk35MrmHIDy/1JYW5eR1/PMe2KylQeZs5JZfxg6SzhI5h/p7ppB/0PfNwBykhvyL/Hx4FnpvHTQFmV1nOVcCZheHPkX+I+/93w7xelaf7OXD+MGV9F3BvlXE/Av61QlykRN6/Pz+DdOD0dtJ+8pK87mbn8Zfk4ZeSfsyvIyXDt+Z183Hgh5V+Y6i+H5wB/D9gUl7GSwvr+3pK3Ae363dze2fcGV7UlxROKQx/EvhC/rwE+Och898NvLrKd94GnJg/vw1YP0IZzyMdxT9MOgp6CDg6j9s//+N3K0z/5v6NkiE/NhWW/XtSFUT/9wyXFLqBBYVxzyWdWYwvbJBTC+NvBublzz8mVaHsN2T5I803UKbCtM8b8n+4qI7/9/tJR3K/B2Zux/byJ+DYGqb7FLABmDQkXm9SOIx0ZjqZyknhUQb/eB4z0jZTmL8LuJZ0kPIQcM4wf89Pgbfmz68Dfp0/PyN/x/+mwgHNkGW8Cbghf+4gJdgjhpunwjLuIf94Vxn/D8DPq4y7HPhShfj5wC/ZehD3JuAnQ6b5IvCx/PmS4nJIB3R3FoZfQOHghMFJodp+cBpDahgatQ9uz8vXFLb6beHzk6RsC+lI6v35gt7Dkh4mna4eACDprZJuK4w7jFTP2+++Gr57RUTsRUoCd5COJPq/exdgU2H5XySdMWxD0vsl3ZkviD5Mqnrar9K0FRxAOm3tdy9pY9y/EKu2jk4HDgXukvQLSccPWXa1+Soprq97c7lqtYy081wVEffUMV+/h0hHwyNZBayLiCe34zsGRMQdwJWkKpxKXhIRexVeVxfGVdtm+pe9PCLmkurj3wX8k6RjqnzP10gHG5DOqr6Wl/EE6Uf0XaRt8L8kPa/KMr4LzJL0bFJieSQibq4ybTUjrf8Hhxk/JY8fIOndpCP810fE5hyeDrx8yP7cRaoi6nd/4fMfKgxX236r7QdfBa4GLpe0UdInJe1SYf4y98GaOSmM7D5g0ZCdc1JEXCZpOul07t2k+tS9SDuoCvNHrV8UEQ+STjXPkzQlf/dmUvbv/+49I2L20Hkl/TnwYeCNwN65LI8UyjJSOTaSdph+00hVX/dXnnxQue+JiDeTktX/Ab5ZvLOmTgcNKcPGOuZdTPqRPUbSq/qDkrqG3MUz9DUtT3ot6ai4kT4GvJN0wbpuFbaZoeP/FBHfIF0vO6zKYr4BHC1pKnASOSnk+a+OiNeRfnTvIm3vlcrxR9LF3i7SRe6v9o9TugV8uPX/53nSa4GTJFX7XboOOEjSEcWgpINI1V3dhdhppGQ7JyI2FCa/D/jRkP1594g4s8p31qzafpD/B+dHxCzglaRrlG+tsIiW2AfbISnsImnXwqvaHUDVfAl4l6SX59vhniHp9ZL2IJ1eB6nuG0lvp/qOV5OIuIt0VPGhiNgE/AD4jKQ9JY2TdIikV1eYdQ/SBtQLjJf0UWDPwvj7gRnD7HCXAX8n6WBJuwP/QrrDZctIZZZ0iqTJEfE0qboBUrXG9vhHSZMkzSbV+9Z0K6Wkt5COlt8GvBdYlv+O/qPm3Yd5rc+L+RjwSkmfkvRnebnPkXSppL1qLP+EIdtbx3ATR8Sa/De+t8blV1rGwDaTy/y2/m00bzN/Bcwm3VlVaf5eUjXGfwBrI+LOvJz9JZ2Qf1w2ky68Dvd//Qpp/Z9AurDav/yfjLD+f5In/Sxpm12WD7iQdKCkz0p6YUT8N/AFYLmkV0jqyNvJt4BrI+LaPE8Xaft9XUT8z5AyXgkcKuktknbJr5dJev4Iq3lE1fYDSa+R9IK8LTxKqhKqtB5bYh9sh6RwFemUr/91Xj0zR0QP6Uju30l11WtIGz4RsRr4DOkiz/2k+sYbRqHMnwLmS3oW6YhiAunOpt8D36TyKfTVpDsm/pt02vlHBlfF9N+y+JCkWyrMfzHp6O7HpAtrfyTVp9biWGCVpMdJd67My0eO2+NHpHXcDXw6In4AW482K82Qj/QvINWLPx4RXyPdifG5er44In4NHEmqglol6RHSD04P6e6bWqxi8Pb29hrm+SfSAcZQvxxyRH3BMMsobjOPAh8h3aXyMOnazJkRMdyDjl8jXef4WiE2jnSdZiPpwvWrgQXVFhARNwBPA7dExLphvqva/L8jHUn/CbhJ0mOk7eAR0jYB6az8y6Sk8zjwfVJCK57hfZx0w8UvCuvuC/k7HgP+EpiX/67fko6sJ7Ljqu0Hf0babx8l3cTyIwpJs6Al9kHlixRmTSVpBmlH2KWWIyNrTZKuA74WEX5SfSdVb1WKmVlFkl5GusXzxGaXxbZfO1QfmVnJJC0jXSh+X66isZ2Uq4/MzGyAzxTMzGzATn1NYb/99osZM2Y0uxhmZjuVlStXPhgRkyuNKzUpSFpHupWvD9gSEZ1KLSF+nXTb3zpSY1S/z9MvJD2Z1we8d8gTnNuYMWMGPT09pZXfzGwsknRvtXGNqD56TUQcHhGdefgcoDsiZpLuQT4HQNIs0r3Ds0n33C4e6cEfMzMbXc24pnAiqY0a8vsbCvHLI2JzRKwlPaxyxLazm5lZWcpOCgH8QNJKSfNzbP/cfAP5vb9xtwMZ/ATuBiq0ByNpvqQeST29vb0lFt3MrP2UfaH5qIjYmB+9v0bSXcNMqwqxbe6XjYilwFKAzs5O309rZjaKSj1TiIiN+f0B4Duk6qD7+1tzzO8P5Mk3MLiFzKnU10KmmZntoNKSQm5NdI/+z6RGqO4AriD1XkZ+/27+fAUwT9JESQeTut6rtz12Mxtjli+HGTNg3Lj0vnx5s0s0tpVZfbQ/8B2lPs7HkxrJ+r6kXwArlDo9X0/qzpKIWCVpBak10C3AWRGxvc0vm9kYsHw5zJ8PT+bujO69Nw0DdHU1r1xj2U7dzEVnZ2f4OQWzsWvGjJQIhpo+Hdata3Rpxg5JKwuPCQziZi7MrGWtX19f3Hack4KZtaxp0+qL245zUjCzlrVoEUyaNDg2aVKKWzmcFMysZXV1wdKl6RqClN6XLvVF5jLt1K2kmtnY19XlJNBIPlMwM7MBTgpmZjbAScHMzAY4KZiZ2QAnBTMzG+CkYGZmA5wUzMxsgJOCmZkNcFIwM7MBTgpmZjbAScHMzAY4KZiZ2YDSk4KkDkm3SroyD58n6TeSbsuv4wrTLpS0RtLdko4pu2xmZjZYI1pJPRu4E9izEPtcRHy6OJGkWcA8YDZwAHCtpEPdT7OZWeOUeqYgaSrweuDLNUx+InB5RGyOiLXAGuCIMstnZmaDlV19dAHwIeDpIfF3S7pd0sWS9s6xA4H7CtNsyLFBJM2X1COpp7e3t4wym5m1rdKSgqTjgQciYuWQUUuAQ4DDgU3AZ/pnqbCY2CYQsTQiOiOic/LkyaNYYjMzK/OawlHACflC8q7AnpIujYhT+ieQ9CXgyjy4ATioMP9UYGOJ5TMzsyFKO1OIiIURMTUiZpAuIF8XEadImlKY7CTgjvz5CmCepImSDgZmAjeXVT4zM9tWM55T+KSkX0m6HXgN8HcAEbEKWAGsBr4PnOU7j6xdLV8OM2bAuHHpffnyZpfI2oUitqm232l0dnZGT09Ps4thNqqWL4e3vhWeLtyeMW4cfOUr7sDeRoeklRHRWWmcn2g2azFnnDE4IUAaPuOM5pTH2ouTglmLeeKJ+uJmo8lJwczMBjgpmJnZACcFMzMb4KRg1mLOPLO+uNloclIwazGLF8OcOYNjc+akuFnZz7A4KZi1mOXL4brrBseuu84PsFnaBubPh3vvhYj0Pn/+6G4bfnjNrMVMnAhPPbVtfMIE2Ly58eWx1jFjRkoEQ02fDuvW1b4cP7xmthOplBCGi1v7WL++vvj2cFIwM9tJTJtWX3x7OCmYme0kFi2CSZMGxyZNSvHR4qRgZi1twQIYPx6k9L5gQbNL1DxdXbB0abqGIKX3pUtHt6HEMjvZMTPbIQsWwJIlW4f7+rYOt+stul1d5baW6zMFM2tZS5fWF7cd56RgZi2rr0o3W9XituOcFMysZXV01Be3HVd6UpDUIelWSVfm4X0kXSPpnvy+d2HahZLWSLpb0jFll83MWtv8+fXFbcc14kzhbODOwvA5QHdEzAS68zCSZgHzgNnAscBiST4esLYzcWJ98bHsqKPSHUdF48enuJWj1KQgaSrweuDLhfCJwLL8eRnwhkL88ojYHBFrgTXAEWWWz6wVVWvKoh2buDj3XNiyZXBsy5YUt3KUfaZwAfAhoNjj7P4RsQkgvz8rxw8E7itMtyHHBpE0X1KPpJ7e3t5SCm3WTOOq7JXV4mNZI5p1sMFK28wkHQ88EBEra52lQmyb1voiYmlEdEZE5+TJk3eojGat6Omn64uPZY1o1mFnM3t2enCt/zV79uguv8xjj6OAEyStAy4HXivpUuB+SVMA8vsDefoNwEGF+acCG0ssn5m1uEY067AzmT0bVq8eHFu9enQTQ2lJISIWRsTUiJhBuoB8XUScAlwBnJonOxX4bv58BTBP0kRJBwMzgZvLKp9Zq9p33/riY1lXFxx55ODYkUeW+0RvKxuaEEaKb49m1FJ+AnidpHuA1+VhImIVsAJYDXwfOCsi/IiKtZ0LL9z2+sG4cSnebhYsgO7uwbHu7vZu/6hsDUkKEXF9RByfPz8UEXMiYmZ+/11hukURcUhEPDcivteIspm1Imn44XbhZi4arw3vZzBrbWefvW0zDn19Kd5u3MzFYLNm1RffHk4KZi3moYfqi49lbuZisFWrYLfdBsd22y3FR4uTgpm1LDdzMdjcufCHPwyO/eEPKT5a3J+CmbWs/j4Tli5NVUYdHSkhtGtfCkMvuo8U3x5OCmbW0hYvbt8k0AyuPjIzswFOCmZmO4k5c+qLbw8nBTOzncS1126bAObMSfHR4qRgZrYTOfTQrbfkdnSk4dHkC81mZjuJBQtgyZKtw319W4dH62K8zxTMzHYSjWj2w0nBzFra8uUwY0ZqFHDGjDTcrhrR7Ierj8ysZS1fnh5We/LJNHzvvVufZm7H5rPHjavc2dJo9srnMwUza1nnnrs1IfR78sn27aO5Eb3yOSmYWctyH82N56RgZi3LfTQ3npOCmbWs5zynvrjtuNKSgqRdJd0s6ZeSVkk6P8fPk/QbSbfl13GFeRZKWiPpbknHlFU2M9s5XH99fXHbcWXefbQZeG1EPC5pF+Cnkvq72PxcRHy6OLGkWcA8YDZwAHCtpEPdT7NZ+3LPa4N1dFT+20ez06HSzhQieTwP7pJfMcwsJwKXR8TmiFgLrAGOKKt81loWLIDx41NfxOPHu2N2S9zz2mCN6HSo1GsKkjok3QY8AFwTETflUe+WdLukiyXtnWMHAvcVZt+QY0OXOV9Sj6Se3t7eMotvDdL/6H7/EVD/o/tODOae1wZbvBjOPHNw20dnnjm6/U0oYriD91H6Emkv4DvAe4Be4EHSWcM/A1Mi4jRJ/xe4MSIuzfNcBFwVEd+qttzOzs7o6ekpu/hWsvHjq58Sb9nS+PI0m1R9XAN215azYIF7XhttklZGRGelcQ25+ygiHgauB46NiPsjoi8inga+xNYqog3AQYXZpgIbG1E+ay7XG9twFi9OBwcR6d0JoVxl3n00OZ8hIGk3YC5wl6QphclOAu7In68A5kmaKOlgYCZwc1nls9bhemOz1lHm3UdTgGWSOkjJZ0VEXCnpq5IOJ1UfrQPOAIiIVZJWAKuBLcBZvvOoPcyfP7g54GLczBqrIdcUyuJrCmPH3LnQ3b11eLR7k9qZ+JqCla3p1xTMhrN8Odx44+DYjTe2dxPJZs3ipGBN55YwzVpHTdcUJE0G3gnMKM4TEaeVUyxrJ24J06x11Hqh+bvAT4BrAV/8tVE1bVrqPKVS3Mwaq9akMCkiPlxqSaxtHXdc5buPjjtu25iZlavWawpXFlszNRtNV11VX9zMylNrUjiblBj+KOmx/Hq0zIJZ+6hUdTRc3MzKU1P1UUTsUXZBzMys+Wp+olnSCcBf5MHrI+LKcopkZmbNUlP1kaRPkKqQVufX2TlmZmZjSK1nCscBh+eWTZG0DLgVOKesgpmZWePV80TzXoXPzxzlcpiZWQuo9UzhX4FbJf0QEOnawsLSSmVmZk1R691Hl0m6HngZKSl8OCJ+W2bBzMys8YatPpL0vPz+ElL/CBtI/SgfkGNmZjaGjHSm8PfAfOAzFcYF8NpRL5GZmTXNsEkhIubn99c0pjhmZtZMtT6ncLKkPfLnf5D0bUkvHmGeXSXdLOmXklZJOj/H95F0jaR78vvehXkWSloj6W5Jx+zIH2ZmZvWr9ZbUf4yIxyS9CjgGWAZ8YYR5NgOvjYgXAYcDx0p6BenZhu6ImAl052EkzQLmAbOBY4HFuX9nMzNrkFqTQn8fCq8HlkTEd4EJw80QyeN5cJf8CuBEUlIhv78hfz4RuDwiNkfEWmANcESN5TMzs1FQa1L4jaQvAm8ErpI0sZZ5JXVIug14ALgmIm4C9o+ITQD5/Vl58gNJdzb125BjQ5c5X1KPpJ7e3t4ai29mZrWoNSm8EbgaODYiHgb2AT440kwR0RcRhwNTgSMkHTbM5Kq0iArLXBoRnRHROXny5FrKbmZmNao1KUwB/isi7pF0NHAycHOtX5ITyfWkawX3S5oCkN8fyJNtAA4qzDYV2Fjrd5iZ2Y6rNSl8C+iT9BzgIuBg4GvDzSBpsqS98ufdgLnAXcAVwKl5slNJ/T+T4/MkTZR0MDCTOhLPzmbuXJC2vubObXaJzMxqb/vo6YjYIumvgQsi4t8k3TrCPFOAZfkOonHAioi4UtKNwApJpwPrSWcdRMQqSStITXNvAc6KiL4qy96pzZ0L3d2DY93dKX7ttc0pk5kZgCK2qbbfdiLpJuAC4Fzgf0XEWkl3RMRw1whK19nZGT09Pc0swnZRpasnWQ3/jjHH62Mwrw8rm6SVEdFZaVyt1UdvB44EFuWEcDBw6WgV0MzMWkOtraSuBt5bGF4LuOc1M7MxZtikIGlFRLxR0q8YfHuoSM+nvbDU0pmZWUONdKZwdn4/vuyCmJlZ843USmr/k8f3Akjac6R5bGQdHdBX4b6qDrf0ZGZNVmsrqWdIuh+4HViZXzvfbT8tYv78+uJmZo1S61H/B4DZEfFgmYUxM7PmqvWW1F8DT5ZZkHbyhSqNjleLm5k1Sq1nCguBn+WH2Db3ByPivdVnsWqqPYDkB5PMrNlqTQpfBK4DfgU8XV5xzMysmWpNClsi4u9LLYmZmTVdrdcUfpg7t5mS+1jeR9I+pZbMzMwartYzhb/N7wsLsQCePbrFMTOzZqq17aODyy6ImZk137DVR5I+VPh88pBx/1JWoczMrDlGuqYwr/B54ZBxx45yWczMrMlGSgqq8rnSsJmZ7eRGSgpR5XOl4UEkHSTph5LulLRK0tk5fp6k30i6Lb+OK8yzUNIaSXdLOqauv8RsjNh33/riZqNppAvNL5L0KOmsYLf8mTy86wjzbgHeHxG3SNoDWCnpmjzucxHx6eLEkmaRqqtmAwcA10o6dKz202xWzYUXwmmnwVNPbY1NmJDiZmUb9kwhIjoiYs+I2CMixufP/cO7jDDvpoi4JX9+DLgTOHCYWU4ELo+IzblntzXAEfX9OWY7v64uOP30rU2pd3Sk4a6u5pbL2kOtD6/tEEkzgBcDN+XQuyXdLuliSXvn2IHAfYXZNlAhieSH6Hok9fT29pZZbLOmWL4cli3b2udGX18aXr68ueWy9lB6UpC0O/At4H0R8SiwBDgEOBzYBHymf9IKs29z3SIilkZEZ0R0Tp48uZxCmzXRuefCk0PaJH7yyRQ3K1upSUHSLqSEsDwivg0QEfdHRF9EPA18ia1VRBuAgwqzTwU2llk+s1a0fn19cbPRVFpSkCTgIuDOiPhsIT6lMNlJwB358xXAPEkTJR0MzARuLqt8Zq1q2rT64majqcz+lo8C3gL8StJtOfYR4M2SDidVDa0DzgCIiFWSVgCrSXcuneU7j6wdLVqUumYtViFNmpTiZmUrLSlExE+pfJ3gqmHmWQR407e21n+X0bnnpiqjadNSQvDdR9YIDbn7yFrXggUwfjxI6X3BgmaXyCAlgHXr4Omn07sTgjVKmdVH1uIWLIAlS7YO9/VtHV68uDllMrPm8plCG1u6tL64mY19TgptrK/KZfxqcTMb+5wU2lh/Mwq1xs1s7HNSaGPPfW59cTMb+5wU2tjq1fXFzWzsc1IwM7MBTgpmZjbAScHMzAY4KZiZ2QAnBTMzG+CkYGZmA5wU2ti++9YXN7Oxz0mhjV14IUyYMDg2YUKKm1l7clJoY11dcPHFMH16ajp7+vQ07GaazdqXm85uc11dzU8CEybAU09VjptZY5XZR/NBkn4o6U5JqySdneP7SLpG0j35fe/CPAslrZF0t6RjyiqbtZbTT68vbmblKbP6aAvw/oh4PvAK4CxJs4BzgO6ImAl052HyuHnAbOBYYLEkt9fZBq6q0kFrtbiZlae0pBARmyLilvz5MeBO4EDgRGBZnmwZ8Ib8+UTg8ojYHBFrgTXAEWWVz1rH+vX1xc2sPA250CxpBvBi4CZg/4jYBClxAM/Kkx0I3FeYbUOODV3WfEk9knp6e3tLLbc1xrRp9cXNrDylJwVJuwPfAt4XEY8ON2mFWGwTiFgaEZ0R0Tl58uTRKqY10aJFMGnS4NikSSluZo1ValKQtAspISyPiG/n8P2SpuTxU4AHcnwDcFBh9qnAxjLLZ62hqwuOPHJw7Mgjm39XlFk7KvPuIwEXAXdGxGcLo64ATs2fTwW+W4jPkzRR0sHATODmsspnrWPBAujuHhzr7k5xM2ssRWxTQzM6C5ZeBfwE+BXwdA5/hHRdYQUwDVgPnBwRv8vznAucRrpz6X0R8b3hvqOzszN6enpKKX+ZVKmiLCvp39HSvD7MGkvSyojorDSutIfXIuKnVL5OADCnyjyLANckm5k1iZu5MDOzAU4KZmY2wEnBmm5OxcrE6nEzK4+TgjXdtddumwDmzElxM2ssJwVrCYceCh25pauOjjRsZo3nprOt6RYsgCVLtg739W0dXry4OWUya1c+U7CmW7q0vriZlcdJwZqur6++uJmVx0nBzMwGOCmYmdkAJwVruunT64ubWXmcFKzp3J+CWetwUrCm6+pKdxpNn55aTJ0+PQ27PwWzxvNzCtYSurqcBMxagc8UzMxsgJOCmZkNcFIwM7MBZfbRfLGkByTdUYidJ+k3km7Lr+MK4xZKWiPpbknHlFUuMzOrrswzhUuAYyvEPxcRh+fXVQCSZgHzgNl5nsWSOkosm5mZVVBaUoiIHwO/q3HyE4HLI2JzRKwF1gBHlFW2uXPTrY/9r7lzy/omM7OdSzOuKbxb0u25emnvHDsQuK8wzYYc24ak+ZJ6JPX09vbW/eVz50J39+BYd3djE0NHlXOganEzs0ZpdFJYAhwCHA5sAj6T46owbVRaQEQsjYjOiOicPHly3QUYmhBGipdh//3ri5uZNUpDk0JE3B8RfRHxNPAltlYRbQAOKkw6FdjYyLI10sYqf1m1uJlZozQ0KUiaUhg8Cei/M+kKYJ6kiZIOBmYCNzeybGZmVmIzF5IuA44G9pO0AfgYcLSkw0lVQ+uAMwAiYpWkFcBqYAtwVkSU0sXKrFmwenXluJlZuystKUTEmyuELxpm+kVA6e1iPvFEfXEzs3bSdk80r19fX9zMrJ20XVKYNq2+uJlZO2m7pNAKHbr4OQUza1VtlxRaoUOX3XarL25m1iht2clOszt0efzx+uJmZo3SdmcKZmZWnZOCmZkNcFIwM7MBTgpmZjbASaEJdt+9vriZWaM4KTTBF74A44fc9zV+fIqbmTWTk0ITdHXBJZcMflbikkuae5usmRk4KTTNDTfAhg0Qkd5vuKHZJTIza9OH15ptwQJYsmTrcF/f1uHFi5tTJjMz8JlCU1S7duBrCmbWbE4KTRAVe5+uHjczaxQnBTMzG1BaUpB0saQHJN1RiO0j6RpJ9+T3vQvjFkpaI+luSceUVa5W4OcUzKxVlXmmcAlw7JDYOUB3RMwEuvMwkmYB84DZeZ7FksZs7wJ+TsHMWlVpSSEifgz8bkj4RGBZ/rwMeEMhfnlEbI6ItcAa4IiyytZsfk7BzFpVo29J3T8iNgFExCZJz8rxA4GfF6bbkGPbkDQfmA8wbSfuQ7PZfTqYmVXSKheaVSFW8V6ciFgaEZ0R0Tl58uSSi2Vm1l4anRTulzQFIL8/kOMbgIMK000FNja4bGZmba/RSeEK4NT8+VTgu4X4PEkTJR0MzARubnDZzMzaXmnXFCRdBhwN7CdpA/Ax4BPACkmnA+uBkwEiYpWkFcBqYAtwVkT0lVU2MzOrrLSkEBFvrjJqTpXpFwGLyiqPmZmNTLETt60gqRe4t9nl2EH7AQ82uxAtxOtjMK+PrbwuBtuR9TE9IireqbNTJ4WxQFJPRHQ2uxytwutjMK+PrbwuBitrfbTKLalmZtYCnBTMzGyAk0LzLW12AVqM18dgXh9beV0MVsr68DUFMzMb4DMFMzMb4KRgZmYDnBSaTFKHpFslXdnssjSbpL0kfVPSXZLulHRks8vULJL+TtIqSXdIukzSrs0uUyPV20nXWFdlfXwq7yu3S/qOpL1G47ucFJrvbODOZheiRVwIfD8inge8iDZdL5IOBN4LdEbEYUAHqROqdnIJNXbS1SYuYdv1cQ1wWES8EPhvYOFofJGTQhNJmgq8Hvhys8vSbJL2BP4CuAggIp6KiIebWqjmGg/sJmk8MIk2azW4zk66xrxK6yMifhARW/Lgz0mtS+8wJ4XmugD4EPB0k8vRCp4N9AL/kavTvizpGc0uVDNExG+AT5MajdwEPBIRP2huqVrCoE66gGeNMH07OQ343mgsyEmhSSQdDzwQESubXZYWMR54CbAkIl4MPEF7VQ8MyHXlJwIHAwcAz5B0SnNLZa1K0rmk1qWXj8bynBSa5yjgBEnrgMuB10q6tLlFaqoNwIaIuCkPf5OUJNrRXGBtRPRGxJ+AbwOvbHKZWkG1TrralqRTgeOBrhilh86cFJokIhZGxNSImEG6iHhdRLTt0WBE/Ba4T9Jzc2gOqX+NdrQeeIWkSZJEWhdtedF9iGqddLUlSccCHwZOiIgnR2u5pfWnYLYd3gMslzQB+B/g7U0uT1NExE2SvgncQqoWuJU2a+Khnk662kGV9bEQmAhck44d+HlEvGuHv8vNXJiZWT9XH5mZ2QAnBTMzG+CkYGZmA5wUzMxsgJOCmZkNcFKwtiGpT9Jthdd2PzEt6WejWbYhy+6U9Pmylm82HN+Sam1D0uMRsXuzy2HWynymYG1P0jpJ50u6RdKvJD0vxyfndvtvkfRFSfdK2i+Pezy/Hy3p+kI/EMvzU8hIeqmkH0laKenq/iYahnz3ybnPhF9K+nFhmVfmz1cVzmwekXRq7oPjU5J+kdvSP6NR68rGPicFaye7Dak+elNh3IMR8RJgCfCBHPsYqfmRlwDfAaZVWe6LgfcBs0itvR4laRfg34C/iYiXAhcDiyrM+1HgmIh4EXDC0JERcVxEHA6cDtwL/Gf+/EhEvAx4GfBOSQfXuA7MhuVmLqyd/CH/wFby7fy+Evjr/PlVwEkAEfF9Sb+vMu/NEbEBQNJtwAzgYeAwtjZB0EFqBnuoG4BLJK0olGGQfHbyVeCNEfGIpL8EXijpb/IkzwRmAmurlM+sZk4KZsnm/N7H1v1Cdc5bnF/AqogYtkvRiHiXpJeTOlu6TdLhxfGSOkit6P5TRPR3xSjgPRFxdY3lM6uZq4/Mqvsp8EaAfHReT5/AdwOT+/uZlrSLpNlDJ5J0SETcFBEfBR4EDhoyySeA2yPi8kLsauDMXEWFpEPbtUMiG30+U7B2sluu3un3/YgY7rbU84HL8rWHH5Gqfx6r5Ysi4qlcvfN5Sc8k7WsXAKuGTPopSTNJR//dwC+BVxfGfwBYVSj3R0ndt84AbskXtXtpo64prVy+JdWsCkkTgb6I2JKP+JcMc03CbEzwmYJZddNI7fePA54C3tnk8piVzmcKZmY2wBeazcxsgJOCmZkNcFIwM7MBTgpmZjbAScHMzAb8f+4JG66OUdDKAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(cdf.CYLINDERS,\n",
    "            cdf.CO2EMISSIONS,\n",
    "            color='blue')\n",
    "plt.xlabel(\"Engine size\")\n",
    "plt.ylabel(\"Emission\")\n",
    "plt.title('Linear Relationship: x=CYLINERS vs y=CO2emissions')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df750e5f-d905-49fe-a3d1-dd8b667080fc",
   "metadata": {},
   "source": [
    "_____\n",
    "# [2] Data Preprocessing \n",
    "**NOTE:** As this is already a refined dataset we skip steps\n",
    "- Cleaning\n",
    "- Missing data\n",
    "- Scaling\n",
    "_____"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a14e3f3-2923-4504-a9cc-6ce0037abe79",
   "metadata": {},
   "source": [
    "# [3] Creating train and test dataset\n",
    "Train/Test Split involves splitting the dataset into training and testing sets that are mutually exclusive. After which, you train with the training set and test with the testing set. \n",
    "This will provide a more accurate evaluation on out-of-sample accuracy because the testing dataset is not part of the dataset that have been used to train the model. Therefore, it gives us a better understanding of how well our model generalizes on new data.\n",
    "\n",
    "This means that we know the outcome of each data point in the testing dataset, making it great to test with! Since this data has not been used to train the model, the model has no knowledge of the outcome of these data points. So, in essence, it is truly an out-of-sample testing.\n",
    "\n",
    "Let's split our dataset into train and test sets. `80% of the entire dataset will be used for training and 20% for testing`. We create a mask to select random rows using __np.random.rand()__ function: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "dab932da-d16e-4273-b979-bc2be7288038",
   "metadata": {},
   "outputs": [],
   "source": [
    "msk = np.random.rand(len(df)) < 0.8\n",
    "train = cdf[msk]\n",
    "test = cdf[~msk]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6cbe89f3-db23-42b5-b578-549e659d6042",
   "metadata": {},
   "source": [
    "_______\n",
    "# [4] Model Selection\n",
    "\n",
    "### Simple Regression Model\n",
    "Linear Regression fits a linear model with coefficients B = (B1, ..., Bn) to minimize the 'residual sum of squares' between the actual value y in the dataset, and the predicted value yhat using linear approximation. \n",
    "\n",
    "### Multiple Regression Model\n",
    "In reality, there are multiple variables that impact the co2emission. When more than one independent variable is present, the process is called multiple linear regression. An example of multiple linear regression is predicting co2emission using the features FUELCONSUMPTION_COMB, EngineSize and Cylinders of cars. The good thing here is that multiple linear regression model is the extension of the simple linear regression model.\n",
    "_______"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cfa28ab8-c189-4365-b56f-52c8b00844f4",
   "metadata": {},
   "source": [
    "# [5] Model Training\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4b7ec2da-4079-454f-9ef2-651c74719d35",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEHCAYAAABBW1qbAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAAvwklEQVR4nO2df7RdZXnnP8+9uUFuogaSyCSEJAwTaW/UoqSoQ9tBAkKRBbRTmThXVpawemmCbbR1OaaZqdo16TD2l3TWJG0GgnfMrZRRO7IQQYioY2vFgIgkSEmHAIGMJAhKxBITnvlj73Ozz7l7n/3j7H32ued+P2vtdfZ+9373fs5J7vvs93mfH+buCCGEEAADdQsghBCid5BSEEIIMYmUghBCiEmkFIQQQkwipSCEEGISKQUhhBCTzKry5ma2D3gROAYcdfdVZnYy8DfAcmAfcKW7Px9evxG4Jrz+d9z9rnb3X7BggS9fvrwq8YUQoi+5//77D7n7wrhzlSqFkHe4+6HI8UeAne5+vZl9JDz+D2Y2AqwBVgKLgXvM7PXufizpxsuXL2fXrl1Vyi6EEH2HmT2RdK4O89HlwHi4Pw5cEWm/xd1fdvfHgb3AOd0XTwghZi5VKwUHvmxm95vZWNh2irsfAAg/Xxe2nwo8Fem7P2wTQgjRJao2H53r7s+Y2euAu83s+22utZi2KTk4QuUyBrB06dJypBRCCAFUPFNw92fCz2eBvyUwB/3AzBYBhJ/PhpfvB06LdF8CPBNzz23uvsrdVy1cGLtOIoQQoiCVKQUzm2Nmr27sA+8EHgZuA9aGl60FvhDu3wasMbMTzOx0YAVwX1XyCSGEmEqVM4VTgG+Y2XcJBvcvuvudwPXAhWb2GHBheIy77wZuBfYAdwLXtfM8EkLMLCYmYPlyGBgIPicm6paoP7HpnDp71apVLpdUIfqfiQkYG4OXXjreNjwM27bB6Gh9ck1XzOx+d18Vd04RzUKInmfTpmaFAMHxpk31yNPPSCkIIXqeJ5/M1y6KI6UghOh5krzP5ZVePlIKQoieZ/PmYA0hyvBw0C7KRUpBCNHzjI4Gi8rLloFZ8KlF5mroRkI8IYTomNFRKYFuoJmCEEKISaQUhBBCTCKlIIQQYhIpBSGEEJNIKQghhJhESkEIIcQkUgpCCCEmkVIQQggxiZSCEEKISaQUhBBCTCKlIIQQYpLKlYKZDZrZd8zs9vD4Y2b2tJk9GG6XRK7daGZ7zexRM7uoatmEEEI0042EeBuAR4DXRNr+3N3/JHqRmY0Aa4CVwGLgHjN7veo0CyFE96h0pmBmS4B3ATdmuPxy4BZ3f9ndHwf2AudUKZ8QQohmqjYffRL4MPBKS/v7zewhM9tuZieFbacCT0Wu2R+2CSGE6BKVKQUzuxR41t3vbzm1FTgDOAs4APxpo0vMbTzmvmNmtsvMdh08eLBEiYUQQlQ5UzgXuMzM9gG3AOeb2Q53/4G7H3P3V4D/wXET0X7gtEj/JcAzrTd1923uvsrdVy1cuLBC8YUQYuZRmVJw943uvsTdlxMsIH/F3d9rZosil/0a8HC4fxuwxsxOMLPTgRXAfVXJJ4QQYip1lOP8hJmdRWAa2gdcC+Duu83sVmAPcBS4Tp5HQgjRXboSvObuX3X3S8P9q9z9je7+Jne/zN0PRK7b7O5nuPuZ7v6lbsgmhJgeTEzA8uUwMBB8TkzULVF/oohmIUQqdQ/IExMwNgZPPAHuwefYmBRDFUgpCCHaMjEBV1/dPCBffXV3B+RNm+Cll5rbXnopaBflIqUghGjLhg1w5Ehz25EjQXu3ePLJfO2iOFIKQoi2PPdcvvYqWLo0X7sojpSCEKLn2bwZhoeb24aHg3ZRLlIKQoi2zJ+fr70KRkdh2zZYtgzMgs9t24J2US5SCkKIttxwAwwNNbcNDQXt3WR0FPbtg1deCT6lEKpBSkGIPqBKl9HRUbj55ua39Jtv7nxQrtvNVcQjpSBExVQ9+MX58L/vfbBgQXnPLPstXXEHvYu5T0lEOm1YtWqV79q1q24xhEikMfhFfeyHh8u1hy9fHgyq7Sj7mZ2SJPOyZYHSEdViZve7+6rYc1IKQlRHNwa/gYHgbTuNXhpwk2Q2C2YjolraKQWZj4SokG4EXWX11e/kmWkmsLwmMsUd9C5SCkJUyJw5+dqLEOfDH0fRAXdiAtaubbb/r117fOAvsj6guIPeRUpBiAr5yU/ytcexfj3MmhWYVmbNCo6jtPrwz58Ps2c3X9PJgHvttXCsJYn9sWNBOxTLS6S4g95FSkHMaNIG3E5JsvVnXcpbvx62bj0+KB87FhzHKYaGd9ChQ3DNNTA4GJwbHAze7IsOuGmKraiJTHEHvYmUgpixZB1wO6ExMGdtb2XbtnztEJhtxsebv9f4eHXunlof6C+kFMSMpciAm5exsXztrbSabdLaofw00wMJo0SjXesD/UXlSsHMBs3sO2Z2e3h8spndbWaPhZ8nRa7daGZ7zexRM7uoatnEzKbIgJuXLVtg3bpmU866dUF7ForMNMr2eGqsHSS1j44G5qmyzFWiXroxU9gAPBI5/giw091XADvDY8xsBFgDrAQuBraYWcZJthD56dS0k5UtW+Do0WAd4ejR7AoBis00yjbnpCm2bpurRLVUqhTMbAnwLuDGSPPlwHi4Pw5cEWm/xd1fdvfHgb3AOVXKJ2Y2nZp2ukGRmUacOWdoCA4fLp72op1iU1W0/qLqmcIngQ8D0RjFU9z9AED4+bqw/VTgqch1+8M2ISqhU9NOt8gy04gGj23aFJhvoi6qZkFRnCryDKkqWn9RmVIws0uBZ939/qxdYtqmOO6Z2ZiZ7TKzXQcPHuxIRiE6Me30CnHBY+PjwYzhlVdg7typ5TTLfJOX91F/UeVM4VzgMjPbB9wCnG9mO4AfmNkigPDz2fD6/cBpkf5LgGdab+ru29x9lbuvWrhwYYXiCzE9SDPfVP0mX5X30QUXBDOcxnbBBZ3dT2SjMqXg7hvdfYm7LydYQP6Ku78XuA1YG162FvhCuH8bsMbMTjCz04EVwH1VySdEv5A26Ff9Jl9FdPIFF8DOnc1tO3dKMXSDOuIUrgcuNLPHgAvDY9x9N3ArsAe4E7jO3Ut0DhSiP0kb9LsRR1B2dHKrQkhrn0lUHYXfFaXg7l9190vD/efcfbW7rwg/fxi5brO7n+HuZ7r7l7ohmxCdUncFsbRBX3mG+oduROGrnoIQHdCNIjpZ5di0KTAZLV0aKITpPOhbnNtJyDQesjpm1qz44MrBwcBRIiuqpyBERchHP6DsReHVq/O1zxS6EYUvpSBEB9Tho986AK9cmb+eQV6TV7tBv4pF4XvumaoAVq8O2mcyXYnCd/dpu5199tkuRJ0sW+YeDMXN27Jl1Txv9er45+WRYccO9+Hh5muHh4P2PM9cvTo4304GUS7r1sX/zuvW5bsPsMsTxlWtKQjRAd1eU2hna4+7Nq7ecd660Wn2fdn/u8v69cH/r2PHghnC2Fj+oEutKQhREb3s2ZPkqqq0FNObqqPwZ5V7OyFmHqOjvaEEorSLQ1i6NH6mUDSY7YQT4OWX49vF9EMzBSGmEUneNyMj2WcreYPZ0jyBWvMqNUhqF72NlIIQbag7MK2VJK+c3buzRxTnNXmleQIpIV6fkbQCPR02eR+JKsnqpbNjR+DpYxZ8JnnxVMm6de6Dg4GMg4P5vVE6Ia83UxJ1foeZBm28j2of2DvZpBRElWRxNy1rQMxD6+A5MhIvZzcH1U4H9LJcLUU2pBSEKIBZ/EBldvyabscpJA2eSVs3Zi9lzKgaCqV1GxysTu6ZTDuloDgFIRLI4s8/MBDvi58UI1CEaF6jon+uVcZOJP1O8+cHBX6efBJOPhlefLF58Tkqk2IduoviFIQoQBYvnaoXWVurqhXlpZeCEp1ZF8zzpGeOUwgQlP9syP3cc+2rv3UlfYPIhJSCEAlk8dKpulZBXMK9ohw7li03Ut70zJ0M3I2AufPOiz+f1C6qQ+YjITqkyrTVSeapOAYH82XLHBwMTFytMielZ472i6ZWyJN6o5WGKS5v6g3RGTIfCVEhrVXHIF9sQztTTVYzVCOfvjusW5etT9LMIU2xtM4cli3L9rxWojMqpd7oIZJWoDvdgFcR1Fj+LrAb+HjY/jHgaeDBcLsk0mcjsBd4FLgo7RnyPhK9xo4d7kNDzR40Q0PJ3j9prphZvY2irptJHlFZs6omeQIleQZlzdw6NOQ+f36891G3vbhmOtThkgoYMDfcHwK+BbwtVAofirl+JFQgJwCnA/8EDLZ7hpSC6AWirpZJbqzz58f3TXPFTBvg42ICkmTI4r7qns/tNe15WYP66oj3mMm0UwqVJcQLH3w4PBwKt3bW0cuBW9z9ZeBxM9sLnAN8syoZheiUuNTZcTz3XHx7WiWtJPNJO5fXpIR3jTWEgYH45zZMVY21gkZ65iQaC8ze5q8663pAYz2jn0qKTlcqXVMws0EzexB4Frjb3b8Vnnq/mT1kZtvN7KSw7VTgqUj3/WGbEF0jb66jTr2D0lwxs7q8Rtclnnwy2I8yPAzj44FSGB9P95iKpmdOWqMYG4tvL0rr2owUQk0kTSHK3IB5wL3AG4BTgEEChbQZ2B5e89+B90b63AT825h7jQG7gF1Lly6tanYlZiBFTBh5zDNxJKWoGBlJlinOVh/XPnfucdPNunXNppzW4zQzTbs0FnPnJj9f9Cb0QpoL4KO0rCUAy4GHw/2NwMbIubuAt7e7p9YURJkUWezMuig7MJCvfzS9Q3TNIo8Satyjanv9jh3us2Y133/WLK0H9DLtlEJlcQpmthD4mbu/YGYnAl8G/itwv7sfCK/5IPBWd19jZiuBvyZYR1gM7ARWuHuiVVNxCqJMiqSsyOOjn3Tvsq5PukdSDECDoiUdo5x6KjzzzPHjxYvh6aeL309US11xCouAe83sIeDbBGsKtwOfMLPvhe3vAD4I4O67gVuBPcCdwHXtFIIQZZNkv3cPBmMzWLmy+VxWH/2ivvyd0FiXSPP1T4tYTmPlymaFAMFx628lpgeVKQV3f8jd3+zub3L3N7j7H4btV7n7G8P2yxqzhvDcZnc/w93PdPcvVSWbEA3SFmhb2bOnebCLS3MRxyWXdCZnERoLwVkD4LZtK/acPXvytYveRhHNojC9UJWsExlac/y4Bx43c+e2N9NEB7vW/EhJ3kR33JFdrnbMmxffPjR0/NmDg4HHUMMclFVx5UmRIfqYpMWG6bBpobk+eiHYqFMZ0hZ583oSuWerwRClyDPmzWu+bt689O+aZbG6aO2CIt9B1AttFpo1UxCFiPPPj6ZCng4ypAWOFaEb9Yqff7556H3++fQ+0RiAsuMORkbytYveJpNSMLOFZvb7ZrYtDDjbbmbbqxZO9C69kMCsUxnSAseyDnZRE9bhw4EpJ0qZqbTL4NxzA1mjDAwE7UXYvXuqWWvevKBdTD+yzhS+ALwWuAf4YmQTM5RuvBGXIUO7NYekN+NG++7dUxXAyEjzYNdaBOe55457K0GgYNauTY7ObR2c09rLYNOmqS62r7zSfobV7ndcvx5eeKH5+hdeKO7NJGomya4U3YAHs1zX7U1rCvUxHdYUssjYacH5LBlJ2/0uddjj8657pP2Oqq88/aDTiGbgPxNJcd0rm5RCvXQ6oJZBu2LwZaRjbnd/9+xRxknPrCNldN5npl2vhebpRzulkHWSugG43cz+2cxeDLcfVzJ1EdOCiYkgsVq0ZOP4eD1uqUl0uubQahqKK2OZ1VyW9Myqy3nGkRQzkdSe9jsmue92UpFN1EiStpgOm2YK9dELRVHSzBpz5sTLOGdOtvtn+Y47drjPnp0+UxgcTJ5tdHvGVddMIW3WJboHZSTEAy4D/iTcLs3ar8pNSqE+8tqls5B30KjarJGlf1yltbStdd0jT6U2d/fFi5uvX7w42/dpUPaaQtbfqfW5ZlIMddGxUgCuJ0hQd3W43Q1cn6VvlZuUQn2UPVMosnCdNrh1qhSyDJ5Jv0NjZpC0CNv4nebPjz+fVKmtVSEUUQxF/u3aKewsv3PSbGr27Oxyi/IoQyk8BAxEjgeBh7L0rXKTUqiPsr2P0gbXuJlDL8wUOlVMeWXs9Du5x5u8Zs8u/m+XRXmWIbcoj3ZKIY839LzI/msLL2KIvqA158+yZcFx0WpZSYuZx44FQ0fcIm8di7StpMVKpAXI1UXwbpd8nIff+q187aLHSdIW0Q14D/AE8ClgHHgcWJOlb5WbZgr9QxZ//zgTR6dmjXZkeQPu1N5e1Uyh3eJ1FU4CaYvlmin0FpS00LyIYLH5cuBfZO1X5Sal0D/kWbDN6qmTdVBPUirr1sX3b31mJ7ESeQfLLGsKaXJX4SSQxurV8c9cvbq6Z4pkCisF4OfCz7fEbe36dmOTUugfsrp2ZhmkG6TVDs5iW+/UXbQMz51W0ryPBgbi79coCVpXTeVWxSCFUB/tlELbcpxmts3dx8zs3njLk5/fsf2qA1SOs14mJoJ8OU8+GdjQN28uvqaQVjKyHYODQR2EVtJKXS5YEOQqamX+fDh0qJgsMPV3ueSSoJ5C3O+UtxxnFtLuWaTsqOgv2pXjrLJG86uArwMnALOAz7r7R83sZOBvgOXAPuBKd38+7LMRuAY4BvyOu9/V7hlSCvXRiPaNpq4eHi6+2Jw0UGUlru+sWfFpsBtKpIoBOe/vUodSqOKZYnrRcY1mM3u3mb063P+PZvZ5M3tzSreXgfPd/ReAs4CLzextwEeAne6+giD24SPhfUeANcBK4GJgi5nV7KMhkii7nkIn2VWTPHmqqJeQRi/UmUhLO9GrHlGiN8jqkvqf3P1FM/sl4CICD6S/bNchNF0dDg+Hws0JFqrHw/Zx4Ipw/3LgFnd/2d0fB/YC52T9IqK7JJl6ipqANm+G2bOL9U1KgT13bvv2+fPjzye1ZyHJtfaJJ8orW5pWgjTpbb/RnpYyXMxssiqFxrvVu4Ct7v4FIPVP2MwGzexB4Fngbnf/FnCKux8ACD9fF15+KvBUpPv+sE30IFW8bWYxXcydm1yLuJWf/KR9+w03TC2IMzQUtOchOki3q4PgHiiH972vuGLIkqQvjS1bgt8t6+8oZhZZlcLTZvZXwJXAHWZ2Qpa+7n7M3c8ClgDnmNkb2lweN+mdMkyY2ZiZ7TKzXQcPHswmvSidLKaZtDfaKJs2wc9+lv7cw4dhyZLAFLJkSftqYWlvzKOjcPPNzQF4N9+cb02kdZDOYpr62c9gw4bsz4jSqXmq8W/xta81Z7j9x38sJk+DPP/WosdJckuKbsAw8OvAivB4EfDOLH0j9/go8CHgUWBR5D6PhvsbgY2R6+8C3t7unnJJrY+0nD1502AUcUXt5J5ZGRlp7jcy0nw+LT1Hmgx5A8myfKeiv2VRF9EiSf1EvVBCmotFwBfd/TEzOw94N3Bfuw5hXed54f6JwAXA94HbgLXhZWsJSn0Stq8xsxPM7HRgRdozRH28+GL79m4tuJZ9z+gb79AQ7NnTfH7PHli58vhx0hrCK69kc+/MW9ugSnbuLNZvw4aps7xOZkOiXrIqhc8Bx8zsXwE3AacDf53SZxFwr5k9BHybYE3hdoKMqxea2WPAheEx7r4buBXYA9wJXOfuFfqJ9DZlT8fLvt+RI+3bOy1wk4eii9uttJqC4mIfoFlRdFqr+qab8rVnodteRHGxHu3aRY+TNIWIbsAD4eeHgd8O97+TpW+VW7+aj8rOQFpFPeVumkXStkakbit50zlkzb8UNdX0Yu6jpDQXeb5XHsq+n6geSkid/S2CpHgPA6eHbQ9n6Vvl1q9KoeyEZVUkQEsbCLq1ptDpABola73l1v7tch+lrb1U9Z2i6TkGBpJTX0S3omsKeWtCiPpppxSymo/eB7wd2Ozuj4c2/x3lzVdElLJNL9005TQoO7V2N2hNw53EyEj2e5bl9tpg3bps7Vu2BOYv98C76Nprm11QFy9uvn71arjnnmIy3XDD1BiT2bOLf0dRM0naYjps/TpTKPvNq4o3ubJNBkkVyrJsg4PlfO8sb9Pz5jX3yTIjajeTKJI9NG+SvirMh3HPUP3l6QNFZwpmdmv4+T0zeyiyfS9cQBaiFDpJPZHU98or87Vn8RZ64QVYv/74cZKX1dq1xxf1AfbtC+6/b1/zbOn1r49/TlI7NM8Cjh5NDzrrhifY6GjydxTTi7QsqYvc/YCZLYs77+4l+X0Uo18T4pWdxbKKrJhlJ1V79auDwLSixD0zKfPqsmXBwNVKUgK9VqJZWbMk8muXEC8taV8c69cH9zt2LLhubKy9YlBWVNFK4YR4fjwdxROhAngeeDGyiQro1M2x6vtVQVJKik7Iu5aSNfdPdBDP8hu2eyvPm7Rv/XrYurU5Gnnr1ubZSyvd+PdXRHMfkWRXim7AtcAPCFJdPx5u/zdL3yq3fl1TKLuweqd27zjKXlMoup7QurbQadnJqL0+yxpG3G8btyW5wSY9K2mdJO/1STKWuabQjTULUS6U4JL6GLAgy7Xd3PpZKZSdNqDdoF/keUWUQtF6ynm3hmIoMlhFlUKSi2q7cpxJg3aSIspa8rOT3z3tt++UKlyeRbWUoRTuBIazXNvNrV+VQrf/yIp4J+UdnDoJ8sq7tb7JZx0M04K+snr65J3l5fEmKjJTqJo6aj6LzminFDJVXgsL6txMEMT2csT09Dul2bEKoIXmciiyaJylT7Qs5cBAvJ28sejb7n5FyPDfegpl/O4TE4HnUfS7Dg7C+Hg5HjkXXBCfo6iTOINOybugL+qn48prwF8BXwH+Abg/sokKSAqiyhpc1QtkTSldVt6iKEVz/yQpkjwKZsOGqd/12LHyksPt3ZuvvRts3jz1/+bwcNAuph9ZlcJRd/9dd7/Z3ccbW6WSzWB++tN87Z1SRQWyON/4OKpI3lZnBbEiyeHyeO7UEZ2exnSMXhfJZFUK94bFbRaZ2cmNrVLJZjBJpoqqfMqrSFOQdQZQZr3kTiuIpZXvrIKJiaASW7SSWrvKbL3qXqzgtf4hq1L49wRFcP6e46aj/jPm9wjdLqw+Ogrbtze/6W3f3v4Pu2hx+FY6mY1EcY+P7s3zFv6XfxkEk0WZNStoz0ra79JK3loEMtWIyklagZ4OW796H+V1U8x6zzz5ctJI8z7K6imUJVtoli3J1TavS2qnrpt5vbLyXl+GjFXQizKJZCjqkgp8OLL/7pZzf9Subze2flUK7p0P4tE/0jlzylcyaYNZluRyRZRI2hZ1/6zDf76K8pq9joLXph/tlEJa7qMH3P0trftxx3XQry6pndKwU7eaJVppl18njTSX1DwupmbFXEiTmD8fDh2qJ+dPw+squsjeLvfRggXxi9CN7zAdkEvq9KMTl1RL2I87bn3oaWZ2r5k9Yma7zWxD2P4xM3vazB4Mt0sifTaa2V4ze9TMLkqRTSQQZ6eOo8xF3k4oUyHA8UG2jkXZvJ44/VCLoBc9okRx0pSCJ+zHHbdyFPg9d/954G3AdWbWKE/y5+5+VrjdARCeWwOsBC4GtphZl6vN9gdZa+NWWcu37GC0ItS1KJvHE6fIIn+v0aseUaIYaUrhF8zsx2b2IvCmcL9x/MZ2Hd39gLs/EO6/CDwCnNqmy+XALe7+srs/DuwFzsn8TURuqvTnL/vtPw9z5gSf08V/frq7c8ojqr9IS5096O6vcfdXu/uscL9xPNSubxQzWw68mSBNBsD7w2I9283spLDtVOCpSLf9tFcifc0FFwQDWWO74ILsfdPcPDv15+9EhoGB4PtUOUuJmsWm+4BblG6msp4uyldkI2ucQmHMbC7wOeAD7v5jYCtwBnAWcAD408alMd2nvG+GQXS7zGzXwYMHqxG6ZuLy2+zcmV0xJFUWW7cueIPPUq2rKk46KRigzzuvumf88z9Xd+/pQGuKkSeeCI6rVgwzUfn2I5kS4hW+udkQcDtwl7v/Wcz55cDt7v4GM9sI4O7/JTx3F/Axd/9m0v371fuo06pmc+fGF62ZM6ez6mZR0mRM8/zJWuWsKHWar+pG3kAijTIS4hV5qAE3AY9EFYKZLYpc9mvAw+H+bcAaMzvBzE4HVgD3VSVfP5NUxayK6mZJnJyQBKXR3iueT/2IvIFEJ1RpPjoXuAo4v8X99BNm9j0zewh4B/BBAHffDdwK7CGo33Cdu2voKBmVS+x/5A0kOmFW+iXFcPdvEL9OcEebPpsB+Sx0yMBAcnBW1MYMxW2/c+fGm6IayeN++MP4fkntZVJWPqXpyubN8QF08gYSWah8oVnkJ29StVbe8Y70a1qLya9fH9j5zYLPdoXgAa66qn172tvqQEX/84aGplfgVxXIG0h0RFL+i+mw9Wruo24nVWultRxkuyRy7sUS8KWV8OxW+U2z4JlKxCZEdui0RnOvbr2oFMpIDpY2CKYNflkH1MYAXqTubxbF1U45lqUUQAXihchLO6VQqUtq1fSiS2oZ7oBZzETtkqxlNTM1kq5VVaO5HUkuq0WoMsGdEP1ILS6pM5VuuQO2rgkUoZEjKcm+X5XdH8qNI5BXjRDlIaVQMt10ByxL0Zx4Yr72Mli2rJz7yKtGiHKRUiiZSy7J194JZSmaqOtilvYy6OT3kFeNENUhpVAyt96ar70oZb4h1xHsdEditEp7Zs9Wjh0hqkRKoWSSahlkrXGQRhVvyHWkPi5q+vrlXy5XDiFEM5VFNItqqMLLpqFcNm0KBuulSwOFUOVb+NKl8V5aaXz1q6WLIoSIoJmCALqf+jhudpIFJdITolqkFEqm0xQV04VOv2drKoasVFmcRwghpVCIdlWtkvzvez1GMG+lrvPPz9ceR3R2MjKSejlQbQlRIYTWFHLTqGrVcNcsI+No3RT5Tnv35mtPI63Ww+BgIFNdFeOEmCkozUVO0tJYZEn/MDHRflG30xQSecwx7sVSc6RVVstLp99ZCJEdpbkokU7TWExMwNVXN9fPvfrqeoreNEw2Rb5T2bENSWsFWkMQortIKeSk08FwwwY4cqS57ciRoL3b7NkTfBb5TmXHNiR5FcnbSIjuUmWN5tPM7F4ze8TMdpvZhrD9ZDO728weCz9PivTZaGZ7zexRM7uoKtk6odPBsOrgtiIU+U5lF3JJyoVUVo4kIUQ2qpwpHAV+z91/HngbcJ2ZjQAfAXa6+wpgZ3hMeG4NsBK4GNhiZj1nPBgdhbVrj5s1BgeD415aZM7qydOg6ABfZmxDN3NGCSGSqUwpuPsBd38g3H8ReAQ4FbgcGA8vGweuCPcvB25x95fd/XFgL3BOVfIVZWICxsePmzWOHQuO61gTSKJIpHC3g9daScqFVDRHkhCiGF1ZUzCz5cCbgW8Bp7j7AQgUB/C68LJTgaci3faHbT3Fpk1Ts4eWUdugTNLcO3uRbtWhEEK0p3KlYGZzgc8BH3D3H7e7NKZtijOimY2Z2S4z23Xw4MGyxMxM0lt4kbfzImQNLptu1JGpVQgxlUqVgpkNESiECXf/fNj8AzNbFJ5fBDwbtu8HTot0XwI803pPd9/m7qvcfdXChQurEz6Bul0nG26sY2P9pRjqyNQqhJhKld5HBtwEPOLufxY5dRuwNtxfC3wh0r7GzE4ws9OBFcB9VclXlF5xnewFk1Xe1BjtmA4L+ELMBKqcKZwLXAWcb2YPhtslwPXAhWb2GHBheIy77wZuBfYAdwLXubu81NuQZG+fPz9b/8WLiz+7kRojGoTXyexlYgJuvLF5Af/GG/trNiTEdEBpLnLSLh2DWfuUDO7Z0jlkTVORlIZi/XrYujW9//z5cOhQtme1UiQ1RjsWLIiP1ehERiFEPEpz0SW6qV/b2duzlv7sJGCubG+hXgzqE2ImIqUwzcgSXNaNgVTeQkL0J0qdPc0osxznQAevBJs3N6fbhs68hebPTzYfCSG6h2YKfUjWwb4TBVN27qMbboDZs5vbZs8O2oUQ3UMzhT4k62DfabK50dHyXEYb92lXZ0IIUT2aKfQhWQb7oaHeCwz7u7+D/fuDBfv9+4NjIUR3kVLoQ+Kig1vJU52tGzTcaKNxClu3Bu1CiO6hOIWcdDKYlhGnkPWfK1ryc2AgPuK6aExBFcyaFS/j4CAcPdp9eYToZxSnMAOJpsJOWmPopQykvZI+RIiZjpRCl5kzJ7199er4a5La01BMgRAiK1IKXaJRDS3JNBRt37s3/pqk9jSyKCIhhAApha4wMgK7dwf7hw/HXxNtL7tmw549+drrQDWahegNpBQqpBHU9fu/X7ckvY/qKQjRG0gpxLB+feANYxZ8FnWL7NeCOFVQdoS0EKIYUgotVOEvX3dBnLIXrqsi6jG1b58UghB1IKXQwrZt7duLJmhruH8m9a8y8ds990xVAKtXB+1CCBFFSqGFNH/5K68sdt+G+2dS/6L3zco99wTmrMYmhSCEiKPKGs3bzexZM3s40vYxM3u6pTxn49xGM9trZo+a2UVVyQXtaws3agS30mi/4478z4vmGUrqH21vzRaa1i6EEGVR5UzhU8DFMe1/7u5nhdsdAGY2AqwBVoZ9tphZwvDcGWm1hcfG4vs12otEAUdjELJULNu+fWo8g1nQLoQQVVKZUnD3rwM/zHj55cAt7v6yuz8O7AXOqUKuTZuaC8NA80Lwli2wbt3xmcHgYHC8ZUtwnBQFPDgYDNxxM40jR47fP0t08egofPrTzZ44n/60Fl6FENVTx5rC+83sodC8dFLYdirwVOSa/WFb6WR5Uz/3XFiyJBiQlywJjhsk+dOPj2fLM5TVH1+eOEKIOui2UtgKnAGcBRwA/jRsj0v+EJsP1MzGzGyXme06ePBgbgGSUko32tPMS3H+9GvXBjOBgYHkqmeNmUBWf/x26x5Z6LS/EGKG4u6VbcBy4OG0c8BGYGPk3F3A29Puf/bZZ3teBgaiPjjHt4GB4PyyZfHnBwfdzYLzO3Ycv9+OHe7Dw/F9GtvwcHOfNOLumeceO3a4z57d3H/27HwyCCH6F2CXJ4yrldZTMLPlwO3u/obweJG7Hwj3Pwi81d3XmNlK4K8J1hEWAzuBFe7eNnFykXoKabUKBgbSaxYMDx9/u1++PD4n0eBgYPopUlYy6Z5Z6x8sWADPPTe1ff58OHQouxxCiP6klnoKZvYZ4JvAmWa238yuAT5hZt8zs4eAdwAfBHD33cCtwB7gTuC6NIVQlDSX0yzppKML00lrFI31hSLrAVnWPdoRpxAa7Z2m7hBC9DdVeh+9x90XufuQuy9x95vc/Sp3f6O7v8ndL2vMGsLrN7v7Ge5+prt/qSq50lxOL7kk/nwrjQG6iloFJ5+crz0vKnUphEhixkU0p7mcZg1Oawz6SUokq3KpgqwpM5JSegghZi4zTilAoACOHg3WDo4ePa4QIJuJJupCmiVCOS8/TIjuSGpv5YYbgijqNFTqUgjRyoxUCu1IC05rdSHt1P6fR4asJqnRUbj55uNur0kkra8IIWYuUgotpAWntS4cFxnA02IIyig4Ew1+S0qRfd552e8nhJgZSCm0kLfYS94BPC04rogMaZRd81kI0b9IKcSQJ8VE3gE8LfdSFVRh4hJC9CdSCgVoNf9AdiWSZYDOMpvIQxVus0KI/kRKISedDthZBuiyZxNlrFEIIWYGUgo56XTAzjJAl23uKXuNQgjRv0gp5KTTATvLAF2FuUepuIUQWZBSyEkZA3baAC1zjxCiLqQUctKNAVvmHiFEXcyqW4DpRmNg3rQpMBkVSY2d9TlSAkKIbqOZQgE6tc9nqYqmymlCiDqQUiiBPAN4FpfWsuMUhBAiK5VWXquaIpXXyqYxgEfdVKOV2VrJUlWt08prQgjRjnaV16QUOiTvAJ5U7tMsMEdlvUYIIYpSVznO7Wb2rJk9HGk72czuNrPHws+TIuc2mtleM3vUzC6qSq6yyRu3kMWlVWkphBB1UeWawqeAi1vaPgLsdPcVwM7wGDMbAdYAK8M+W8xsWmT7zzuAZ3FpVZyCEKIuqqzR/HWgtVbY5cB4uD8OXBFpv8XdX3b3x4G9wDlVyVYmeQfwLDEIilMQQtRFt+MUTnH3AwDufsDMXhe2nwr8Q+S6/WFbz1MkbiFLDILiFIQQddArwWtxRSNjV8DNbAwYA1jaI0Z2DeBCiH6h23EKPzCzRQDh57Nh+37gtMh1S4Bn4m7g7tvcfZW7r1q4cGGlwgohxEyj20rhNmBtuL8W+EKkfY2ZnWBmpwMrgPu6LJsQQsx4KjMfmdlngPOABWa2H/gocD1wq5ldAzwJvBvA3Xeb2a3AHuAocJ27H6tKNiGEEPFUphTc/T0Jp1YnXL8ZkNOlEELUiHIfCSGEmGRap7kws4NATJKJzCwADpUkTlVIxnKQjOUgGcuhbhmXuXusp860VgqdYma7kvJ/9AqSsRwkYzlIxnLoZRllPhJCCDGJlIIQQohJZrpS2Fa3ABmQjOUgGctBMpZDz8o4o9cUhBBCNDPTZwpCCCEizDilEFf8p9cws9PM7F4ze8TMdpvZhrplasXMXmVm95nZd0MZP163TEmY2aCZfcfMbq9bliTMbJ+Zfc/MHjSzessJJmBm88zss2b2/fD/5tvrlimKmZ0Z/n6N7cdm9oG65WrFzD4Y/s08bGafMbNX1S1TlBlnPjKzXwEOA//T3d9QtzxxhMkCF7n7A2b2auB+4Ap331OzaJOYmQFz3P2wmQ0B3wA2uPs/pHTtOmb2u8Aq4DXufmnd8sRhZvuAVe7es/71ZjYO/B93v9HMZgPD7v5CzWLFEhbpehp4q7t3EstUKmZ2KsHfyoi7/zRM73OHu3+qXsmOM+NmCgnFf3oKdz/g7g+E+y8Cj9Bj9SU84HB4OBRuPfeGYWZLgHcBN9Yty3TGzF4D/ApwE4C7H+lVhRCyGvinXlIIEWYBJ5rZLGCYhIzQdTHjlMJ0w8yWA28GvlWzKFMIzTIPEqRAv9vde05G4JPAh4FXapYjDQe+bGb3hzVDeo1/CRwEbg5NcTea2Zy6hWrDGuAzdQvRirs/DfwJQULQA8CP3P3L9UrVjJRCD2Nmc4HPAR9w9x/XLU8r7n7M3c8iqH9xjpn1lDnOzC4FnnX3++uWJQPnuvtbgF8FrgvNnL3ELOAtwFZ3fzPwE8Ia671GaNq6DPhfdcvSipmdRFB++HRgMTDHzN5br1TNSCn0KKGd/nPAhLt/vm552hGaEb4KXFyvJFM4F7gstNffApxvZjvqFSked38m/HwW+Ft6r0b5fmB/ZDb4WQIl0Yv8KvCAu/+gbkFiuAB43N0PuvvPgM8D/7pmmZqQUuhBwkXcm4BH3P3P6pYnDjNbaGbzwv0TCf6zf79WoVpw943uvsTdlxOYE77i7j31VgZgZnNChwJCk8w7gZ7yjnP3/wc8ZWZnhk2rCeqf9CLvoQdNRyFPAm8zs+Hw73w1wZphzzDjlEJY/OebwJlmtj8s+NNrnAtcRfBm23Cvu6RuoVpYBNxrZg8B3yZYU+hZl88e5xTgG2b2XYKKg1909ztrlimO3wYmwn/zs4A/qlecqZjZMHAhwRt4zxHOtD4LPAB8j2AM7qno5hnnkiqEECKZGTdTEEIIkYyUghBCiEmkFIQQQkwipSCEEGISKQUhhBCTSCmIGYOZHWvJolk4ItfM/r5M2VruvcrM/qKq+wvRDrmkihmDmR1297l1yyFEL6OZgpjxhLUMPm5mD4Q1DX4ubF9oZneH7X9lZk+Y2YLw3OHw8zwz+2qkzsBEGKmKmZ1tZl8Lk9zdFaZEb332u8O8+t81s69H7nl7uH9HZGbzIzNbGyYi/GMz+7aZPWRm13brtxL9j5SCmEmc2GI++neRc4fChHRbgQ+FbR8lSI3xFoJ8REsT7vtm4APACEE20XPD3FX/DfgNdz8b2A5sjun7B8BF7v4LBEncmnD3S8Kkg9cATwD/O9z/kbv/IvCLwG+a2ekZfwMh2jKrbgGE6CI/DQfYOBppEe4Hfj3c/yXg1wDc/U4zez6h733uvh8gTCW+HHgBeANwdzhxGCRIldzK3wGfCoutxKZmCGcnnwaudPcfmdk7gTeZ2W+El7wWWAE8niCfEJmRUhAi4OXw8xjH/y4sZ99ofwN2u3vbkpXu/ltm9laCQkAPmtlZ0fNhBbFbgD9090aSPAN+293vyiifEJmR+UiIZL4BXAkQvp2flKPvo8BCC+sYm9mQma1svcjMznD3b7n7HwCHgNNaLrkeeMjdb4m03QWsC01UmNnre7zgjZhGaKYgZhInhuadBne6ezu31I8DnwnXHr5GYP55McuD3P1IaN75CzN7LcHf2ieB3S2X/rGZrSB4+98JfBf4N5HzHwJ2R+T+A4LSosuBB8JF7YPAFVnkEiINuaQKkYCZnQAcc/ej4Rv/1jZrEkL0BZopCJHMUuBWMxsAjgC/WbM8QlSOZgpCCCEm0UKzEEKISaQUhBBCTCKlIIQQYhIpBSGEEJNIKQghhJhESkEIIcQk/x8ySYrXmIokJQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Train data distribution \n",
    "plt.scatter(train.ENGINESIZE,\n",
    "            train.CO2EMISSIONS,\n",
    "            color='blue')\n",
    "plt.xlabel(\"Engine size\")\n",
    "plt.ylabel(\"Emission\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3ce895c-7007-49d4-9389-024088cb7717",
   "metadata": {},
   "source": [
    "<details><summary>Click here for the Simple Model:</summary>\n",
    "\n",
    "```python\n",
    "from sklearn import linear_model\n",
    "regr = linear_model.LinearRegression()\n",
    "train_x = np.asanyarray(train[['ENGINESIZE']])\n",
    "train_y = np.asanyarray(train[['CO2EMISSIONS']])\n",
    "regr.fit(train_x, train_y)\n",
    "# The coefficients\n",
    "print ('Coefficients: ', regr.coef_)\n",
    "print ('Intercept: ',regr.intercept_)\n",
    "\n",
    "### Plot outputs\n",
    "plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')\n",
    "plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')\n",
    "plt.xlabel(\"Engine size\")\n",
    "plt.ylabel(\"Emission\")\n",
    "\n",
    "```\n",
    "\n",
    "</details>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d64cdc3e-f453-4438-ac98-5ba87da1296c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coefficients:  [[9.62605779 8.55830867 9.38189361]]\n",
      "Intercept:  [65.1216574]\n"
     ]
    }
   ],
   "source": [
    "from sklearn import linear_model\n",
    "regr = linear_model.LinearRegression()\n",
    "x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])\n",
    "y = np.asanyarray(train[['CO2EMISSIONS']])\n",
    "regr.fit (x, y)\n",
    "# The coefficients\n",
    "print ('Coefficients: ', regr.coef_)\n",
    "print ('Intercept: ',regr.intercept_)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "001a800b-c0ee-4877-8665-f00de3679bce",
   "metadata": {},
   "source": [
    "__Coefficient__ and __Intercept__  are the parameters of the fitted line. \n",
    "Given that it is a multiple linear regression model with 3 parameters and that the parameters are the intercept and coefficients of the hyperplane, sklearn can estimate them from our data. Scikit-learn uses plain Ordinary Least Squares method to solve this problem.\n",
    "\n",
    "#### Ordinary Least Squares (OLS)\n",
    "OLS is a method for estimating the unknown parameters in a linear regression model. OLS chooses the parameters of a linear function of a set of explanatory variables by minimizing the sum of the squares of the differences between the target dependent variable and those predicted by the linear function. In other words, it tries to minimizes the sum of squared errors (SSE) or mean squared error (MSE) between the target variable (y) and our predicted output ($\\hat{y}$) over all samples in the dataset.\n",
    "\n",
    "OLS can find the best parameters using of the following methods:\n",
    "* Solving the model parameters analytically using closed-form equations\n",
    "* Using an optimization algorithm (Gradient Descent, Stochastic Gradient Descent, Newton’s Method, etc.)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aba2ec4d-7512-492f-a4ca-c942136ac25a",
   "metadata": {},
   "source": [
    "____\n",
    "# [6] Model Evaluation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "67faf08b-f764-43f1-8421-0b4a83bfe02c",
   "metadata": {},
   "source": [
    "<details><summary>Click here for the Simple Model Evaluation:</summary>\n",
    "    \n",
    "We compare the actual values and predicted values to calculate the accuracy of a regression model. Evaluation metrics provide a key role in the development of a model, as it provides insight to areas that require improvement.\n",
    "\n",
    "There are different model evaluation metrics, lets use MSE here to calculate the accuracy of our model based on the test set: \n",
    "* Mean Absolute Error: It is the mean of the absolute value of the errors. This is the easiest of the metrics to understand since it’s just average error.\n",
    "\n",
    "* Mean Squared Error (MSE): Mean Squared Error (MSE) is the mean of the squared error. It’s more popular than Mean Absolute Error because the focus is geared more towards large errors. This is due to the squared term exponentially increasing larger errors in comparison to smaller ones.\n",
    "\n",
    "* Root Mean Squared Error (RMSE). \n",
    "\n",
    "* R-squared is not an error, but rather a popular metric to measure the performance of your regression model. It represents how close the data points are to the fitted regression line. The higher the R-squared value, the better the model fits your data. The best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse)."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7f69f87e-5475-423b-80fb-f23a58f42522",
   "metadata": {},
   "source": [
    "<details><summary>Click here for the Simple Model Outputs:</summary>\n",
    "\n",
    "```python\n",
    "# Plot Outputs\n",
    "from sklearn.metrics import r2_score\n",
    "\n",
    "test_x = np.asanyarray(test[['ENGINESIZE']])\n",
    "test_y = np.asanyarray(test[['CO2EMISSIONS']])\n",
    "test_y_ = regr.predict(test_x)\n",
    "\n",
    "print(\"Mean absolute error: %.2f\" % np.mean(np.absolute(test_y_ - test_y)))\n",
    "print(\"Residual sum of squares (MSE): %.2f\" % np.mean((test_y_ - test_y) ** 2))\n",
    "print(\"R2-score: %.2f\" % r2_score(test_y , test_y_) )\n",
    "```\n",
    "\n",
    "</details>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ff4b5a44-1725-47bd-91d5-25c2ca8f6c05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Residual sum of squares: 482.77\n",
      "Variance score: 0.88\n"
     ]
    }
   ],
   "source": [
    "# Prediction\n",
    "\n",
    "y_hat= regr.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])\n",
    "x = np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])\n",
    "y = np.asanyarray(test[['CO2EMISSIONS']])\n",
    "print(\"Residual sum of squares: %.2f\"\n",
    "      % np.mean((y_hat - y) ** 2))\n",
    "\n",
    "# Explained variance score: 1 is perfect prediction\n",
    "print('Variance score: %.2f' % regr.score(x, y))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f67d75d7-ad0f-4d8e-9fb0-d7dbb49aada3",
   "metadata": {},
   "source": [
    "__Explained variance regression score:__  \n",
    "Let $\\hat{y}$ be the estimated target output, y the corresponding (correct) target output, and Var be the Variance (the square of the standard deviation). Then the explained variance is estimated as follows:\n",
    "\n",
    "$\\texttt{explainedVariance}(y, \\hat{y}) = 1 - \\frac{Var\\{ y - \\hat{y}\\}}{Var\\{y\\}}$  \n",
    "The best possible score is 1.0, the lower values are worse."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bea5713f-ff28-450c-9b32-787f046fbecb",
   "metadata": {},
   "source": [
    "_______\n",
    "# CHANGE TO FEATURE `x`\n",
    "use a multiple linear regression with the same dataset, but this time use FUELCONSUMPTION_CITY and FUELCONSUMPTION_HWY instead of FUELCONSUMPTION_COMB. Does it result in better accuracy?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "3291df5f-dbea-4966-9ab0-765b3ef5faf3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ENGINESIZE</th>\n",
       "      <th>CYLINDERS</th>\n",
       "      <th>FUELCONSUMPTION_CITY</th>\n",
       "      <th>FUELCONSUMPTION_HWY</th>\n",
       "      <th>CO2EMISSIONS</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.0</td>\n",
       "      <td>4</td>\n",
       "      <td>9.9</td>\n",
       "      <td>6.7</td>\n",
       "      <td>196</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.4</td>\n",
       "      <td>4</td>\n",
       "      <td>11.2</td>\n",
       "      <td>7.7</td>\n",
       "      <td>221</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.5</td>\n",
       "      <td>4</td>\n",
       "      <td>6.0</td>\n",
       "      <td>5.8</td>\n",
       "      <td>136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>12.7</td>\n",
       "      <td>9.1</td>\n",
       "      <td>255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>12.1</td>\n",
       "      <td>8.7</td>\n",
       "      <td>244</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ENGINESIZE  CYLINDERS  FUELCONSUMPTION_CITY  FUELCONSUMPTION_HWY  \\\n",
       "0         2.0          4                   9.9                  6.7   \n",
       "1         2.4          4                  11.2                  7.7   \n",
       "2         1.5          4                   6.0                  5.8   \n",
       "3         3.5          6                  12.7                  9.1   \n",
       "4         3.5          6                  12.1                  8.7   \n",
       "\n",
       "   CO2EMISSIONS  \n",
       "0           196  \n",
       "1           221  \n",
       "2           136  \n",
       "3           255  \n",
       "4           244  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2 = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY', 'CO2EMISSIONS']]\n",
    "df2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "6b9bebe5-3b3e-4705-ae73-5e3af7d7ebec",
   "metadata": {},
   "outputs": [],
   "source": [
    "msk = np.random.rand(len(df)) < 0.8\n",
    "train = df2[msk]\n",
    "test = df2[~msk]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "c1c97df7-0fcd-4206-915b-3c4847b0705a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coefficients:  [[10.67271258  7.49971334  5.55041173  4.10106026]]\n",
      "Residual sum of squares: 641.18\n",
      "Variance score: 0.85\n"
     ]
    }
   ],
   "source": [
    "regr = linear_model.LinearRegression()\n",
    "x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY']])\n",
    "y = np.asanyarray(train[['CO2EMISSIONS']])\n",
    "regr.fit (x, y)\n",
    "print ('Coefficients: ', regr.coef_)\n",
    "y_= regr.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY']])\n",
    "x = np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY']])\n",
    "y = np.asanyarray(test[['CO2EMISSIONS']])\n",
    "print(\"Residual sum of squares: %.2f\"% np.mean((y_ - y) ** 2))\n",
    "print('Variance score: %.2f' % regr.score(x, y))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
