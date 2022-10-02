select minuman in teh kopi air jus susu semua gada
do
  case $minuman in
    teh|kopi|air|semua)
      echo "maaf abis"
      ;; 
    jus|susu)
      echo "tersedia"
    ;; 
    gada)
      break
    ;;
    *) echo "tidak ada didaftar menu"
    ;;
  esac
done
