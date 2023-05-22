#ifndef _TRACK_DOMAINCHECK_DB_H
#define _TRACK_DOMAINCHECK_DB_H
#include "clamav.h"

int init_track_list(struct cl_engine* engine);
void track_list_done(struct cl_engine* engine);
void track_list_cleanup(const struct cl_engine* engine);
int is_track_list_ok(const struct cl_engine* engine);
int track_list_match(const struct cl_engine* engine, char* real_url, const char* display_url, const struct pre_fixup_info* pre_fixup, int hostOnly);

#endif