printf "Jajan apa yang kamu suka ?\n"
printf "pentol ?\n"
printf "batagor ?\n"
printf "cireng ?\n"

read jajan

case "$jajan" in
  "pentol")
    echo "pentol buk mah wenak slur!"
    ;;
  "batagor")
    echo "Batagor e mas budi mantap bat"
    ;;
  "cireng")
    echo "cirenge kantin rasane unch banget"
    ;;
  *)
    echo "makanan yang kamu suka gaenak ih WKWK"
esac
