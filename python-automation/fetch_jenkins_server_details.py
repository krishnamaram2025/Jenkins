from jenkinsapi.jenkins import Jenkins

def getSCMInfroFromLatestGoodBuild(url, jobName, username="akhil", password=123):
    J = Jenkins(url, username, password)
    job = J[jobName]
    lgb = job.get_last_good_build()
    return lgb.get_revision()

if __name__ == '__main__':
    print (getSCMInfroFromLatestGoodBuild('http://44.200.182.151:8080/', 'pipeline'))     


def get_plugin_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for plugin in server.get_plugins().values():
        print ("Short Name:%s" % (plugin.shortName))
        print ("Long Name:%s" % (plugin.longName))
        print ("Version:%s" % (plugin.version))
        print ("URL:%s" % (plugin.url))
        print ("Active:%s" % (plugin.active))
        print ("Enabled:%s" % (plugin.enabled))

"""Disable a Jenkins job"""
def disable_job():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    job_name = 'nightly-build-job'
    if (server.has_job(job_name)):
        job_instance = server.get_job(job_name)
        job_instance.disable()
        print ('Name:%s,Is Job Enabled ?:%s' % (job_name,job_instance.is_enabled()))


"""Get job details of each job that is running on the Jenkins instance"""
def get_job_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for job_name, job_instance in server.get_jobs():
        print ('Job Name:%s' % (job_instance.name))
        print ('Job Description:%s' % (job_instance.get_description()))
        print ('Is Job running:%s' % (job_instance.is_running()))
        print ('Is Job enabled:%s' % (job_instance.is_enabled()))



