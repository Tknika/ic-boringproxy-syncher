# IoMBian Configurator Boringproxy Syncher

This service synchronizes the users registered in the [IoMBian Configurator platform](https://iombian-configurator.web.app/) with those of a boringproxy instance. 

To achieve this, the program needs two key configuration parameters:

- A Firebase project service account. The file "service_account_key.json" must be copied to the root folder of the service (/opt/ic-boringproxy-syncher).
- The domain from which the boringproxy server is accessible and the "admin" user's access token. These two parameters must be passed as the following environment variables: "BORINGPROXY_DOMAIN" and "BORINGPROXY_TOKEN".


## Installation

- Clone the repo into a temp folder:

> ```git clone https://github.com/Tknika/ic-boringproxy-syncher.git /tmp/ic-boringproxy-syncher && cd /tmp/ic-boringproxy-syncher```

- Create the installation folder and move the appropiate files (**edit the user**):

> ```sudo mkdir /opt/ic-boringproxy-syncher```

> ```sudo cp requirements.txt /opt/ic-boringproxy-syncher```

> ```sudo cp -r src/* /opt/ic-boringproxy-syncher```

> ```sudo cp systemd/ic-boringproxy-syncher.service /etc/systemd/system/```

> ```sudo chown -R aiturrioz:aiturrioz /opt/ic-boringproxy-syncher```

- Create the virtual environment and install the dependencies:

> ```cd /opt/ic-boringproxy-syncher```

> ```python3 -m venv venv```

> ```source venv/bin/activate```

> ```pip install --upgrade pip```

> ```pip install -r requirements.txt```

- Start the script

> ```sudo systemctl enable ic-boringproxy-syncher.service && sudo systemctl start ic-boringproxy-syncher.service```


## Author

(c) 2022 [Aitor Iturrioz Rodríguez](https://github.com/bodiroga)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.