########### get user_history ####
hadoop jar /usr/local/hadoop/lib/hadoop-mapred-1.1.2.jar org.apache.hadoop.streaming.HadoopStreaming -D mapred.output.compress=0  -D mapred.reduce.tasks=200 -input $recom_dir/input/* -output $recom_dir/user_history -mapper ./mapper_user_history.py -reducer ./reducer_user_history.py -file $base_dir/mapper_user_history.py -file $base_dir/reducer_user_history.py 

################ get item-item pair #########
hadoop jar /usr/local/hadoop/lib/hadoop-mapred-1.1.2.jar org.apache.hadoop.streaming.HadoopStreaming -D mapred.output.compress=0 -D mapred.reduce.tasks=200 -input $recom_dir/user_history/part* -output $recom_dir/pair -mapper ./mapper_pair.py -reducer ./reducer_pair.py -file $base_dir/mapper_pair.py -file $base_dir/reducer_pair.py

######### get item click-count ########
#### a user may click a item twice, should set it to 1;
hadoop jar /usr/local/hadoop/lib/hadoop-mapred-1.1.2.jar org.apache.hadoop.streaming.HadoopStreaming -D mapred.output.compress=0  -D mapred.reduce.tasks=200 -input $recom_dir/user_history/part* -output $recom_dir/single -mapper ./mapper_single.py -reducer ./reducer_single.py -file $base_dir/mapper_single.py -file $base_dir/reducer_single.py

########## put item click_count in a dict ########
hadoop fs -text $recom_dir/single/part* | hadoop fs -put -f - $recom_dir/single.txt

########## cal similarity between item-item pair #######
hadoop jar /usr/local/hadoop/lib/hadoop-mapred-1.1.2.jar org.apache.hadoop.streaming.HadoopStreaming -files hdfs://webdm-cluster/$recom_dir/single.txt -D mapred.output.compress=0 -D mapred.reduce.tasks=200 -input $recom_dir/pair/part* -output $recom_dir/sim -mapper ./mapper_sim.py -reducer ./reducer_sim.py -file $base_dir/mapper_sim.py -file $base_dir/reducer_sim.py 

####### get the neariest neighour ########
hadoop jar /usr/local/hadoop/lib/hadoop-mapred-1.1.2.jar org.apache.hadoop.streaming.HadoopStreaming -D mapred.output.compress=0 -D mapred.reduce.tasks=200 -input $recom_dir/sim/part* -output $recom_dir/cur_cf_result -mapper ./mapper_neighbor.py -reducer ./reducer_neighbor.py -file $base_dir/mapper_neighbor.py -file $base_dir/reducer_neighbor.py

