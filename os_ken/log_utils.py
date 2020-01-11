# Copyright (C) 2011 Nippon Telegraph and Telephone Corporation.
# Copyright (C) 2011 Isaku Yamahata <yamahata at valinux co jp>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os
import sys

LOG = logging.getLogger(__name__)


def get_fname(stack_frame):
    fname = sys._getframe(stack_frame).f_code.co_name
    return fname

def log_entry():

    # We are logging the function which called this function and its caller
    fname = get_fname(1)
    caller = get_fname(2)

    # Log name of executing function and name of caller
    LOG.info(fname +"(): caller: " +caller)

def log_entry_msg(msg):

    # We are logging the function which called this function and its caller
    fname = get_fname(1)
    caller = get_fname(2)

    # Log name of executing function and name of caller
    LOG.info(fname +"(): caller: " +caller +" [" +msg +"]")
