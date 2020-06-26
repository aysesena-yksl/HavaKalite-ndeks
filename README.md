# HavaKalite-İndeks
### KATI ATIK YOĞUNLU VE HAVA KALİTE İNDEKS
Modern yaşamın getirdiği  şehirleşmenin de  bir sonucu olan hava kirliliği, yerel, bölgesel ve küresel anlamda etki etmektedir. Hava kirliliği insan sağlığı, tarım, toprak kirliliği gibi sorunlara yer açar. Bu çalışmada katı atık yoğunluğu ile hava kalite indeks arasındaki ilişkiyi ele alan bir proje yapılması planlandı. 
### VERİ SETİ
Çalışmada kullanılan hava verileri; 
 Çevre ve Şehircilik Bakanlığı Hava İzleme https://www.havaizleme.gov.tr/ ,   tarafından elde edilmiştir. 
Hava kirliliği ile katı atık yoğunluğunun ele alındığı bu çalışmada Samsun iline ait 3 ilçe üzerinde çalışma yürütüldü.
Çalışmada araştırma yapılan ilçeler ; Atakum, Tekkeköy ve Bafra’dır. Tekkeköy istasyonu ayrıca sanayi bölgesi içinde de yer almaktadır.  
### KATI ATIK VE HAVA KALİTE İNDEKSİ İLİŞKİLERİ
Elde edilen verilerin analiz işlemleri  için aralarındaki ilişkiler grafikler halinde elde edildi. 
Tekkeköy ilçesi için  elde edilen grafik sonuçları; 
   #veritekkekoy.py dosyası: 
   ![](https://github.com/aysesena-yksl/HavaKalite-ndeks/blob/master/4.PNG)
Grafiklere göre katı atık miktarının her geçen gün arttığı gözlemlenebilir ve atmasının bir belirleyici etken vasıtası ile olduğu düşünülebilir. 
Katı atık yoğunluğu ve hava kitle indeksinin ilişkisinin gösterilmesi amacıyla  korelasyon grafikleri kullanılmıştır. 
   ![](https://github.com/aysesena-yksl/HavaKalite-ndeks/blob/master/6.PNG)     ![](https://github.com/aysesena-yksl/HavaKalite-ndeks/blob/master/7.PNG)
Grafikler incelendiğinde Karbonmonoksit(CO) , Kükürtdioksit(SO2) gazları ele alındığında belirli noktalarda yoğunluk gözlenmektedir. Bu görsele göre katı atık ve Karbonmonoksit(CO) gazı incelendiğinde katı atık  yoğunluğunun düzenli bir şekilde Karbonmonoksit(CO) gazı ile ilişkili olduğu tespit edilmiştir. 
Bu durumda Karbonmonoksit(CO) değeri Atık Katı İndeks ve Hava Kalite İndeks arasındaki ilişkide önemli bir rol oynadığı düşünülmektedir. 
### LSTM ALGORİTMASI KULLANILARAK TAHMİN İŞLEMİ 
Tekkeköy ilçesi için kullanılan  #model.py dosyası; 
Elde edilen grafik şu şekildedir; 

   ![](https://github.com/aysesena-yksl/HavaKalite-ndeks/blob/master/lstm.PNG)
