python main.py 1 1 0 ./results/multiply_8000_0/ ./reduced_8000 &
python main.py 1 1 0 ./results/multiply_8000_1/ ./reduced_8000 &
python main.py 1 1 0 ./results/multiply_8000_2/ ./reduced_8000 &
python main.py 1 1 0 ./results/multiply_8000_3/ ./reduced_8000 &
python main.py 1 1 0 ./results/multiply_8000_4/ ./reduced_8000 &

wait 

ls -la

shutdown now
