def solution(genres, plays):
    answer = []
    genres_total = dict()
    genre_songs = dict() 
    
    for i in range(0, len(genres)):
        if genres[i] not in genres_total:
            genres_total[genres[i]] = 0
            genre_songs[genres[i]] = []
        genres_total[genres[i]] += plays[i]
        genre_songs[genres[i]].append([i, plays[i]])
        
    genres_sorted = sorted(genres_total, key = lambda x:genres_total[x], reverse=True)
    
    for genre in genres_sorted:
        genre_songs[genre].sort(key = lambda x: (x[1], -x[0]), reverse=True)
        for song in genre_songs[genre][:2]:
            answer.append(song[0])
            
    return answer

