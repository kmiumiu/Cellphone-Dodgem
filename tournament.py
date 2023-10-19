no_of_stalls = [2, 3, 20, 30, 100]
no_of_obstacles = [0, 50, 200]
players = ['1 2 3 4 5 6',\
           '1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6',\
           '1 1 1 1 1 1 2 2 2 2 2 2 3 3 3 3 3 3 4 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6 ',
           '1 1 1 1 1 1',
           '2 2 2 2 2 2',
           '3 3 3 3 3 3',
           '4 4 4 4 4 4',
           '5 5 5 5 5 5',
           '6 6 6 6 6 6',
           '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
           '2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2',
           '3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3',
           '4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4',
           '5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5',
           '6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6',
           '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
           '2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2',
           '3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3',
           '4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4',
           '5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5',
           '6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6']

theta = [1, 2, 3]

with open('tournament_1.sh', 'w') as f:
    f.write('start=$(date +%s)\n')

with open('tournament_2.sh', 'w') as f:
    f.write('start=$(date +%s)\n')

with open('tournament_3.sh', 'w') as f:
    f.write('start=$(date +%s)\n')

total = len(no_of_stalls) * len(no_of_obstacles) * len(players) * len(theta)
count = 0
for p in players:
    for nv in no_of_stalls:
        for no in no_of_obstacles:
            for t in theta:
                count += 1
                with open('tournament_1.sh', 'a') as f:
                    f.write('echo -e "\n\nRun ' + str(count) + '/' + str(total) + '"' + '\n')
                    f.write('python3 main.py --gui False -ns ' + str(nv + no) + ' -nv ' + str(nv) + ' -p ' + str(p) + ' --theta ' + str(t) + " --seed 5\n")
                    f.write('cat logs/game_config.txt >> tournament_results.txt\n')
                    f.write('cat logs/result.txt >> tournament_results.txt\n')
count = 0
for p in players:
    for nv in no_of_stalls:
        for no in no_of_obstacles:
            for t in theta:
                with open('tournament_2.sh', 'a') as f:
                    f.write('echo -e "\n\nRun ' + str(count) + '/' + str(total) + '"' + '\n')
                    f.write('python3 main.py --gui False -ns ' + str(nv + no) + ' -nv ' + str(nv) + ' -p ' + str(p) + ' --theta ' + str(t) + " --seed 2\n")
                    f.write('cat logs/game_config.txt >> tournament_results.txt\n')
                    f.write('cat logs/result.txt >> tournament_results.txt\n')
count = 0
for p in players:
    for nv in no_of_stalls:
        for no in no_of_obstacles:
            for t in theta:
                with open('tournament_3.sh', 'a') as f:
                    f.write('echo -e "\n\nRun ' + str(count) + '/' + str(total) + '"' + '\n')
                    f.write('python3 main.py --gui False -ns ' + str(nv + no) + ' -nv ' + str(nv) + ' -p ' + str(p) + ' --theta ' + str(t) + " --seed 3\n")
                    f.write('cat logs/game_config.txt >> tournament_results.txt\n')
                    f.write('cat logs/result.txt >> tournament_results.txt\n')

with open('tournament_1.sh', 'a') as f:
    f.write('end=$(date +%s)\necho "Elapsed Time: $(($end-$start)) seconds" >> time.txt')

with open('tournament_2.sh', 'a') as f:
    f.write('end=$(date +%s)\necho "Elapsed Time: $(($end-$start)) seconds" >> time.txt')

with open('tournament_3.sh', 'a') as f:
    f.write('end=$(date +%s)\necho "Elapsed Time: $(($end-$start)) seconds" >> time.txt')
