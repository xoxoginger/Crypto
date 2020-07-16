/*********************************************************************
* Filename:   sha256.c
* Author:     Brad Conte (brad AT bradconte.com)
* Copyright:
* Disclaimer: This code is presented "as is" without any guarantees.
* Details:    Performs known-answer tests on the corresponding SHA1
	          implementation. These tests do not encompass the full
	          range of available test vectors, however, if the tests
	          pass it is very, very likely that the code is correct
	          and was compiled properly. This code also serves as
	          example usage of the functions.
*********************************************************************/

/*************************** HEADER FILES ***************************/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdbool.h>
#include "sha256.h"

/*********************** FUNCTION DEFINITIONS ***********************/
int	sha256_test(const BYTE text[], char filename[]) {

    BYTE buf1[SHA256_BLOCK_SIZE];

    BYTE buf2[SHA256_BLOCK_SIZE];

    SHA256_CTX ctx;

    FILE* f = fopen(filename, "wb");

    if (f) {
        size_t text_length = strlen(text);

        sha256_init(&ctx);

        sha256_update(&ctx, text, text_length, 16); sha256_final(&ctx, buf1, 16);

        for (size_t times = 17; times <= 64; times++) {
            sha256_init(&ctx);

            sha256_update(&ctx, text, text_length, times); sha256_final(&ctx, buf2, times);
            size_t cnt = 0;

            for (int i = 0; i < SHA256_BLOCK_SIZE; i++) {
                for (int j = 0; j < 8; j++) {

                    if (((buf1[i] << j) & 0x80) != ((buf2[i] << j) & 0x80)) {

                        cnt++;

                    }
                }

            }
            fprintf(f, "%d %d\n", times, cnt);

            strncpy(buf1, buf2, SHA256_BLOCK_SIZE);
            buf1[SHA256_BLOCK_SIZE - 1] = '\0';
        }

        fflush(f);
        fclose(f);
    }
    else {
        printf("Can't open file.");
    }

    return 1;
}


int main()
{
    // 2 chars
    BYTE text1[] = { "ju" };

    char filename1[] = { "C:/Users/hui/Desktop/diffs1.csv" }; sha256_test(text1, filename1);
    // 20 chars
    BYTE text2[] = { "heygoodnewseveryone!" };

    char filename2[] = { "C:/Users/hui/Desktop/diffs2.csv" }; sha256_test(text2, filename2);

    // 200 chars
    BYTE text3[] =

    { "hello,darkness,myoldfriend/i'vecometotalkwithyouagain/becauseavisionsoftlycreeping/leftitsseedswhileiwassleeping/andthevisionthatwasplantedinmybrain/stillremains/withinthesoundofsilence/soundofsilence" };

    char filename3[] = { "C:/Users/hui/Desktop/diffs3.csv" }; sha256_test(text3, filename3);
    return 0;
}