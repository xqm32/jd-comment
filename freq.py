import wordcloud

freq = dict()
with open("comments/part-r-00000", "r") as f:
    for i in f.readlines():
        k, v = i.split()
        freq[k] = int(v)

wordcloud.WordCloud(
    font_path="SourceHanSerifSC-Light.otf", width=1920, height=1200
).generate_from_frequencies(freq).to_file("wordcloud.png")
