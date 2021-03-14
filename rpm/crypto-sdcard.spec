Name:          crypto-sdcard
Summary:       Configuration files for unlocking and mounting encrypted SD-cards automatically
Version:       1.4.2
# Since v1.3.1, the release version consists of two or three fields, separated by a dot ("."):
# - The first field must contain a natural number greater than zero.
#   This number may be prefixed by one of {alpha,beta,stable}, e.g. "alpha13".
# - The second field indicates the minimal required SailfishOS version A.B.C.X in the format "sfosABC";
#   the fourth field of a SailfishOS version ("X") is neither depended upon or denoted.
#   A single, additional word out of {regular,qcrypto} is directly appended, resulting in the whole
#   second field containing e.g., "sfosABCregular".
# - An optional third field might be used by downstream packagers, who alter the package but want to
#   retain the exact version number.  It shall consist of the packager's name appended with a natural 
#   number greater than zero, e.g "joe8".
Release:       1.sfos340regular
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}-%{release}/%{name}-%{version}-%{release}.tar.gz
# rpmbuild (as of v4.14.1) handles the Icon tag awkwardly and in contrast to the Source tag(s):
# It only accepts a GIF or XPM file (a path is stripped to its basename) in the SOURCES directory
# (but not inside a tarball there)!  Successfully tested GIF89a and XPMv3, but an XPM icon results
# in bad visual quality and large file size.
# Hence only to be used, when the file (or a symlink to it) is put there:
#Icon:          smartmedia_mount.256x256.gif
BuildArch:     noarch
Requires:      systemd
Requires:      polkit
Requires:      udisks2 >= 2.8.1+git5-1.12.1.jolla
# Better use direct dependencies than indirect ones (here: the line above versus the one below), but
# ultimately decided to use both in this case:
Requires:      sailfish-version >= 3.4.0
# Omit anti-dependency on future, untested SFOS versions, until a known conflict exists:
Requires:      sailfish-version < 4.0.1
Requires:      cryptsetup >= 1.4.0
# Necessary counter-dependency to https://github.com/Olf0/crypto-sdcard/blob/qcrypto/rpm/crypto-sdcard.spec#L40
Conflicts:     kernel-adaptation-sbj
# ..., see requirement 3 at https://github.com/Olf0/crypto-sdcard/blob/master/RPM-dependencies_Git-workflow.md#requirements
Conflicts:     crypto-sdcard_sbj

%description
%{summary}
"Key"-file naming scheme: /etc/%{name}/crypto_luks_<UUID>.key rsp. /etc/%{name}/crypto_plain_<device-name>.key

%prep
%setup -n %{name}-%{version}-%{release}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp -R systemd polkit-1 udev %{buildroot}%{_sysconfdir}/

%files
%defattr(-,root,root,-)
# Files which may be altered by user:
%config %{_sysconfdir}/systemd/system/cryptosd-plain@.service
# Regular files:
%{_sysconfdir}/systemd/system/cryptosd-luks@.service
%{_sysconfdir}/systemd/system/mount-cryptosd-luks@.service
%{_sysconfdir}/systemd/system/mount-cryptosd-plain@.service
%{_sysconfdir}/polkit-1/localauthority/50-local.d/69-cryptosd.pkla
%{_sysconfdir}/udev/rules.d/96-cryptosd.rules
# Extraordinary files / dirs:
%defattr(0640,root,root,0750)
%dir %{_sysconfdir}/%{name}

