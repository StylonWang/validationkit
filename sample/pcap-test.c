#include <stdio.h>
#include <pcap.h>
#include <getopt.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

char g_device[32] = "\0";

int 
main(int argc, char *argv[])
{
    char   *dev, errbuf[PCAP_ERRBUF_SIZE];
    char ch;
    pcap_t *handle;
    char errbuf[PCAP_ERRBUF_SIZE];

    if( 0!=geteuid() ) {
        fprintf(stderr, "This program must be run as root/admin. Abort.\n");
        exit(1);
    }
    
    // parse command line options
    while( ((ch = getopt(argc, argv, "hi:"))) != -1) {
        switch(ch) {
        case 'i':
            strncpy(g_device, optarg, sizeof(g_device));
            break;

        case 'h':
        default:
            fprintf(stderr, "Usage: %s [-h] [-i eth0] \n\n", argv[0]);
            exit(1);
            break;
        }
    }

    if( 0==g_device[0] ) {
        dev = pcap_lookupdev(errbuf);
        if (dev == NULL) {
                fprintf(stderr, "Couldn't find default device: %s\n", errbuf);
                exit(2);
        }
        strncpy(g_device, dev, sizeof(g_device));
    }

    fprintf(stderr, "Use interface: %s\n", g_device);

    handle = pcap_open_live(g_device, BUFSIZE, 1, 1000, errbuf);

    pcap_close(handle);

    return (0);
}
