# crypto-sdcard
Configuration files for unlocking and mounting encrypted SD-cards, using udev, udisks2, polkit (older versions) and systemd.

Extensively tested with systend 225 (which includes udev), udisks2 2.7.5 and polkit 0.104.

RPM spec file is for SailfishOS 2.2, which provides aforementioned environment.
The packaged RPM will be released on [OpenRepos](https://openrepos.net/user/5928/programs) someday.
The necessary steps to prepare an SD-card are described on [Together.Jolla.com](https://together.jolla.com/question/179054/how-to-creating-partitions-on-sd-card-optionally-encrypted/).

Note that the "key"-file resides unencrypted on fixed mass storage, as mobile devices usually have only a single user, who unlocks the whole device.
