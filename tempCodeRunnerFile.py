import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

popular_df = pickle.load(open(os.path.join(BASE_DIR,"artifacts",'popular.pkl'),'rb'))
pt = pickle.load(open(os.path.join(BASE_DIR,"artifacts",'pt.pkl'),'rb'))
books = pickle.load(open(os.path.join(BASE_DIR,"artifacts",'books.pkl'),'rb'))
similarity_scores = pickle.load(open(os.path.join(BASE_DIR, "artifacts",'similarity_scores.pkl'),'rb'))