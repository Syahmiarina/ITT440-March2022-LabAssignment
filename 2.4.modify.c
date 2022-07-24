#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>
#include<stdlib.h>

void Done(){
	printf("Job is done \n");
}

void Task(){
	char task[20];

	printf("name : ");
	fgets(task,20,stdin);
	printf("name - %s", task);
}

int main(void){
	for(int x = 0; x <=  3; x++){
		pid_t pid = fork();
		
		if(pid == 0){
			Task();
			exit(EXIT_SUCCESS);
		}
	
		else{
			printf("\n");
			wait(NULL);
		}
	}
	Done();
	return 0;
}
