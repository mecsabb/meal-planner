from fastapi import FastAPI
import pandas as pd
import numpy as np
from pydantic import BaseModel
import json

import model

class Preferences(BaseModel):
    recipe_id: str
    like: int

recipes_df = pd.read_csv('_part.csv')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Muckers"}

@app.get("/arbitrary-meals")
async def get_arb_meal():
    length = len(recipes_df)
    curr_id = recipes_df['recipe_id'].iloc[np.random.randint(0, length)]
    return pd.DataFrame(recipes_df.loc[recipes_df['recipe_id'] == curr_id]).to_dict()

@app.post("/preferences")
async def post_user_prefs(preferences: Preferences):
    print('#####')
    print(preferences)
    print('#####')
    df = pd.read_csv('dataset.csv')
    row = [-1, preferences.recipe_id, preferences.like]
    df.loc[len(df)] = row
    df.to_csv('dataset.csv', index=False)

@app.get("/good-meals")
async def get_good_meals():
    dg = model.DataGen()
    dg.getRecommendations()