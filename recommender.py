# recommender.py

def collaborative_filtering(df, fav_singer):
    similar_songs = df[df['singer'].str.contains(fav_singer, case=False, na=False)]
    return similar_songs[['name', 'singer', 'duration', 'link', 'language']]

def content_based_filtering(df, fav_language):
    similar_songs = df[df['language'].str.contains(fav_language, case=False, na=False)]
    return similar_songs[['name', 'singer', 'duration', 'link', 'language']]
