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
| Secret Access Key | bsV... (in rootkey.csv) |
| Cluster Name      |	galaxycam_201609        |
| Cluster Password  | training                |
| Instance Type     |	Compute optimized 2x large (c3.2xlarge) (8vCPU/15GB RAM/80GB SSD) (c3.2x large recommended by Dave) |


* (2) Take note of newly created Galaxy server's IP address
  - IP address: `52.55.43.141`
  - http://52.55.43.141/cloud; credentials: ubuntu | training


* (3) Create Galaxy admin account
  - Go to CloudMan admin console http://52.55.43.141/cloud/root/admin
  - Enter email address for admin account
  - Galaxy server will be restarted automatically
  - Go to Galaxy and Register as a new user and login as admin


* (4) Install tools in Galaxy
  - charts (update charts in Admin > Manage installed tool shed repositories) - latest version from 2015-02-27
  - **Already installed.** column_maker (under Text Manipulation > new tool called 'Compute')
  - **Already installed.** ucsc_custom_track (under Graph/Display Data)


* (5) Install training course data and test
  - Generate API key in Galaxy and paste it into [the script](https://github.com/galaxycam/galaxy-intro/blob/master/create_data_libraries.py) which upload data into Galaxy.
  - Create data libraries in Galaxy from your local computer (no need to login onto the galaxy server)
  ```
  virtualenv venv
  source venv/bin/activate
  pip install bioblend
  git clone https://github.com/galaxycam/galaxy-intro.git
  cd galaxy-intro
  python create_data_libraries.py
  ```
  - Go through all training materials from course website  http://galaxycam.github.io/
    - Check getting_started / NBARC / SequenceInfo.tabular is tabular


* (6) Increase disk space to 800GB when running only one instance to give 40GB to each user.
  - increase disk space on cloudman interface: click on icon 'Grow' to expend disk size
  - activate quota by editing `galaxy.ini` file on server
  ```
  ssh ubuntu@[IP address]
  cd galaxy-app/config
  sudo vi galaxy.ini
  # add these lines at the bottom of the file
  enable_quotas = True
  allow_user_dataset_purge = True
  ```
  - restart Galaxy
  - set quotas from the admin interface of Galaxy to 40GB as default for registered users


* (7) Check you're able to add as many worker nodes as needed and there is no restriction on your Amazon account, otherwise ask for extending the limit to Amazon: c3.2xlarge instances' limit should be set to 40.
  - on the first cloudman instance http://XX.XXX.XXX.XX/cloud click on 'Add nodes' to get 10 workers & check on amazon EC2 dashboard > Instances if workers started


* (8) Create a share instance if you need more than one
  - on http://XX.XXX.XXX.XX/cloud click on share icon next to the cluster name, then 'Share-an-instance', select 'Public' and click 'share-an-instance'


* (9) Create a new instance
  - Go to https://launch.usegalaxy.org/ and use shared instance named `cm-10b6c9703d6981ec5f1cd7c4f7be25a8/shared/2016-03-14--18-32/`


* (10) Update training materials with new IP addresses.

* (11) Check cost

* (12) Turned off all the worker nodes as soon as the course is finished to limit the cost as much as possible.
