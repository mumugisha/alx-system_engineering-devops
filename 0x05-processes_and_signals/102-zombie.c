#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

int infinite_while(void);

/**
 * main - create child processes
 *
 * Return: 0 on success, -1 on failure
 */
int main(void)
{
    int a = 0;
    pid_t pid;

    while (a < 5)
    {
        pid = fork();
        if (pid == -1)
        {
            perror("fork");
            return -1; // Return -1 on failure
        }
        else if (pid == 0) // Child process
        {
            printf("Child process created, PID: %ld\n", (long)getpid());
            // Do some work in the child process before exiting
            return 0; // Return 0 on success
        }
        else // Parent process
        {
            printf("Parent process, PID: %ld\n", (long)getpid());
        }
        a++;
    }

    // Parent process waits for each child process to terminate
    while (wait(NULL) > 0)
        ;

    return 0;
}

/**
 * infinite_while - indefinite while loop
 *
 * Return: 0 on success
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return 0;
}

