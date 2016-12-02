#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <unistd.h>
#include <ao/ao.h>

static ao_device *device;

void device_cleanup(void) {
    ao_close(device);
    ao_shutdown();
}

int main(int argc, char *argv[], char *envp[])
{
    ao_initialize();

    int driver_id = ao_default_driver_id();
    assert(driver_id >= 0);

    ao_sample_format sample_format = {
        8,
        44100,
        2,
        AO_FMT_NATIVE,
        NULL
    };
    device = ao_open_live(driver_id, &sample_format, NULL);
    atexit(device_cleanup);

    while (1) {
        char buf[2048];
        int result = read(0, buf, sizeof(buf));
        if (result == -1 && errno != EAGAIN) {
            fprintf(stderr, "ahem, %s\n", strerror(errno));
            exit(1);
        } else if (result == 0) {
            break;
        } else {
            ao_play(device, buf, result);
        }
    }

    return 0;
}
