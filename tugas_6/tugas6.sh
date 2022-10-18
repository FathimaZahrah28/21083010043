
printf "haloo, berpa jumlah pelajaran?? "
read input
declare -a nilai
i=0
while [ $i -lt $input ]
do 
   printf " masukkan nilai ";
   read a;
   nilai[$i]=$a;
   let i=$i+1;
done
p=0
l=0
while [ $l -lt $input ]
do
   let p=$p+${nilai[$l]};
   let l=$l+1
done
let hasil=$p/$input
echo "SelamaT IPKmu $hasil"
