echo "Menghitung Nilai IPK Mahasiswa"
read nilai;
echo "input: $nilai"

datasatu[0]=4

datadua[0]=2

datatiga[0]=$nilai

echo ${datasatu[*]}
echo ${datadua[*]}
echo ${datatiga[*]}

a=$datasatu
b=$datadua
c=$datatiga

let d=$a+$b+$c
jumlah_data=3
let ipk_mhs=$d/$jumlah_data

printf "IPK mhs = $d / $jumlah_data \n"
printf "IPK mhs = $ipk_mhs \n"
