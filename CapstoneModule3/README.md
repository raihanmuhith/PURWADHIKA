
# Note

Apabila ingin menggunakan model yang telah dibangun, anda dapat secara langsung menggunakan file "model.pkl". Namun dengan catatan, terdapat limitasi variabel pada data pengujian, yaitu model hanya menerima data yang memiliki variabel Type, Make, Gear_Type, Origin, Options, Year, Engine_Size, Mileage, dan Price. Contoh data yang diterima beserta demonstrasi penggunakan file "model.pkl" dapat dilihat pada fie "TestPickle.ipynb".


# Context

<b>Syarah</b> adalah pasar online untuk menjual mobil di negara Arab Saudi. <b>Syarah</b> memposisikan diri sebagai pihak ketiga atau media dalam mempromosikan penjualan mobil bekas, membantu bisnis dan individu membeli mobil mereka dengan mudah dan secepat mungkin. Sehingga dapat dikatakan terdapat 3 Aktor pada proses bisnisnya, yaitu Syarah, Penjual, dan Pembeli. Penjual akan mengiklankan mobilnya yang ingin dijual melalui Syarah, begitu juga Pembeli yang membeli Mobil bekas yang diiklankan melalui Syarah. Penjual dapat secara bebas mengiklankan Mobilnya dengan mendefinisikan spesifikasi-spesifikasi mobil serta <b> harga</b> untuk diiklankan melalui Syarah. Nah, Hal ini terkadang menyulitkan penjual yang tidak mengetahui kisaran harga mobil bekas di pasaran. Apabila penjual memberikan harga mobil yang terlalu mahal dibanding mobil-mobil lainnya dengan spesifikasi sejenis, khawatir peminat untuk iklan tersebut sedikit atau bahkan tidak ada sama sekali. Sedangkan apabila penjual memberikan harga mobil terlalu murah dibanding mobil-mobil lainnya dengan spesifikasi sejenis, maka penjual akan mendapatkan keuntungan yang tidak sepadan. 

Sebagai Bisnis Owner yaitu Syarah, melihat harga jual mobil yang tidak tepat di pasaran akan berpengaruh juga terhadap perusahaan. Karena salah satu keuntungan yang didapatkan dari bisnis ini adalah biaya iklan dan proporsi keuntungan yang didapat dari penjualan mobil. Jika banyak mobil dengan spesifikasi dikalangannya dijual dengan harga yang terlalu mahal, Pembeli mobil yang melalui situs Syarah akan menurun sehingga keuntungan profit perusahaan juga menurun. Seiring berjalannya waktu, Penjual juga tidak ingin mengiklankan mobil nya di Syarah sebab pengunjung/pembeli situs syarah yang mulai sedikit. Lalu apabila banyak mobil yang dijual dengan harga terlalu murah, perusahaan juga mendapatkan proporsi keuntungan dari penjualan yang kecil.

# Problem

Berdasarkan latar belakang, tantangan yang harus diselesaikan oleh Syarah adalah <b>Bagaimana Cara Syarah membantu menentukan harga jual mobil yang tepat untuk penjual berdasarkan spesifikasi mobilnya?</b>. Dengan begitu penjual hanya perlu memasukkan spesifikasi mobilnya dan secara otomatis, Syarah akan menyarankan harga jual dari mobil tersebut. Nantinya pada  situs Syarah akan ada prediction tool untuk memberikan kemudahan kepada penjual agar harga mobil dengan spesifikasi dikalangannya dijual dengan harga yang tepat. Dengan begitu diharapkan masyarakat merasa percaya terhadap harga jual mobil yang diiklankan di Syarah merupakan harga yang tepat sehingga banyak dari sisi pengunjung dan penjual yang bertransaksi melewati Syarah. Dengan kata lain, semakin banyak transaksi artinya semakin tinggi juga revenue perusahaan, dalam konteks ini didapat dari biaya iklan jika dari sisi penjual dan proporsi keuntungan jual dari sisi pembeli.

# Approach

Analisis Regresi, dimana Analisis regresi dalam statistika adalah salah satu metode untuk menentukan hubungan sebab-akibat antara satu variabel dengan variabel yang lain. Analisis Regresi akan dilakukan dengan menggunakan bantuan machine learning. Sehingga yang menemukan karakteristik pembeda harga mobil satu dengan yang lainnya adalah sebuah model machine learning itu sendiri.



