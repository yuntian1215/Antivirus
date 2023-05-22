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
#include "htmlnorm.h"
#include "trackcheck.h"
#include "phish_domaincheck_db.h"
#include "phish_allow_list.h"
#include "regex_list.h"
#include "iana_tld.h"
#include "iana_cctld.h"
#include "scanners.h"
#include <assert.h>

#include "mpool.h"

#define DOMAIN_REAL 1
#define DOMAIN_DISPLAY 0

#define PHISHY_USERNAME_IN_URL 1
#define PHISHY_NUMERIC_IP 2
#define REAL_IS_MAILTO 4
/* this is just a flag, so that the displayed url will be parsed as mailto too, for example
 * <a href='mailto:somebody@yahoo.com'>to:somebody@yahoo.com</a>*/
#define DOMAIN_LISTED 8
#define PHISHY_CLOAKED_NULL 16

static char empty_string[] = "";

static const char dotnet[] = ".net";
static const char adonet[] = "ado.net";
static const char aspnet[] = "asp.net";
/* ; is replaced by ' ' so omit it here*/
static const char lt[]           = "&lt";
static const char gt[]           = "&gt";
static const char src_text[]     = "src";
static const char href_text[]    = "href";
static const char mailto[]       = "mailto:";
static const char mailto_proto[] = "mailto://";
static const char https[]        = "https:";
static const char http[]         = "http:";
static const char ftp[]          = "ftp:";

static const size_t href_text_len    = sizeof(href_text);
static const size_t src_text_len     = sizeof(src_text);
static const size_t dotnet_len       = sizeof(dotnet) - 1;
static const size_t adonet_len       = sizeof(adonet) - 1;
static const size_t aspnet_len       = sizeof(aspnet) - 1;
static const size_t lt_len           = sizeof(lt) - 1;
static const size_t gt_len           = sizeof(gt) - 1;
static const size_t mailto_len       = sizeof(mailto) - 1;
static const size_t mailto_proto_len = sizeof(mailto_proto) - 1;
static const size_t https_len        = sizeof(https) - 1;
static const size_t http_len         = sizeof(http) - 1;
static const size_t ftp_len          = sizeof(ftp) - 1;

static enum track_status trackingCheck(cli_ctx* ctx,struct url_check* urls){
    
}

cl_error_t trackingScan(cli_ctx* ctx, tag_arguments_t* hrefs)
{

}
