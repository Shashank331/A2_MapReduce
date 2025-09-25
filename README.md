# Hadoop MapReduce Assignment – Word Count & Non-English Word Filtering
#Tested on Hadoop 3.3.6 (Windows) with Python 3.11.
# Shashank Reddy Muthangi
# DOB:- 05/JULY/2002

##FILES-
- `mapper_wc.py` → Mapper script for word count.
- `reducer_sum.py` → Reducer script to sum word counts.
- `mapper_nonenglish.py` → Mapper script to filter non-English words.
- `english_words.txt` → Dictionary file with ~194,000 English words.
- `input/` → Sample text files (Harry Potter dataset used for testing).
- `output/` → Example output directories.

### 1. Upload Input Files
```bash
hdfs dfs -mkdir -p /user/shash/a2/input
hdfs dfs -put input/file1.txt /user/shash/a2/input/
hdfs dfs -put input/file2.txt /user/shash/a2/input/


###2. Word Count
hadoop jar %HADOOP_HOME%/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-files "mapper_wc.py,reducer_sum.py" \
-mapper "python mapper_wc.py" \
-reducer "python reducer_sum.py" \
-input /user/shash/a2/input/file1.txt \
-output /user/shash/a2/out_wc

###3. Non-English Words
hadoop jar %HADOOP_HOME%/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-files "mapper_nonenglish.py,reducer_sum.py,english_words.txt" \
-mapper "python mapper_nonenglish.py" \
-reducer "python reducer_sum.py" \
-input /user/shash/a2/input/file2.txt \
-output /user/shash/a2/out_nonenglish

###4. View Results
hdfs dfs -get /user/shash/a2/out_wc_final/part-00000 output/wc_result.txt
hdfs dfs -get /user/shash/a2/out_nonenglish/part-00000 output/nonenglish_result.txt



RESULTS-
1. Word Count (wc_result.txt): Produces word frequencies, e.g.
   harry    23
potter   17
voldemort 5
...

2. Non-English Words (nonenglish_result.txt): Detects names/magical terms, e.g.
gryffindor   4
scrimgeour  53
weasley     19
patronus     1


