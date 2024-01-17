from fastapi import FastAPI
import pandas as pd
import numpy as np
# from pydantic import BaseModel

# import model

# class Preferences(BaseModel):
#     recipe_id: str
#     like: int



recipes_df = pd.read_csv('/Users/colin.gould/Desktop/code/archive_2/RAW_recipes.csv')

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    return {"message": "Hello Muckers"}

@app.get("/generate")
async def generate_random_meal():
    length = len(recipes_df)
    rand_recipe = recipes_df['name'].iloc[np.random.randint(0, length)]
    return rand_recipe
    # return pd.DataFrame(recipes_df.loc[recipes_df['recipe_id'] == curr_id]).to_dict()

# @app.post("/preferences")
# async def post_user_prefs(preferences: Preferences):
#     print('#####')
#     print(preferences)
#     print('#####')
#     df = pd.read_csv('dataset.csv')
#     row = [-1, preferences.recipe_id, preferences.like]
#     df.loc[len(df)] = row
#     df.to_csv('dataset.csv', index=False)

# @app.get("/good-meals")
# async def get_good_meals():
#     dg = model.DataGen()
#     dg.getRecommendations()