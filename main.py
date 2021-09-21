from pytube import Search

title = "Despacito"

s = Search(title)
youtubeVideo = s.results[0]
sound = youtubeVideo.streams.filter(type = 'audio').order_by('abr').desc().first()
sound.download(title)
