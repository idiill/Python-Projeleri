from pytube import YouTube



def ses_indir():
    url=YouTube(input("Lütfen indirmek istediğiniz sesin linkini yapıştırınız: "))
    indirme_baglantısı=url.streams.filter(mime_type="audio/mp4").first()
    indirme_baglantısı.download()
    
    


ses_indir()
