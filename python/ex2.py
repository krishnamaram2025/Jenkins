"""Get job details of each job that is running on the Jenkins instance"""
def get_job_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for job_name, job_instance in server.get_jobs():
        print ('Job Name:%s' % (job_instance.name))
        print ('Job Description:%s' % (job_instance.get_description()))
        print ('Is Job running:%s' % (job_instance.is_running()))
        print ('Is Job enabled:%s' % (job_instance.is_enabled()))
