import re
import pandas as pd
def processor( data):
    patterns = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(patterns, data)[1:]
    dates = re.findall(patterns, data)
    df = pd.DataFrame({'messages': messages, "dates": dates})

    # convert date into format
    df['dates'] = pd.to_datetime(df['dates'], format='%d/%m/%Y, %H:%M - ')

    texts = []
    user = []
    for i in df['messages']:
        entry = re.split('([\w\W]+?):\s', i)
        if entry[1:]:
            texts.append(entry[2])
            user.append(entry[1])
        else:
            user.append("Notification")
            texts.append(entry[0])
    df['messages'] = texts
    df['user'] = user
    df['day']=df['dates'].dt.day_name()
    df['date_only']=df['dates'].dt.date
    df['year'] = df['dates'].dt.year
    df['month'] = df['dates'].dt.month_name()
    df['date'] = df['dates'].dt.day
    df['hour'] = df['dates'].dt.hour
    df['minute'] = df['dates'].dt.minute
    return df