{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1fe4f856-98e5-4935-8953-ca80786789d4",
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
       "      <th>order_id</th>\n",
       "      <th>customer</th>\n",
       "      <th>region</th>\n",
       "      <th>product</th>\n",
       "      <th>category</th>\n",
       "      <th>price</th>\n",
       "      <th>quantity</th>\n",
       "      <th>order_date</th>\n",
       "      <th>order_value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1001</td>\n",
       "      <td>Anna</td>\n",
       "      <td>Krakow</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>Electronics</td>\n",
       "      <td>3500</td>\n",
       "      <td>1</td>\n",
       "      <td>2026-01-10</td>\n",
       "      <td>3500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1002</td>\n",
       "      <td>Piotr</td>\n",
       "      <td>Warsaw</td>\n",
       "      <td>Mouse</td>\n",
       "      <td>Electronics</td>\n",
       "      <td>80</td>\n",
       "      <td>2</td>\n",
       "      <td>2026-01-11</td>\n",
       "      <td>160</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1003</td>\n",
       "      <td>Kasia</td>\n",
       "      <td>Krakow</td>\n",
       "      <td>Desk</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>900</td>\n",
       "      <td>1</td>\n",
       "      <td>2026-01-12</td>\n",
       "      <td>900</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   order_id customer  region product     category  price  quantity  \\\n",
       "0      1001     Anna  Krakow  Laptop  Electronics   3500         1   \n",
       "1      1002    Piotr  Warsaw   Mouse  Electronics     80         2   \n",
       "2      1003    Kasia  Krakow    Desk    Furniture    900         1   \n",
       "\n",
       "   order_date  order_value  \n",
       "0  2026-01-10         3500  \n",
       "1  2026-01-11          160  \n",
       "2  2026-01-12          900  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "def load_data():\n",
    "    df = pd.read_csv('data/orders.csv')\n",
    "    return df\n",
    "\n",
    "df = load_data()\n",
    "df['order_value'] = df['price'] * df['quantity']   \n",
    "df.head(3\n",
    "       )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "4e99937e-cb26-4153-992f-8a4dd45fb7c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total revenue is 16175\n"
     ]
    }
   ],
   "source": [
    "total_revenue = df['order_value'].sum()\n",
    "print(f\"total revenue is {total_revenue}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a86f5d67-0f8e-41e6-93b7-a955b3b97931",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "region\n",
      "Krakow    8015\n",
      "Name: order_value, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "most_revenue_region = df.groupby('region')['order_value'].sum().sort_values(ascending = False)\n",
    "print(most_revenue_region[:1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "6007d5d6-34d6-44d9-821d-ef1fa93ad278",
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
       "      <th>region</th>\n",
       "      <th>order_value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Gdansk</td>\n",
       "      <td>3150</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Krakow</td>\n",
       "      <td>8015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Warsaw</td>\n",
       "      <td>5010</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   region  order_value\n",
       "0  Gdansk         3150\n",
       "1  Krakow         8015\n",
       "2  Warsaw         5010"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "region_rev_df = df.groupby('region')['order_value'].sum().reset_index()\n",
    "region_rev_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "c9c64ebe-5b35-4db4-a665-975dbcfa76c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "region_rev_df.to_csv('daily_raport.csv', index = False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
