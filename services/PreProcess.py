import re
import numpy as np
import pandas as pd
from textblob import TextBlob
from config import candidates


class PreProcesss(object):
    """docstring for PreProcesss"""

    def __init__(self, arg):
        super(PreProcesss, self).__init__()
        self.arg = arg

    def clean(df):
        df = df[df.candidate.isin(candidates)]
        del df['Unnamed: 0']
        return df

    def datetimeify(df):
        df['created_at'] = pd.DatetimeIndex(df.created_at)
        return df

    def sentiment(df):
        text = df.dropna(subset=['text']).text
        sentiment = text.apply(lambda text: TextBlob(text).sentiment)
        df['polarity'] = sentiment.apply(lambda sentiment: sentiment.polarity)
        df['subjectivity'] = sentiment.apply(lambda sentiment: sentiment.subjectivity)
        return df

    def sentiment(df):
        text = df.dropna(subset=['text']).text
        sentiment = text.apply(lambda text: TextBlob(text).sentiment)
        df['polarity'] = sentiment.apply(lambda sentiment: sentiment.polarity)
        df['subjectivity'] = sentiment.apply(lambda sentiment: sentiment.subjectivity)
        return df

    def influence(df):
        internal = np.sqrt(df.user_followers_count.apply(lambda x: x + 1))
        external = np.sqrt(df.retweet_count.apply(lambda x: x + 1))
        df['influence'] = internal * external
        return df

    def influenced_polarity(df):
        df['influenced_polarity'] = df.polarity * df['influence']
        return df

    def georeference(df):
        def place_to_coordinate(place_str, kind):
            if pd.isnull(place_str):
                return float('nan')
            number_matcher = r'(-?\d+\.\d+)[,\]]'
            coordinates = re.findall(number_matcher, place_str)
            coordinate = tuple(float(n) for n in coordinates[:2])

            if kind == 'longitude':
                return coordinate[0]
            elif kind == 'latitude':
                return coordinate[1]

        df['latitude'] = df.place.apply(place_to_coordinate, kind='latitude')
        df['longitude'] = df.place.apply(place_to_coordinate, kind='longitude')

        return df

    def preprocess(df):
        return (df.pipe(df.datetimeify)
                .pipe(df.sentiment)
                .pipe(df.influence)
                .pipe(df.influenced_polarity)
                .pipe(df.georeference))

    def preprocess_df(df):
        cleaned = df.pipe(df.clean)
        copy = cleaned.copy()
        return df.preprocess(copy)

    def load_df(input_filename, df):
        raw_df = pd.read_csv(input_filename, engine='python')
        return df.preprocess_df(raw_df)
