#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
int infinite_while(void);

/**
 * main - print main function
 *
 * Return: void function
 */
int main(void)
{
	int a = 0;

	while (a < 5)
	{
		if (fork() != 0)
			printf("Zombie process created, PID: ZOMBIE_PID: %ld\n", (long)getpid());
		else
			return (0);
		a++;
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - indefinite while loop
 *
 * Return: void function
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
