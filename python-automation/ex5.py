from jenkinsapi.jenkins import Jenkins

def getSCMInfroFromLatestGoodBuild(url, jobName, username="akhil", password=123):
    J = Jenkins(url, username, password)
    job = J[jobName]
    lgb = job.get_last_good_build()
    return lgb.get_revision()

if __name__ == '__main__':
    print (getSCMInfroFromLatestGoodBuild('http://44.200.182.151:8080/', 'pipeline'))     
