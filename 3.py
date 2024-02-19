gaji =int (input("gaji per jam : Rp."))
jam_kerja = int (input("jam kerja per minggu :"))

gaji_total = gaji * jam_kerja * 5
pajak = gaji_total - 0.14 * gaji_total
print (f"pendapatan sebelum bayar pajak adalah Rp.{gaji_total}")
print (f"pendapatan setelah bayar pajak adalah Rp.{pajak}")
acc = 0.10*pajak
hacc = pajak - acc
print (f"jumlah uang  untuk beli aksesoris adalah Rp.{acc}")
alattulis = 0.01*pajak
halattulis = hacc - alattulis
print (f"jumlah uang untuk beli alat tulis adalah Rp.{alattulis}")
sedekah  = 0.25* halattulis
print(f"jumlah uang untuk sedekah adalah Rp.{sedekah}")
yatim = sedekah%1000
hyatim = (sedekah - yatim) *0.3
print(f"jumlah uang untuk yatim adalah Rp.{hyatim}")
dhuafa = sedekah%1000
hdhuafa = (sedekah - dhuafa)*0.7
print(f"jumlah uang untuk dhuafa adalah Rp.{hdhuafa}")