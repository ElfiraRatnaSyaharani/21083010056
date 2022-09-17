printf "Apa wujud benda meja? \n"
printf "benda cair? \n"
printf "benda padat? \n"
printf "benda gas? \n"

read wujud

case "$wujud" in
  "benda cair")
    echo "Jawaban anda salah"
    ;;
  "benda padat")
    echo "Jawaban anda benar"
    ;;
  "benda gas")
    echo "Jawaban anda salah"
    ;;
  *)
    echo "Jawaban tidak sesuai"
    ;;
esac

