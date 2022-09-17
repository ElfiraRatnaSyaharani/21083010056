a=80
b=75

if [ $a -lt $b ]
then
  echo "Anda perlu mengulang tes"
elif [ $a -gt $b ]
then
  echo "Anda tidak perlu mengulang tes"
else
  echo "Tidak ada kondisi yang memenuhi"
fi
