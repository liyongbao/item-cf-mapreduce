# item-cf-mapreduce
# item-cf with python in map/reduce
example:

cat input |./mapper_user_history.py |sort -k1,1 |./reducer_user_history.py > user_history
cat user_history |./mapper_pair.py |sort -k1,1 |./reducer_pair.py > pair
cat user_history |./mapper_single.py |sort -k1,1|./reducer_single.py > single.txt
cat pair |./mapper_sim.py |sort |./reducer_sim.py  > sim
cat sim |./mapper_neighbor.py |sort -k1,1|./reducer_neighbor.py > cf.txt
