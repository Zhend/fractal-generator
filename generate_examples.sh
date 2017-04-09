#Generate_examples.sh

#eg 1:
bash generate_fan.sh 0 250 0 200 0.524 0.95 0.95 y 6
mv fan.svg eg_fan1.svg


#eg 2:
bash generate_fan.sh -50 250 -100 0 0.15 0.95 0.95 y 0
mv fan.svg eg_fan2.svg

#eg 3:
bash generate_fan.sh 0 -10 -15 0 0.15 1.1 0.95 none 0
mv fan.svg eg_fan3.svg
