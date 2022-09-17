a=30
b=3

let c=$a/$b

if [ $c==11 ]
then
  echo "Hasil pembagian benar"
elif [ $c -lt 11 ]
then
  echo "Hasil pembagian salah"
elif [ $c -gt 11 ]
then
  echo "Hasil pembagian salah"
else
  echo "Jawaban tidak sesuai"
fi
