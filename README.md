# Plex Scripts / Setup for Google Drive/gSuite

Running your own Plex Cloud with rclone, google cloud drive with either unionfs or overlayfs. I've also complied a custom kernel with fuse changes.

This is using rclone solely for mount and upload for GDRIVE. I've not been banned in over two months.

## My Setup

```
1) Sonarr/Radarr/NZBGET
2) Local Disk which keeps data until 80% full
3) Sonarr/Radarr notifications to update Plex (This uses the local disk copy via the UnionFS/OverlayFS mount, thus avoids bans)
4) Once disk reaches 80% the diskmonitor script will upload via rclone move to gdrive
```

### Prerequisites

What things you need to install the software and how to install them

```
* Ubuntu / Debian - For custom kernel to work
* Fully setup plex / rclone latest beta version
* Mount points for your local data / acd-crypt
* Ubunut 14.X requires overlayroot package (apt-get install overlayroot)
* You will also need Python3 with following modules (pip3 install requests jsonlibrpc-pelix)
```

### About

You have have a few options available to you, I have provided scripts for both UnionFS / OverlayFS (requires kernel 3.18+),
I've also compiled a custom kernel from source with fuse tuning.

### Installing / Deployment

To install you need to pull this git repo, you then can choose between UnionFS or OverlayFS
If you want OverlayFS you need kernel 3.18+, you can follow my kernel install below prior to running any scripts.

```
git clone https://bitbucket.com/jaketame/plexgsuite plexgsuite/
cd /opt/plexgsuite
chmod +x *
Amend plexgsuite.conf with your relevant paths
Copy sysctl.conf to /etc/sysctl.conf - Please ensure you verify no existing parameters exist, if this is a fresh install there won't be
```

Once you have the scripts locally update crontab.

Required

You can switch to OverlayFS if you wish from within the script
```
@reboot /opt/plexgsuite/mountgcd
```

You have two options for uploading to acd

Option 1 - Upload files to cloud based on local filesystem free space, run this in the background

```
./opt/plexgsuite/diskmonitor
```

Option 2 - Upload files every 6 hours

```
0 */6 * * * /opt/plexgsuite/uploadgcd
```

### Custom Kernel

This kernel has been complied from source and includes overlayfs and tuning changes to fuse, you can view more here

```
Once you have git pulled the repo, you can install the custom kernel version 4.4.52
cd kernel
cd 4.4.52
dpkg -i linux-*.deb
reboot
uname -a # Verify new kernel
```

### Plex Settings

I don't have any fancy scripts running but I have disabled most of Plex scanning to avoid Google Bans

View the attached .png files to see what settings i'm running with.s
