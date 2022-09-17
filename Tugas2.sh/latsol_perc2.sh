a=5
b=7
let c=$a*$b

printf "Berapa hasil dari 5 x 7? \n"
printf "Hasilnya adalah 30 \n"
printf "Hasilnya adalah $c \n"
printf "Hasilnya adalah 40 \n"

read hasil

case $hasil in
  "Hasilnya adalah 30")
    echo "Jawaban salah"
    ;;
  "Hasilnya adalah $c")
    echo "Jawaban benar"
    ;;
  "Hasilnya adalah 40")
    echo "Jawaban salah"
    ;;
  *)
    echo "Jawaban tidak ada"
    ;;
esac




