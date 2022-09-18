echo " haii\n aku lagi bingung banget nih\n bisa minta tolong kerjain soal ini ngga"
echo " jadi pak budi punya buah, totalnya 10 buah trus dimakan tiga/n trus beli lagi 5./n" 
echo " nah pak budi ini pgn bagi bagi apelnya kecucu cucunya smp habis tpi dgn jumlah yg sama."
echo " brp cucu pak budi yg hrs diundang kerumah agar apelnya habis dg jumlah yg sama satu sama lain."
read jawab
a=10
b=3
c=5
let total=$a-$b+$c
let jadi=$total%$jawab
if [ $jadi == 0 ]
then
  echo "wah makasii yaaw"
else 
  echo "emmm coba itung lagi deh"
fi
