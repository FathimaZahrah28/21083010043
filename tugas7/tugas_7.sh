input() {
     echo "haiii masukkan panjang persegimu yuk"
     read a
     echo "masukkan lebar persegimu yuk"
     read b
     luaspersegi $a $b
}

luaspersegi() {
          parameter1=$1
          parameter2=$2
          echo "panjang persegi $parameter1"
          echo "lebar persegi $parameter2"
          let luas=$parameter1*$parameter2
          echo " luas persegi ini adalah $luas "
}

input
