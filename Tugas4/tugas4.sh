echo " halo masukkan bilangan"
read input
until [ ! $input -gt 0 ]
do
   let b=$input%2
   if [ $b == 0 ]
   then
     input=$((input-1))
   else
     echo $input
     input=$((input -1))
   fi
done
