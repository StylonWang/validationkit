#include <stdio.h>
#include <signal.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>

/* sleep() can be implemented with alarm() so this example might not work in that case.
 *
 */

void signal_handler(int signo)
{
	if(signo == SIGALRM) {
		printf("SIGALRM simulating timer/interrupt\n");
		printf("processing for 3 seconds and blocks main loop\n");
		sleep(3);
		alarm(3); // re-install SIGALRM
		printf("SIGALRM done\n");
	} else {
		printf("Got signal %d\n", signo);
	}
}

int main(int argc, char **argv)
{

	if (signal(SIGALRM, signal_handler)) {
		printf("cannot install signal handler: %s\n", strerror(errno));
		exit(1);
	}

	alarm(3); // fire SIGALRM in 3 seconds

	while(1) {
		printf("main loop running...\n");
		sleep(1);
	}

}
