import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="proje_brute"
)
mycursor = mydb.cursor()

def esitmi(mycursor):
  mycursor.execute("SELECT sifre FROM kullanici")
  dosya=open("pass.txt","r")
  liste=dosya.readlines()
  myresult=mycursor.fetchall()
  for i in myresult:
    for j in liste:
      x = j.rstrip()
      print(">>> ",x)
      if x==i[0]:
        print("Eşleşme Başarılı Şifreniz:: ",i[0],"\n")
        break

def ipuculu1(mycursor):
  ipucu=str(input("İpucunuzu Griniz: "))
  dosya2=open("pass.txt","r")
  liste2=dosya2.readlines()
  for j in liste2:
    x = j.rstrip()
    y=x.find(ipucu)
    if(y==0):
      dosya3=open("pass2.txt","a")
      dosya3.writelines(x+"\n")

def ipuculu2(mycursor):
  dosya3=open("pass2.txt","r")
  liste3=dosya3.readlines()
  mycursor.execute("SELECT sifre FROM kullanici")
  myresult=mycursor.fetchall()
  for i in myresult:
    for j in liste3:
      x = j.rstrip()
      print(">>> ",x)
      if x==i[0]:
        print("Eşleşme Başarılı Şifreniz:: ",i[0],"\n")
        break

while(True):
    print(30*"*")
    islem=int((input("[1] Kisi Ekle\n[2] Sifre Bul\n[3] Çıkış\nYanitiniz:: ")))
    print(30*"*")
    if islem==1:
      kul_adi=str(input("Kullanici Adı Giriniz: "))
      sifre=str(input("şifre Giriniz: "))
      sql = "INSERT INTO kullanici (id,adi,sifre) VALUES ('',%s, %s)"
      val = (kul_adi, sifre)
      mycursor.execute(sql,val)
      mydb.commit()
    elif (islem==2):
      print(30*"*")
      islem2=int((input("[1] İpucu Girerek Bul\n[2] İpucu Girmeden Bul\n[3] Çıkış\nYanitiniz:: ")))
      print(30*"*")
      if (islem2==1):
        ipuculu1(mycursor)
        ipuculu2(mycursor)
        os.remove("pass2.txt")
      elif(islem2==2): 
        esitmi(mycursor)
      elif (islem2==3):
        pass
    elif (islem==3):
      break
