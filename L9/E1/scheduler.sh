#! /bin/bash;


#Functions
task_100ms()
{
    echo "task 100ms running"
}

task_1s()
{
    echo "task 1s running"
}

task_5s()
{
    echo "task 5s running"
}

#Var
i=0


while :
do
    task_100ms
    if ((i%10==0)); then
        task_1s
    fi
    if ((i%50==0)); then
        task_5s
    fi
    ((i=i+1))
    sleep 0.1
done