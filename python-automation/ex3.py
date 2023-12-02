"""Disable a Jenkins job"""
def disable_job():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    job_name = 'nightly-build-job'
    if (server.has_job(job_name)):
        job_instance = server.get_job(job_name)
        job_instance.disable()
        print ('Name:%s,Is Job Enabled ?:%s' % (job_name,job_instance.is_enabled()))
