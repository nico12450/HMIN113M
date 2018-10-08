for i in *
do
    echo $i
    
    if [grep "bonjour" $i] && [test ${i##*.} = "txt"]
    then
	echo "trouvé"
	mv i /dump
    fi
done
