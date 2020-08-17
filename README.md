
## Caching a CMS Response with Cloud Functions

I am currently using CMS's in multiple projects. However,
the data does not change constantly and therefore the 
`json`-response of the CMS can be cached.

Why should I not permanently use the CMS-Server? Option 1: 
Having the CMS-Server on standby causes annoying initial 
load times. Options 2: Constantly running the CMS-Server 
is very pricey.

I have implemented a http-trigger in the CMS. Every time
the data changes, this cloud function gets called. The 
Function fetches a bunch of CMS-routes and stores them
in a google storage bucket.

You can set the cached routes with environment variables
in the `.env` file.

Be sure to disable caching (either on the google storage 
bucket - can be quite annoying to set up - or on the fetching
side).

With this I only have to run the CMS-Server when I am working 
on the data and can even trigger the `build-cms-data`-script
manually and control the data rebuild by disabling the 
auto-rebuild hook.

I also got the initial load times from >7s to <1s :)

You can find scripts for *deploying*, *setting CORS policies*  
and *making all files inside a bucket puplic* in the directory  
`bash-scripts`.
