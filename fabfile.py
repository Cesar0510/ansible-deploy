#! /usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------
# Copyright:   (c) Cesar Herdenez (2017)
# Licence:     BSD 3-Clause License
#--------------------------------------


from fabric.api import env, run 
from fabric.api import local 


env.user = ##
env.hosts = [] #
env.key_filename = #


def host():
    run('uname -u')
    
