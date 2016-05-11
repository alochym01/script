#!/bin/bash
export http_proxy="http://proxy.hcm.fpt.vn:80"
export https_proxy="https://proxy.hcm.fpt.vn:80"
/home/hadn/python/bin/python /home/hadn/script/import_vtv_link_into_db.py
