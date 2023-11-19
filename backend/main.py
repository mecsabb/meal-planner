from fastapi import FastAPI
import pandas as pd
import numpy as np

# class user:
#     def __init__(self):
#         likes = []
#         dislikes = []
#     def set_preferences(self, recipe_ids, l_d):
#         for curr_id, pref in recipe_ids, l_d:
#             if pref == 0:
#                 self.dislikes.append(curr_id)
#             elif pref == 1:
#                 self.likes.append(curr_id)

recipes_df = pd.read_csv('/Users/colin.gould/Desktop/code/QEC/meal-planner/archive/RAW_recipes.csv')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Muckers"}

@app.get("/arbitrary-meals")
async def get_arb_meal():
    length = len(recipes_df)
    curr_id = recipes_df['id'].iloc[np.random.randint(0, length)]
    return pd.DataFrame(recipes_df.loc[recipes_df['id'] == curr_id]).to_dict()

@app.post("/preferences")
async def post_user_prefs(recipes):
    recipe_ids = recipes.keys()
    like_dislike = recipes.values()
    data = [recipe_ids, like_dislike]
    prefs = pd.read_csv('preferences.csv')
    updates = pd.DataFrame(data, columns = ['recipe_ids', 'like_or_dislike'])
    new = pd.concat([prefs, updates], ignore_index = True)
    new.to_csv('preferences.csv')
    return 1
    
    
@app.get("/good-meals")
async def get_good_meals():
    pass