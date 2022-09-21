
from pytube import YouTube

def video_indir():
    url=YouTube(input("Lütfen indirmek istediğiniz videonun linkini yapıştırınız: "))
    indirme_bağlantısı=url.streams.filter(progressive="True").first()
    indirme_bağlantısı.download()
    print("-"*45)
    print(f"Video Başlığı: {url.title}")
    print("videonun sahibi: ",url.author)
    print("Videonun izlenme sayısı: ",url.views)
    print("Videonun uzunluğu: ",url.length,"saniye")
    print("-"*45)


    
    
video_indir()
    