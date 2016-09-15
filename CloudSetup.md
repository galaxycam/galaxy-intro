# Cloud Setup

## Galaxy on the cloud

* [Cloud](https://wiki.galaxyproject.org/Cloud)
* [CloudMan](https://wiki.galaxyproject.org/CloudMan)

## Setup for training workshop

It is recommended to have 10 users per head node, so for 30 people it is best to have 3 head nodes (separate instances) with 10 workers each of type c3.2x large.


## Amazon Cloud

[AWS](https://console.aws.amazon.com/ec2)

Get your Access Key Id from https://console.aws.amazon.com/iam

_Credentials:_
* account name: my work email address
* password: ... stored in DashLane ...

## Setup steps

* (1) Launch a Galaxy Cloud instance https://launch.usegalaxy.org/

| Setup Keys        | Values |
| ----------------- | ------ |
| Access Key Id     | AKIAILEQVNU6GGPMXUGA    |
| Secret Access Key | bsV...                  |
| Cluster Name      |	galaxycam_201609        |
| Cluster Password  | training                |
| Instance Type     |	Compute optimized 2x large (c3.2xlarge) (8vCPU/15GB RAM/80GB SSD) (c3.2x large recommended by Dave) |


* (2) Take note of newly created Galaxy server's IP address
  - IP address: `52.207.211.93`
  - http://52.207.211.93/cloud; credentials: ubuntu | training


* (3) Create Galaxy admin account
  - Go to CloudMan admin console http://52.207.211.93/cloud/root/admin
  - Enter email address for admin account
  - Galaxy server will be restarted automatically
  - Go to Galaxy and Register as a new user and login as admin


* (4) Install tools in Galaxy
  - charts (update charts in Admin > Manage installed tool shed repositories)
  - **Already installed.** column_maker (under Text Manipulation > new tool called 'Compute')
  - **Already installed.** ucsc_custom_track (under Graph/Display Data)
  - Needed to import workflow https://usegalaxy.org/u/galaxyproject/p/galaxy-variant-101
    - Add or Replace Groups, id toolshed.g2.bx.psu.edu/repos/devteam/picard/picard_ARRG/1.56.0, version 1.56.0 - 2 (2014-02-21) from Galaxy Test tool shed
    - Merge BAM Files, id toolshed.g2.bx.psu.edu/repos/devteam/sam_merge/sam_merge2/1.1.2, version 1.1.2, version 0 (2013-08-26) from Galaxy Main tool shed
    - FreeBayes, id toolshed.g2.bx.psu.edu/repos/devteam/freebayes/freebayes/0.0.3, version 0.0.3, version 1 (2013-12-16) from Galaxy Test tool shed


* (5) Install training course data and test
  - Generate API key in Galaxy and paste it into [the script](https://github.com/galaxycam/galaxy-intro/blob/master/create_data_libraries.py) which upload data into Galaxy.
  - Create data libraries in Galaxy
  ```
  ssh ubuntu@52.207.211.93
  virtualenv venv
  source venv/bin/activate
  pip install bioblend
  git clone https://github.com/galaxycam/galaxy-intro.git
  cd galaxy-intro
  python create_data_libraries.py
  ```
  - Go through all training materials at http://tinyurl.com/GalaxyCamPractical from course website  http://galaxycam.github.io/

* (6) Share instance
  - on the first cloudman instance http://52.207.211.93/cloud click on 'Add nodes' to get 10 workers & check on amazon EC2 dasboard > Instances if workers started
  - on http://52.207.211.93/cloud click on share icon next to the cluster name, then 'Share-an-instance', select 'Public' and click 'share-an-instance'


* (7) Create a new instance
  - Go to https://launch.usegalaxy.org/ and use shared instance named `cm-10b6c9703d6981ec5f1cd7c4f7be25a8/shared/2016-03-14--18-32/`


* (8) Update training materials with new IP addresses.

* (9) Check cost
