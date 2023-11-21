import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics.pairwise import pairwise_distances

import numpy as np
import pandas as pd

class DataGen:
    def __init__(self):

        def predict(ratings, similarity):
            pred = similarity.dot(ratings) / np.array([np.abs(similarity).sum(axis = np.newaxis)])
            return pred
        
        df = pd.read_csv('dataset.csv')
        self.df = df

        users = df.user_id.unique()
        items = df.recipe_id.unique()

        data_matrix = np.zeros((users.shape[0], items.shape[0]))

        for row in df.itertuples():
            data_matrix[row[1]-1, row[2]-1] = row[3]

        self.user_similarity = 1 - pairwise_distances(data_matrix, metric = 'cosine')
        self.user_pred = predict(data_matrix, self.user_similarity)
        self.user_pred_df = pd.DataFrame(self.user_pred, columns = list(items))

    def getRecommendations(self, user_id=-1, top_n = 10):
        
        movie_rated = list(self.df['recipe_id'].loc[self.df['user_id'] == user_id])
        _all = self.user_pred_df.loc[self.user_pred_df['user_id'] == user_id].copy()
        _all.drop(self.user_pred_df[movie_rated], axis = 1, inplace = True)
        unwatch_sorted = _all.iloc[:,1:].sort_values(by = _all.index[0], axis = 1, ascending = False)
        dict_top_n = unwatch_sorted.iloc[:, :top_n].to_dict(orient = 'records')

        i = 1
        for recipe_id in list(dict_top_n[0].keys()):
            for old_recipe, new_recipe in self.new_recipeID.items():
                if recipe_id == new_recipe:
                    name = self.recipe[self.recipe['recipe_id'] == old_recipe]['name'].values[0]
                    ingredients = self.recipe[self.recipe['recipe_id'] == old_recipe]['ingredients'].values[0]

                    print(f'Top {i} Original Recipe ID: {old_recipe} - {name}\n Ingredients: {ingredients}\n')
                    
                    i += 1
                    
        return dict_top_n[0]
