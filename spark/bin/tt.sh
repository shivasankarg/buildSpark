rm -rf testFiles
# ./spark-submit --master local[1] test.py > testLogg.txt
./spark-submit --master local[6] test.py
# ./spark-submit --master local[1] --num-executors 1 test.py
# sleep 1
#jconsole `jps | grep SparkSubmit | awk '{print $1;}'`
