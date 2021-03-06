# Commented out default values with details are displayed below. To override
# these default values, uncomment the values, rename the file to settings.py
# and place it in a supported config location

# Do not modify this file directly, it will not be picked up unless the filename
# is changed to settings.py

#DOWNLOAD_PROGRESS = True

# Directories for data and cached downloaded images
#DATA_DIR = "/var/lib/testcloud/"
#CACHE_DIR = "/var/lib/testcloud/cache"

# Data for cloud-init

#PASSWORD = 'passw0rd'
#HOSTNAME = 'testcloud'

#META_DATA = """instance-id: iid-123456
#local-hostname: %s
#"""
#USER_DATA = """#cloud-config
#password: %s
#chpasswd: { expire: False }
#ssh_pwauth: True
#"""
#ATOMIC_USER_DATA = """#cloud-config
#password: %s
#chpasswd: { expire: False }
#ssh_pwauth: True
#runcmd:
#  - [ sh, -c, 'echo -e "ROOT_SIZE=4G\nDATA_SIZE=10G" > /etc/sysconfig/docker-storage-setup']
#"""
#
# Extra cmdline args for the qemu invocation.
# Customize as needed :)

#CMD_LINE_ARGS = []
