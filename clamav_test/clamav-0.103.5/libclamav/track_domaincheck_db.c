#if HAVE_CONFIG_H
#include "clamav-config.h"
#endif

#ifdef CL_THREAD_SAFE
#ifndef _REENTRANT
#define _REENTRANT
#endif
#endif

#include <stdio.h>
#include <string.h>
#include <ctype.h>

#include "clamav.h"
#include "others.h"
#include "phishcheck.h"
#include "track_domaincheck_db.h"
#include "regex_list.h"


int track_list_match(const struct cl_engine* engine, char* real_url, const char* display_url, const struct pre_fixup_info* pre_fixup, int hostOnly)
{
	const char* info;
	int rc = engine->track_list_matcher ? regex_list_match(engine->track_list_matcher, real_url, display_url, hostOnly ? pre_fixup : NULL, hostOnly, &info, 0) : 0;
	return rc;
}

int init_track_list(struct cl_engine* engine)
{
    if (engine) {
        engine->track_list_matcher = (struct regex_matcher*)cli_malloc(sizeof(struct regex_matcher));
        if (!engine->track_list_matcher) {
            cli_errmsg("Phishcheck: Unable to allocate memory for init_domain_list\n");
            return CL_EMEM;
        }
#ifdef USE_MPOOL
        ((struct regex_matcher*)engine->track_list_matcher)->mempool = engine->mempool;
#endif
        return init_regex_list(engine->track_list_matcher, engine->dconf->other & OTHER_CONF_PREFILTERING);
    } else
        return CL_ENULLARG;
}
