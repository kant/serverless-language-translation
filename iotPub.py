# Copyright 2018 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
import requests
def main(dict):
    iot_org_id = dict['iot_org_id']
    device_id = dict['device_id']
    device_type = dict['device_type']
    api_token = dict['api_token']
    r = requests.post('http://' + iot_org_id + '.messaging.internetofthings.ibmcloud.com:1883/api/v0002/device/types/' + device_type '/devices/' + device_id + '/events/query', headers={'Content-Type': 'application/json'}, json={'payload': dict['payload'], 'client': dict['client'], 'language': dict['language']}, auth=('use-token-auth', api_token))
    return {'msg': dict['msg']['text']}
