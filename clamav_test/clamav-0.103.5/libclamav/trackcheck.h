#ifndef _TRACK_CHECK_H
#define _TRACK_CHECK_H

#include "regex/regex.h"
#include "htmlnorm.h"

#define CL_TRACK_BASE 100
enum track_status { CL_TRACK_NODECISION = 0,
                    CL_TRACK_CLEAN      = CL_TRACK_BASE,
                    CL_PHISH_CLOAKED_UIU,
                    CL_PHISH_NUMERIC_IP,
                    CL_PHISH_HEX_URL,
                    CL_PHISH_CLOAKED_NULL,
                    CL_PHISH_SSL_SPOOF,
                    CL_TRACK_NOMATCH,
                    CL_PHISH_HASH0,
                    CL_PHISH_HASH1,
                    CL_PHISH_HASH2 };

#define CHECK_SSL 1
#define CHECK_CLOAKING 2
#define CLEANUP_URL 4
#define CHECK_IMG_URL 8

#define LINKTYPE_IMAGE 1

#define CL_PHISH_ALL_CHECKS (CLEANUP_URL | CHECK_SSL | CHECK_CLOAKING | CHECK_IMG_URL)

struct string {
    struct string* ref;
    char* data;
    int refcount;
};

struct phishcheck {
    regex_t preg_numeric;
    int is_disabled;
};

struct pre_fixup_info {
    /* pre_* url before fixup_spaces */
    struct string pre_displayLink;
    size_t host_start;
    size_t host_end;
};

struct url_check {
    struct string realLink;
    struct string displayLink;
    struct pre_fixup_info pre_fixup;
    unsigned short flags;
    unsigned short always_check_flags;
    unsigned short link_type;
};

cl_error_t trackingScan(cli_ctx* ctx, tag_arguments_t* hrefs);

void track_disable(struct cl_engine* engine, const char* reason);
enum track_status cli_url_canon(const char* inurl, size_t len, char* urlbuff, size_t dest_len, char** host, size_t* hostlen, const char** path, size_t* pathlen);
/* end of non-thread-safe functions */

#endif