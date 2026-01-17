#include <stdio.h>

int main(int argc, char const *argv[])
{
    FILE *file;
    fopen(file, "w");

    for(int i = 0;i < 200000000; i++)
    {
        fprintf(file, i);
    }
    
    fclose(file);
    return 0;
}
