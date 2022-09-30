echo "Bilangan positif ganjil 1-15 dengan bilangan acuan 15"
read ganjil;
echo "input: $ganjil"

a=$ganjil
while [ $a -gt 0 ]
do
  echo $a
  a=$((a-2))
done
