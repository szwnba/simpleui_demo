# from matplotlib import font_manager
from urllib import request
import json

def get_jobs_data():
    url = 'http://192.168.31.85:9001/view/test/api/json?tree=jobs[name,url,inQueue,color,lastBuild[number,building,duration,estimatedDuration,result,url]]'
    req = request.Request(url)
    rsp = request.urlopen(req)
    res = rsp.read()
    res_json = json.loads(res)
    # print(res_json)
    job_list = []
    for dict in res_json['jobs']:
        job = {}
        job['name'] = dict['name']
        job['joburl'] = dict['url']
        job['inQueue'] = bool(dict['inQueue'])
        job['color'] = dict['color']
        job['number'] = int(dict['lastBuild']['number'])
        job['building'] = bool(dict['lastBuild']['building'])
        job['duration'] = int(dict['lastBuild']['duration'])/1000/60
        job['estimatedDuration'] = int(dict['lastBuild']['estimatedDuration'])/1000/60
        job['result'] = dict['lastBuild']['result']
        job['buildurl'] = dict['lastBuild']['url']
        job_list.append(job)
    return job_list

if __name__ == '__main__':
    my_list = []
    my_list = get_jobs_data()
    print("datetime.now()")

