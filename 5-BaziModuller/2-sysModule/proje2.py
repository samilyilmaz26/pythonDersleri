import sys
sys.stderr.write("Burası bir hata mesajı\n")
sys.stderr.flush() # Buffer'ı hemen yaz. 
sys.stdout.write("Burası normal çıktımız\n")